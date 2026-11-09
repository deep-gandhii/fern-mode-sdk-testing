import json
import logging
import typing
from json.decoder import JSONDecodeError

import websockets
import websockets.sync.connection as websockets_sync_connection

try:
    from websockets.legacy.client import WebSocketClientProtocol  # type: ignore
except ImportError:
    from websockets import WebSocketClientProtocol  # type: ignore

from pydantic import TypeAdapter
from ..net.transport.events import EventEmitterMixin, EventType
from ..net.transport.websocket_state import WebSocketState, resolve_websocket_state
from ..types import (
    CommittedTranscriptEntitiesPayload,
    CommittedTranscriptPayload,
    CommittedTranscriptWithTimestampsPayload,
    InputAudioChunkPayload,
    PartialTranscriptPayload,
    ReceiveTranscription,
    ScribeAuthErrorPayload,
    ScribeChunkSizeExceededErrorPayload,
    ScribeErrorPayload,
    ScribeInputErrorPayload,
    ScribeInsufficientAudioActivityErrorPayload,
    ScribeQueueOverflowErrorPayload,
    ScribeQuotaExceededErrorPayload,
    ScribeRateLimitedErrorPayload,
    ScribeResourceExhaustedErrorPayload,
    ScribeSessionTimeLimitExceededErrorPayload,
    ScribeThrottledErrorPayload,
    ScribeTranscriberErrorPayload,
    ScribeUnacceptedTermsErrorPayload,
    SessionStartedPayload,
)

_logger = logging.getLogger(__name__)

V1SpeechToTextRealtimeSocketClientResponse = typing.Union[
    bytes,
    str,
    None,
    SessionStartedPayload,
    PartialTranscriptPayload,
    CommittedTranscriptPayload,
    CommittedTranscriptWithTimestampsPayload,
    CommittedTranscriptEntitiesPayload,
    ScribeErrorPayload,
    ScribeAuthErrorPayload,
    ScribeQuotaExceededErrorPayload,
    ScribeThrottledErrorPayload,
    ScribeUnacceptedTermsErrorPayload,
    ScribeRateLimitedErrorPayload,
    ScribeQueueOverflowErrorPayload,
    ScribeResourceExhaustedErrorPayload,
    ScribeSessionTimeLimitExceededErrorPayload,
    ScribeInputErrorPayload,
    ScribeChunkSizeExceededErrorPayload,
    ScribeInsufficientAudioActivityErrorPayload,
    ScribeTranscriberErrorPayload,
    ReceiveTranscription,
]
_UNDISCRIMINATED_ADAPTER = TypeAdapter(ReceiveTranscription)


class V1SpeechToTextRealtimeSocketClient(EventEmitterMixin):
    def __init__(self, *, websocket: websockets_sync_connection.Connection):
        super().__init__()
        self._websocket = websocket

    @property
    def state(self) -> WebSocketState:
        """
        The current connection state, as reported by the underlying websocket.
        """
        return resolve_websocket_state(self._websocket)

    def __iter__(self):
        for message in self._websocket:
            parsed = self._parse(message)
            if parsed is not None:
                yield parsed

    def start_listening(self):
        """
        Start listening for messages on the websocket connection.

        Emits EventType.OPEN, then EventType.MESSAGE per message, EventType.ERROR on
        failure, and EventType.CLOSE when the connection ends.
        """
        self._emit(EventType.OPEN, None)
        try:
            for raw_message in self._websocket:
                parsed = self._parse(raw_message)
                if parsed is not None:
                    self._emit(EventType.MESSAGE, parsed)
        except (websockets.WebSocketException, JSONDecodeError) as exc:
            self._emit(EventType.ERROR, exc)
        finally:
            self._emit(EventType.CLOSE, None)

    def recv(self) -> "V1SpeechToTextRealtimeSocketClientResponse":
        """
        Receive a single message from the websocket connection.
        """
        return self._parse(self._websocket.recv())

    def send_publish(self, message: InputAudioChunkPayload) -> None:
        """
        Send a InputAudioChunkPayload message to the websocket connection.
        """
        self.send_model(message)

    def send(self, data: typing.Any) -> None:
        """
        Send a raw message to the websocket connection.
        """
        if isinstance(data, dict):
            data = json.dumps(data)
        self._websocket.send(data)

    def send_model(self, data: typing.Any) -> None:
        """
        Send a model to the websocket connection.
        """
        self.send(data.model_dump(by_alias=True, exclude_none=True))

    def _parse(
        self, message: typing.Any
    ) -> "V1SpeechToTextRealtimeSocketClientResponse":
        if isinstance(message, bytes):
            return message
        try:
            json_data = json.loads(message)
        except JSONDecodeError:
            return message
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "session_started"
        ):
            try:
                return SessionStartedPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed SessionStartedPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "partial_transcript"
        ):
            try:
                return PartialTranscriptPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed PartialTranscriptPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "committed_transcript"
        ):
            try:
                return CommittedTranscriptPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed CommittedTranscriptPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "committed_transcript_with_timestamps"
        ):
            try:
                return CommittedTranscriptWithTimestampsPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed CommittedTranscriptWithTimestampsPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "committed_transcript_entities"
        ):
            try:
                return CommittedTranscriptEntitiesPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed CommittedTranscriptEntitiesPayload WebSocket message."
                )
                return None
        if isinstance(json_data, dict) and json_data.get("message_type") == "error":
            try:
                return ScribeErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "auth_error"
        ):
            try:
                return ScribeAuthErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeAuthErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "quota_exceeded"
        ):
            try:
                return ScribeQuotaExceededErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeQuotaExceededErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "commit_throttled"
        ):
            try:
                return ScribeThrottledErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeThrottledErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "unaccepted_terms"
        ):
            try:
                return ScribeUnacceptedTermsErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeUnacceptedTermsErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "rate_limited"
        ):
            try:
                return ScribeRateLimitedErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeRateLimitedErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "queue_overflow"
        ):
            try:
                return ScribeQueueOverflowErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeQueueOverflowErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "resource_exhausted"
        ):
            try:
                return ScribeResourceExhaustedErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeResourceExhaustedErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "session_time_limit_exceeded"
        ):
            try:
                return ScribeSessionTimeLimitExceededErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeSessionTimeLimitExceededErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "input_error"
        ):
            try:
                return ScribeInputErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeInputErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "chunk_size_exceeded"
        ):
            try:
                return ScribeChunkSizeExceededErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeChunkSizeExceededErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "insufficient_audio_activity"
        ):
            try:
                return ScribeInsufficientAudioActivityErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeInsufficientAudioActivityErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "transcriber_error"
        ):
            try:
                return ScribeTranscriberErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeTranscriberErrorPayload WebSocket message."
                )
                return None
        try:
            return _UNDISCRIMINATED_ADAPTER.validate_python(json_data)
        except Exception:
            _logger.warning(
                "Skipping unknown WebSocket message; update your SDK version to support new message types."
            )
            return None


class AsyncV1SpeechToTextRealtimeSocketClient(EventEmitterMixin):
    def __init__(self, *, websocket: WebSocketClientProtocol):
        super().__init__()
        self._websocket = websocket

    @property
    def state(self) -> WebSocketState:
        """
        The current connection state, as reported by the underlying websocket.
        """
        return resolve_websocket_state(self._websocket)

    async def __aiter__(self):
        async for message in self._websocket:
            parsed = self._parse(message)
            if parsed is not None:
                yield parsed

    async def start_listening(self):
        """
        Start listening for messages on the websocket connection.

        Emits EventType.OPEN, then EventType.MESSAGE per message, EventType.ERROR on
        failure, and EventType.CLOSE when the connection ends.
        """
        await self._emit_async(EventType.OPEN, None)
        try:
            async for raw_message in self._websocket:
                parsed = self._parse(raw_message)
                if parsed is not None:
                    await self._emit_async(EventType.MESSAGE, parsed)
        except (websockets.WebSocketException, JSONDecodeError) as exc:
            await self._emit_async(EventType.ERROR, exc)
        finally:
            await self._emit_async(EventType.CLOSE, None)

    async def recv(self) -> "V1SpeechToTextRealtimeSocketClientResponse":
        """
        Receive a single message from the websocket connection.
        """
        return self._parse(await self._websocket.recv())

    async def send_publish(self, message: InputAudioChunkPayload) -> None:
        """
        Send a InputAudioChunkPayload message to the websocket connection.
        """
        await self.send_model(message)

    async def send(self, data: typing.Any) -> None:
        """
        Send a raw message to the websocket connection.
        """
        if isinstance(data, dict):
            data = json.dumps(data)
        await self._websocket.send(data)

    async def send_model(self, data: typing.Any) -> None:
        """
        Send a model to the websocket connection.
        """
        await self.send(data.model_dump(by_alias=True, exclude_none=True))

    def _parse(
        self, message: typing.Any
    ) -> "V1SpeechToTextRealtimeSocketClientResponse":
        if isinstance(message, bytes):
            return message
        try:
            json_data = json.loads(message)
        except JSONDecodeError:
            return message
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "session_started"
        ):
            try:
                return SessionStartedPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed SessionStartedPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "partial_transcript"
        ):
            try:
                return PartialTranscriptPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed PartialTranscriptPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "committed_transcript"
        ):
            try:
                return CommittedTranscriptPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed CommittedTranscriptPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "committed_transcript_with_timestamps"
        ):
            try:
                return CommittedTranscriptWithTimestampsPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed CommittedTranscriptWithTimestampsPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "committed_transcript_entities"
        ):
            try:
                return CommittedTranscriptEntitiesPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed CommittedTranscriptEntitiesPayload WebSocket message."
                )
                return None
        if isinstance(json_data, dict) and json_data.get("message_type") == "error":
            try:
                return ScribeErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "auth_error"
        ):
            try:
                return ScribeAuthErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeAuthErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "quota_exceeded"
        ):
            try:
                return ScribeQuotaExceededErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeQuotaExceededErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "commit_throttled"
        ):
            try:
                return ScribeThrottledErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeThrottledErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "unaccepted_terms"
        ):
            try:
                return ScribeUnacceptedTermsErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeUnacceptedTermsErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "rate_limited"
        ):
            try:
                return ScribeRateLimitedErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeRateLimitedErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "queue_overflow"
        ):
            try:
                return ScribeQueueOverflowErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeQueueOverflowErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "resource_exhausted"
        ):
            try:
                return ScribeResourceExhaustedErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeResourceExhaustedErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "session_time_limit_exceeded"
        ):
            try:
                return ScribeSessionTimeLimitExceededErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeSessionTimeLimitExceededErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "input_error"
        ):
            try:
                return ScribeInputErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeInputErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "chunk_size_exceeded"
        ):
            try:
                return ScribeChunkSizeExceededErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeChunkSizeExceededErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "insufficient_audio_activity"
        ):
            try:
                return ScribeInsufficientAudioActivityErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeInsufficientAudioActivityErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "transcriber_error"
        ):
            try:
                return ScribeTranscriberErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed ScribeTranscriberErrorPayload WebSocket message."
                )
                return None
        try:
            return _UNDISCRIMINATED_ADAPTER.validate_python(json_data)
        except Exception:
            _logger.warning(
                "Skipping unknown WebSocket message; update your SDK version to support new message types."
            )
            return None
