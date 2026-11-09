from typing import Any, Optional, Generator, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.cast_models import cast_models
from ...types import HttpValidationError
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable, AsyncGenerator
import asyncio
import threading


class PreviewClient(BaseService):
    """
    Fern-style resource client for PreviewClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._stream_config: SdkConfig = {}

    def set_stream_config(self, config: SdkConfig):
        """
        Sets method-level configuration for stream.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._stream_config = config
        return self

    @property
    def with_raw_response(self) -> "RawPreviewClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawPreviewClient(self)

    @cast_models
    def stream(
        self,
        generated_voice_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Stream a voice preview that was created via the /v1/text-to-voice/design endpoint.

        Parameters
        ----------
        generated_voice_id : str
            The generated_voice_id to stream.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            Streaming audio data

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.text_to_voice.preview.stream(
            generated_voice_id="37HceQefKmEi3bGovXjL",
        )
        for chunk in response:
            print(chunk)
        """

        Validator(str).validate(generated_voice_id, "generated_voice_id")

        resolved_config = self._get_resolved_config(
            self._stream_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/text-to-voice/{{generated_voice_id}}/stream",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("generated_voice_id", generated_voice_id)
            .serialize()
            .set_method("GET")
            .set_binary_download()
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response


class RawPreviewClient:
    """
    Raw-response client for PreviewClient.

    Each method delegates to the matching :class:`PreviewClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: PreviewClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def stream(
        self,
        generated_voice_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = PreviewClient.stream(
            _call_client, generated_voice_id, request_options=request_options
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )


class AsyncPreviewClient(PreviewClient):
    """
    Async wrapper for PreviewClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawPreviewClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawPreviewClient(self)

    def stream(
        self,
        generated_voice_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Stream a voice preview that was created via the /v1/text-to-voice/design endpoint.

        Parameters
        ----------
        generated_voice_id : str
            The generated_voice_id to stream.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Streaming audio data

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.text_to_voice.preview.stream(
                generated_voice_id="37HceQefKmEi3bGovXjL",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().stream(
            generated_voice_id, request_options=request_options
        )

        async def async_generator():
            exhausted = object()
            closing = threading.Event()

            def pull():
                try:
                    return next(sync_generator, exhausted)
                finally:
                    if closing.is_set():
                        sync_generator.close()

            try:
                while True:
                    item = await asyncio.to_thread(pull)
                    if item is exhausted:
                        return
                    yield item
            finally:
                closing.set()
                try:
                    sync_generator.close()
                except ValueError as error:
                    if "already executing" not in str(error):
                        raise

        return async_generator()


class AsyncRawPreviewClient:
    """
    Async raw-response client for AsyncPreviewClient.
    """

    def __init__(self, client: AsyncPreviewClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def stream(
        self,
        generated_voice_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncPreviewClient.stream(
            _call_client, generated_voice_id, request_options=request_options
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )
