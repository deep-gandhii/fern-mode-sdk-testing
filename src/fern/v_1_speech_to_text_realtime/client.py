import websockets.sync.client as websockets_sync_client
from typing import Any, Optional, Iterator
from contextlib import contextmanager
from ..services.v_1_speech_to_text_realtime_channel import (
    V1SpeechToTextRealtimeSocketClient,
)
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.cast_models import cast_models
from ..net.transport.websocket_compat import (
    InvalidWebSocketStatus,
    InvalidWebSocketUri,
    get_status_code,
    has_handshake_header,
    merge_handshake_headers,
    redact_url,
    websocket_url,
)
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable, AsyncIterator
from contextlib import asynccontextmanager
from ..net.transport.websocket_compat import async_websocket_connect, websocket_url
from ..services.v_1_speech_to_text_realtime_channel import (
    AsyncV1SpeechToTextRealtimeSocketClient,
)


class V1SpeechToTextRealtimeClient(BaseService):
    """
    Fern-style resource client for V1SpeechToTextRealtimeClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response

    @property
    def with_raw_response(self) -> "RawV1SpeechToTextRealtimeClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawV1SpeechToTextRealtimeClient(self)

    @contextmanager
    def connect(
        self,
        *,
        model_id: str,
        token: Optional[str] = None,
        audio_format: Optional[str] = None,
        language_code: Optional[str] = None,
        secondary_languages: Optional[str] = None,
        commit_strategy: Optional[str] = None,
        vad_threshold: Optional[str] = None,
        vad_silence_threshold_secs: Optional[str] = None,
        min_speech_duration_ms: Optional[str] = None,
        min_silence_duration_ms: Optional[str] = None,
        include_timestamps: Optional[str] = None,
        include_language_detection: Optional[str] = None,
        keyterms: Optional[str] = None,
        no_verbatim: Optional[str] = None,
        entity_detection: Optional[str] = None,
        filter_background_audio: Optional[str] = None,
        enable_logging: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["V1SpeechToTextRealtimeSocketClient"]:
        """
        Open a websocket connection to /v1/speech-to-text/realtime.

        Yields a :class:`V1SpeechToTextRealtimeSocketClient` for the lifetime of the connection; the socket
        is closed when the context manager exits.
        """
        resolved_config = self._get_resolved_config(None, request_options)
        base_url = (
            self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url
        )
        ws_url = websocket_url(base_url, "/v1/speech-to-text/realtime")

        ws_url = (
            Serializer(ws_url)
            .add_channel_query("model_id", model_id)
            .add_channel_query("token", token)
            .add_channel_query("audio_format", audio_format)
            .add_channel_query("language_code", language_code)
            .add_channel_query("secondary_languages", secondary_languages)
            .add_channel_query("commit_strategy", commit_strategy)
            .add_channel_query("vad_threshold", vad_threshold)
            .add_channel_query("vad_silence_threshold_secs", vad_silence_threshold_secs)
            .add_channel_query("min_speech_duration_ms", min_speech_duration_ms)
            .add_channel_query("min_silence_duration_ms", min_silence_duration_ms)
            .add_channel_query("include_timestamps", include_timestamps)
            .add_channel_query("include_language_detection", include_language_detection)
            .add_channel_query("keyterms", keyterms)
            .add_channel_query("no_verbatim", no_verbatim)
            .add_channel_query("entity_detection", entity_detection)
            .add_channel_query("filter_background_audio", filter_background_audio)
            .add_channel_query("enable_logging", enable_logging)
            .serialize()
            .url
        )

        client_headers = merge_handshake_headers(
            (self._service_config or {}).get("additional_headers")
        )
        static_headers: dict[str, str] = {}
        for header in self._default_headers.get_headers():
            static_headers = merge_handshake_headers(
                static_headers, header.get_headers()
            )
        connect_headers = {}
        connect_headers.update((request_options or {}).get("additional_headers") or {})
        headers = merge_handshake_headers(client_headers, static_headers)
        headers = merge_handshake_headers(headers, connect_headers)

        try:
            with websockets_sync_client.connect(
                ws_url, additional_headers=headers
            ) as protocol:
                yield V1SpeechToTextRealtimeSocketClient(websocket=protocol)
        except InvalidWebSocketUri as exc:
            raise ApiError(redact_url(str(exc))) from None
        except InvalidWebSocketStatus as exc:
            status_code = get_status_code(exc)
            if status_code == 401:
                raise ApiError(
                    status_code=status_code,
                    headers=dict(headers),
                    body="Websocket initialized with invalid credentials.",
                ) from exc
            raise ApiError(
                status_code=status_code,
                headers=dict(headers),
                body="Unexpected error when initializing websocket connection.",
            ) from exc


class RawV1SpeechToTextRealtimeClient:
    """
    Raw-response client for V1SpeechToTextRealtimeClient.

    Each method delegates to the matching :class:`V1SpeechToTextRealtimeClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: V1SpeechToTextRealtimeClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    @contextmanager
    def connect(
        self,
        *,
        model_id: str,
        token: Optional[str] = None,
        audio_format: Optional[str] = None,
        language_code: Optional[str] = None,
        secondary_languages: Optional[str] = None,
        commit_strategy: Optional[str] = None,
        vad_threshold: Optional[str] = None,
        vad_silence_threshold_secs: Optional[str] = None,
        min_speech_duration_ms: Optional[str] = None,
        min_silence_duration_ms: Optional[str] = None,
        include_timestamps: Optional[str] = None,
        include_language_detection: Optional[str] = None,
        keyterms: Optional[str] = None,
        no_verbatim: Optional[str] = None,
        entity_detection: Optional[str] = None,
        filter_background_audio: Optional[str] = None,
        enable_logging: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["V1SpeechToTextRealtimeSocketClient"]:
        """
        Open a websocket connection to /v1/speech-to-text/realtime, delegating to the client's connect.
        """
        with self._client.connect(
            model_id=model_id,
            token=token,
            audio_format=audio_format,
            language_code=language_code,
            secondary_languages=secondary_languages,
            commit_strategy=commit_strategy,
            vad_threshold=vad_threshold,
            vad_silence_threshold_secs=vad_silence_threshold_secs,
            min_speech_duration_ms=min_speech_duration_ms,
            min_silence_duration_ms=min_silence_duration_ms,
            include_timestamps=include_timestamps,
            include_language_detection=include_language_detection,
            keyterms=keyterms,
            no_verbatim=no_verbatim,
            entity_detection=entity_detection,
            filter_background_audio=filter_background_audio,
            enable_logging=enable_logging,
            request_options=request_options,
        ) as socket:
            yield socket


class AsyncV1SpeechToTextRealtimeClient(V1SpeechToTextRealtimeClient):
    """
    Async wrapper for V1SpeechToTextRealtimeClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawV1SpeechToTextRealtimeClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawV1SpeechToTextRealtimeClient(self)

    @asynccontextmanager
    async def connect(
        self,
        *,
        model_id: str,
        token: Optional[str] = None,
        audio_format: Optional[str] = None,
        language_code: Optional[str] = None,
        secondary_languages: Optional[str] = None,
        commit_strategy: Optional[str] = None,
        vad_threshold: Optional[str] = None,
        vad_silence_threshold_secs: Optional[str] = None,
        min_speech_duration_ms: Optional[str] = None,
        min_silence_duration_ms: Optional[str] = None,
        include_timestamps: Optional[str] = None,
        include_language_detection: Optional[str] = None,
        keyterms: Optional[str] = None,
        no_verbatim: Optional[str] = None,
        entity_detection: Optional[str] = None,
        filter_background_audio: Optional[str] = None,
        enable_logging: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncIterator["AsyncV1SpeechToTextRealtimeSocketClient"]:  # type: ignore[override]
        """
        Open a websocket connection to /v1/speech-to-text/realtime.
        """
        resolved_config = self._get_resolved_config(None, request_options)
        base_url = (
            self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url
        )
        ws_url = websocket_url(base_url, "/v1/speech-to-text/realtime")

        ws_url = (
            Serializer(ws_url)
            .add_channel_query("model_id", model_id)
            .add_channel_query("token", token)
            .add_channel_query("audio_format", audio_format)
            .add_channel_query("language_code", language_code)
            .add_channel_query("secondary_languages", secondary_languages)
            .add_channel_query("commit_strategy", commit_strategy)
            .add_channel_query("vad_threshold", vad_threshold)
            .add_channel_query("vad_silence_threshold_secs", vad_silence_threshold_secs)
            .add_channel_query("min_speech_duration_ms", min_speech_duration_ms)
            .add_channel_query("min_silence_duration_ms", min_silence_duration_ms)
            .add_channel_query("include_timestamps", include_timestamps)
            .add_channel_query("include_language_detection", include_language_detection)
            .add_channel_query("keyterms", keyterms)
            .add_channel_query("no_verbatim", no_verbatim)
            .add_channel_query("entity_detection", entity_detection)
            .add_channel_query("filter_background_audio", filter_background_audio)
            .add_channel_query("enable_logging", enable_logging)
            .serialize()
            .url
        )

        client_headers = merge_handshake_headers(
            (self._service_config or {}).get("additional_headers")
        )
        static_headers: dict[str, str] = {}
        for header in self._default_headers.get_headers():
            static_headers = merge_handshake_headers(
                static_headers, header.get_headers()
            )
        connect_headers = {}
        connect_headers.update((request_options or {}).get("additional_headers") or {})
        headers = merge_handshake_headers(client_headers, static_headers)
        headers = merge_handshake_headers(headers, connect_headers)

        try:
            async with async_websocket_connect(ws_url, headers=headers) as protocol:
                yield AsyncV1SpeechToTextRealtimeSocketClient(websocket=protocol)
        except InvalidWebSocketUri as exc:
            raise ApiError(redact_url(str(exc))) from None
        except InvalidWebSocketStatus as exc:
            status_code = get_status_code(exc)
            if status_code == 401:
                raise ApiError(
                    status_code=status_code,
                    headers=dict(headers),
                    body="Websocket initialized with invalid credentials.",
                ) from exc
            raise ApiError(
                status_code=status_code,
                headers=dict(headers),
                body="Unexpected error when initializing websocket connection.",
            ) from exc


class AsyncRawV1SpeechToTextRealtimeClient:
    """
    Async raw-response client for AsyncV1SpeechToTextRealtimeClient.
    """

    def __init__(self, client: AsyncV1SpeechToTextRealtimeClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    @asynccontextmanager
    async def connect(
        self,
        *,
        model_id: str,
        token: Optional[str] = None,
        audio_format: Optional[str] = None,
        language_code: Optional[str] = None,
        secondary_languages: Optional[str] = None,
        commit_strategy: Optional[str] = None,
        vad_threshold: Optional[str] = None,
        vad_silence_threshold_secs: Optional[str] = None,
        min_speech_duration_ms: Optional[str] = None,
        min_silence_duration_ms: Optional[str] = None,
        include_timestamps: Optional[str] = None,
        include_language_detection: Optional[str] = None,
        keyterms: Optional[str] = None,
        no_verbatim: Optional[str] = None,
        entity_detection: Optional[str] = None,
        filter_background_audio: Optional[str] = None,
        enable_logging: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncIterator["AsyncV1SpeechToTextRealtimeSocketClient"]:
        """
        Open a websocket connection to /v1/speech-to-text/realtime, delegating to the client's connect.
        """
        async with self._client.connect(
            model_id=model_id,
            token=token,
            audio_format=audio_format,
            language_code=language_code,
            secondary_languages=secondary_languages,
            commit_strategy=commit_strategy,
            vad_threshold=vad_threshold,
            vad_silence_threshold_secs=vad_silence_threshold_secs,
            min_speech_duration_ms=min_speech_duration_ms,
            min_silence_duration_ms=min_silence_duration_ms,
            include_timestamps=include_timestamps,
            include_language_detection=include_language_detection,
            keyterms=keyterms,
            no_verbatim=no_verbatim,
            entity_detection=entity_detection,
            filter_background_audio=filter_background_audio,
            enable_logging=enable_logging,
            request_options=request_options,
        ) as socket:
            yield socket
