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

from ..net.transport.events import EventEmitterMixin, EventType
from ..net.transport.websocket_state import WebSocketState, resolve_websocket_state
from ..types import (
    SendTranslateStreamMessage,
    TranslateAudioOutputError,
    TranslateAudioPayload,
    TranslateAuthError,
    TranslateErrorPayload,
    TranslateFinalTranscriptPayload,
    TranslateInputError,
    TranslatePartialTranscriptPayload,
    TranslateQueueOverflowError,
    TranslateRateLimitedError,
    TranslateSessionStartedPayload,
    TranslateStatusPayload,
    TranslateTranscriberError,
    TranslateTranslationError,
    TranslateTranslationPayload,
)

_logger = logging.getLogger(__name__)

V1TranslateRealtimeSocketClientResponse = typing.Union[
    bytes,
    str,
    None,
    TranslateSessionStartedPayload,
    TranslateStatusPayload,
    TranslatePartialTranscriptPayload,
    TranslateFinalTranscriptPayload,
    TranslateTranslationPayload,
    TranslateAudioPayload,
    TranslateErrorPayload,
    TranslateAuthError,
    TranslateRateLimitedError,
    TranslateQueueOverflowError,
    TranslateInputError,
    TranslateTranscriberError,
    TranslateTranslationError,
    TranslateAudioOutputError,
]


class V1TranslateRealtimeSocketClient(EventEmitterMixin):
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

    def recv(self) -> "V1TranslateRealtimeSocketClientResponse":
        """
        Receive a single message from the websocket connection.
        """
        return self._parse(self._websocket.recv())

    def send_publish(self, message: SendTranslateStreamMessage) -> None:
        """
        Send a SendTranslateStreamMessage message to the websocket connection.
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

    def _parse(self, message: typing.Any) -> "V1TranslateRealtimeSocketClientResponse":
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
                return TranslateSessionStartedPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateSessionStartedPayload WebSocket message."
                )
                return None
        if isinstance(json_data, dict) and json_data.get("message_type") == "status":
            try:
                return TranslateStatusPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateStatusPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "partial_transcript"
        ):
            try:
                return TranslatePartialTranscriptPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslatePartialTranscriptPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "final_transcript"
        ):
            try:
                return TranslateFinalTranscriptPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateFinalTranscriptPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "translation"
        ):
            try:
                return TranslateTranslationPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateTranslationPayload WebSocket message."
                )
                return None
        if isinstance(json_data, dict) and json_data.get("message_type") == "audio":
            try:
                return TranslateAudioPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateAudioPayload WebSocket message."
                )
                return None
        if isinstance(json_data, dict) and json_data.get("message_type") == "error":
            try:
                return TranslateErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "auth_error"
        ):
            try:
                return TranslateAuthError._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateAuthError WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "rate_limited"
        ):
            try:
                return TranslateRateLimitedError._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateRateLimitedError WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "queue_overflow"
        ):
            try:
                return TranslateQueueOverflowError._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateQueueOverflowError WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "input_error"
        ):
            try:
                return TranslateInputError._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateInputError WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "transcriber_error"
        ):
            try:
                return TranslateTranscriberError._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateTranscriberError WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "translation_error"
        ):
            try:
                return TranslateTranslationError._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateTranslationError WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "audio_output_error"
        ):
            try:
                return TranslateAudioOutputError._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateAudioOutputError WebSocket message."
                )
                return None
        _logger.warning(
            "Skipping unknown WebSocket message; update your SDK version to support new message types."
        )
        return None


class AsyncV1TranslateRealtimeSocketClient(EventEmitterMixin):
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

    async def recv(self) -> "V1TranslateRealtimeSocketClientResponse":
        """
        Receive a single message from the websocket connection.
        """
        return self._parse(await self._websocket.recv())

    async def send_publish(self, message: SendTranslateStreamMessage) -> None:
        """
        Send a SendTranslateStreamMessage message to the websocket connection.
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

    def _parse(self, message: typing.Any) -> "V1TranslateRealtimeSocketClientResponse":
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
                return TranslateSessionStartedPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateSessionStartedPayload WebSocket message."
                )
                return None
        if isinstance(json_data, dict) and json_data.get("message_type") == "status":
            try:
                return TranslateStatusPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateStatusPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "partial_transcript"
        ):
            try:
                return TranslatePartialTranscriptPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslatePartialTranscriptPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "final_transcript"
        ):
            try:
                return TranslateFinalTranscriptPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateFinalTranscriptPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "translation"
        ):
            try:
                return TranslateTranslationPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateTranslationPayload WebSocket message."
                )
                return None
        if isinstance(json_data, dict) and json_data.get("message_type") == "audio":
            try:
                return TranslateAudioPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateAudioPayload WebSocket message."
                )
                return None
        if isinstance(json_data, dict) and json_data.get("message_type") == "error":
            try:
                return TranslateErrorPayload._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateErrorPayload WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "auth_error"
        ):
            try:
                return TranslateAuthError._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateAuthError WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "rate_limited"
        ):
            try:
                return TranslateRateLimitedError._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateRateLimitedError WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "queue_overflow"
        ):
            try:
                return TranslateQueueOverflowError._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateQueueOverflowError WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "input_error"
        ):
            try:
                return TranslateInputError._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateInputError WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "transcriber_error"
        ):
            try:
                return TranslateTranscriberError._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateTranscriberError WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "translation_error"
        ):
            try:
                return TranslateTranslationError._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateTranslationError WebSocket message."
                )
                return None
        if (
            isinstance(json_data, dict)
            and json_data.get("message_type") == "audio_output_error"
        ):
            try:
                return TranslateAudioOutputError._unmap(json_data)
            except Exception:
                _logger.warning(
                    "Discarding a malformed TranslateAudioOutputError WebSocket message."
                )
                return None
        _logger.warning(
            "Skipping unknown WebSocket message; update your SDK version to support new message types."
        )
        return None
