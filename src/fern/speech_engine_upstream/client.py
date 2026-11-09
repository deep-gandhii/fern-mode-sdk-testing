import websockets.sync.client as websockets_sync_client
from typing import Any, Optional, Iterator
from contextlib import contextmanager
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..services.speech_engine_upstream_channel import SpeechEngineUpstreamSocketClient
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
from ..services.speech_engine_upstream_channel import (
    AsyncSpeechEngineUpstreamSocketClient,
)


class SpeechEngineUpstreamClient(BaseService):
    """
    Fern-style resource client for SpeechEngineUpstreamClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response

    @property
    def with_raw_response(self) -> "RawSpeechEngineUpstreamClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawSpeechEngineUpstreamClient(self)

    @contextmanager
    def connect(
        self,
        *,
        x_eleven_labs_speech_engine_authorization: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["SpeechEngineUpstreamSocketClient"]:
        """
        Open a websocket connection to /speech-engine/upstream.

        Yields a :class:`SpeechEngineUpstreamSocketClient` for the lifetime of the connection; the socket
        is closed when the context manager exits.
        """
        resolved_config = self._get_resolved_config(None, request_options)
        base_url = (
            self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url
        )
        ws_url = websocket_url(base_url, "/speech-engine/upstream")

        client_headers = merge_handshake_headers(
            (self._service_config or {}).get("additional_headers")
        )
        static_headers: dict[str, str] = {}
        for header in self._default_headers.get_headers():
            static_headers = merge_handshake_headers(
                static_headers, header.get_headers()
            )
        connect_headers = {}
        if x_eleven_labs_speech_engine_authorization is not None:
            connect_headers["X-ElevenLabs-Speech-Engine-Authorization"] = str(
                getattr(
                    x_eleven_labs_speech_engine_authorization,
                    "value",
                    x_eleven_labs_speech_engine_authorization,
                )
            )
        connect_headers.update((request_options or {}).get("additional_headers") or {})
        headers = merge_handshake_headers(client_headers, static_headers)
        headers = merge_handshake_headers(headers, connect_headers)

        try:
            with websockets_sync_client.connect(
                ws_url, additional_headers=headers
            ) as protocol:
                yield SpeechEngineUpstreamSocketClient(websocket=protocol)
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


class RawSpeechEngineUpstreamClient:
    """
    Raw-response client for SpeechEngineUpstreamClient.

    Each method delegates to the matching :class:`SpeechEngineUpstreamClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: SpeechEngineUpstreamClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    @contextmanager
    def connect(
        self,
        *,
        x_eleven_labs_speech_engine_authorization: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["SpeechEngineUpstreamSocketClient"]:
        """
        Open a websocket connection to /speech-engine/upstream, delegating to the client's connect.
        """
        with self._client.connect(
            x_eleven_labs_speech_engine_authorization=x_eleven_labs_speech_engine_authorization,
            request_options=request_options,
        ) as socket:
            yield socket


class AsyncSpeechEngineUpstreamClient(SpeechEngineUpstreamClient):
    """
    Async wrapper for SpeechEngineUpstreamClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawSpeechEngineUpstreamClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawSpeechEngineUpstreamClient(self)

    @asynccontextmanager
    async def connect(
        self,
        *,
        x_eleven_labs_speech_engine_authorization: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncIterator["AsyncSpeechEngineUpstreamSocketClient"]:  # type: ignore[override]
        """
        Open a websocket connection to /speech-engine/upstream.
        """
        resolved_config = self._get_resolved_config(None, request_options)
        base_url = (
            self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url
        )
        ws_url = websocket_url(base_url, "/speech-engine/upstream")

        client_headers = merge_handshake_headers(
            (self._service_config or {}).get("additional_headers")
        )
        static_headers: dict[str, str] = {}
        for header in self._default_headers.get_headers():
            static_headers = merge_handshake_headers(
                static_headers, header.get_headers()
            )
        connect_headers = {}
        if x_eleven_labs_speech_engine_authorization is not None:
            connect_headers["X-ElevenLabs-Speech-Engine-Authorization"] = str(
                getattr(
                    x_eleven_labs_speech_engine_authorization,
                    "value",
                    x_eleven_labs_speech_engine_authorization,
                )
            )
        connect_headers.update((request_options or {}).get("additional_headers") or {})
        headers = merge_handshake_headers(client_headers, static_headers)
        headers = merge_handshake_headers(headers, connect_headers)

        try:
            async with async_websocket_connect(ws_url, headers=headers) as protocol:
                yield AsyncSpeechEngineUpstreamSocketClient(websocket=protocol)
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


class AsyncRawSpeechEngineUpstreamClient:
    """
    Async raw-response client for AsyncSpeechEngineUpstreamClient.
    """

    def __init__(self, client: AsyncSpeechEngineUpstreamClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    @asynccontextmanager
    async def connect(
        self,
        *,
        x_eleven_labs_speech_engine_authorization: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncIterator["AsyncSpeechEngineUpstreamSocketClient"]:
        """
        Open a websocket connection to /speech-engine/upstream, delegating to the client's connect.
        """
        async with self._client.connect(
            x_eleven_labs_speech_engine_authorization=x_eleven_labs_speech_engine_authorization,
            request_options=request_options,
        ) as socket:
            yield socket
