import websockets.sync.client as websockets_sync_client
from typing import Any, Optional, Iterator
from contextlib import contextmanager
from ..services.v_1_translate_realtime_channel import V1TranslateRealtimeSocketClient
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
from ..services.v_1_translate_realtime_channel import (
    AsyncV1TranslateRealtimeSocketClient,
)


class V1TranslateRealtimeClient(BaseService):
    """
    Fern-style resource client for V1TranslateRealtimeClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response

    @property
    def with_raw_response(self) -> "RawV1TranslateRealtimeClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawV1TranslateRealtimeClient(self)

    @contextmanager
    def connect(
        self,
        *,
        target_language: str,
        voice_id: str,
        authorization: Optional[str] = None,
        source_language: Optional[str] = None,
        input_format: Optional[str] = None,
        output_format: Optional[str] = None,
        tts_model_id: Optional[str] = None,
        client_session_id: Optional[str] = None,
        enable_zrm: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["V1TranslateRealtimeSocketClient"]:
        """
        Open a websocket connection to /v1/translate/realtime.

        Yields a :class:`V1TranslateRealtimeSocketClient` for the lifetime of the connection; the socket
        is closed when the context manager exits.
        """
        resolved_config = self._get_resolved_config(None, request_options)
        base_url = (
            self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url
        )
        ws_url = websocket_url(base_url, "/v1/translate/realtime")

        ws_url = (
            Serializer(ws_url)
            .add_channel_query("target_language", target_language)
            .add_channel_query("voice_id", voice_id)
            .add_channel_query("authorization", authorization)
            .add_channel_query("source_language", source_language)
            .add_channel_query("input_format", input_format)
            .add_channel_query("output_format", output_format)
            .add_channel_query("tts_model_id", tts_model_id)
            .add_channel_query("client_session_id", client_session_id)
            .add_channel_query("enable_zrm", enable_zrm)
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
                yield V1TranslateRealtimeSocketClient(websocket=protocol)
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


class RawV1TranslateRealtimeClient:
    """
    Raw-response client for V1TranslateRealtimeClient.

    Each method delegates to the matching :class:`V1TranslateRealtimeClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: V1TranslateRealtimeClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    @contextmanager
    def connect(
        self,
        *,
        target_language: str,
        voice_id: str,
        authorization: Optional[str] = None,
        source_language: Optional[str] = None,
        input_format: Optional[str] = None,
        output_format: Optional[str] = None,
        tts_model_id: Optional[str] = None,
        client_session_id: Optional[str] = None,
        enable_zrm: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["V1TranslateRealtimeSocketClient"]:
        """
        Open a websocket connection to /v1/translate/realtime, delegating to the client's connect.
        """
        with self._client.connect(
            target_language=target_language,
            voice_id=voice_id,
            authorization=authorization,
            source_language=source_language,
            input_format=input_format,
            output_format=output_format,
            tts_model_id=tts_model_id,
            client_session_id=client_session_id,
            enable_zrm=enable_zrm,
            request_options=request_options,
        ) as socket:
            yield socket


class AsyncV1TranslateRealtimeClient(V1TranslateRealtimeClient):
    """
    Async wrapper for V1TranslateRealtimeClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawV1TranslateRealtimeClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawV1TranslateRealtimeClient(self)

    @asynccontextmanager
    async def connect(
        self,
        *,
        target_language: str,
        voice_id: str,
        authorization: Optional[str] = None,
        source_language: Optional[str] = None,
        input_format: Optional[str] = None,
        output_format: Optional[str] = None,
        tts_model_id: Optional[str] = None,
        client_session_id: Optional[str] = None,
        enable_zrm: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncIterator["AsyncV1TranslateRealtimeSocketClient"]:  # type: ignore[override]
        """
        Open a websocket connection to /v1/translate/realtime.
        """
        resolved_config = self._get_resolved_config(None, request_options)
        base_url = (
            self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url
        )
        ws_url = websocket_url(base_url, "/v1/translate/realtime")

        ws_url = (
            Serializer(ws_url)
            .add_channel_query("target_language", target_language)
            .add_channel_query("voice_id", voice_id)
            .add_channel_query("authorization", authorization)
            .add_channel_query("source_language", source_language)
            .add_channel_query("input_format", input_format)
            .add_channel_query("output_format", output_format)
            .add_channel_query("tts_model_id", tts_model_id)
            .add_channel_query("client_session_id", client_session_id)
            .add_channel_query("enable_zrm", enable_zrm)
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
                yield AsyncV1TranslateRealtimeSocketClient(websocket=protocol)
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


class AsyncRawV1TranslateRealtimeClient:
    """
    Async raw-response client for AsyncV1TranslateRealtimeClient.
    """

    def __init__(self, client: AsyncV1TranslateRealtimeClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    @asynccontextmanager
    async def connect(
        self,
        *,
        target_language: str,
        voice_id: str,
        authorization: Optional[str] = None,
        source_language: Optional[str] = None,
        input_format: Optional[str] = None,
        output_format: Optional[str] = None,
        tts_model_id: Optional[str] = None,
        client_session_id: Optional[str] = None,
        enable_zrm: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncIterator["AsyncV1TranslateRealtimeSocketClient"]:
        """
        Open a websocket connection to /v1/translate/realtime, delegating to the client's connect.
        """
        async with self._client.connect(
            target_language=target_language,
            voice_id=voice_id,
            authorization=authorization,
            source_language=source_language,
            input_format=input_format,
            output_format=output_format,
            tts_model_id=tts_model_id,
            client_session_id=client_session_id,
            enable_zrm=enable_zrm,
            request_options=request_options,
        ) as socket:
            yield socket
