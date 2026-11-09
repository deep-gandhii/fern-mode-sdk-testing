from typing import Any, Optional, Generator, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.cast_models import cast_models
from ....types import HttpValidationError
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable, AsyncGenerator
import asyncio
import threading


class AudioClient(BaseService):
    """
    Fern-style resource client for AudioClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._get_config: SdkConfig = {}

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    @property
    def with_raw_response(self) -> "RawAudioClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawAudioClient(self)

    @cast_models
    def get(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Returns the audio corresponding to a sample attached to a voice.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        sample_id : str
            ID of the sample to be used. You can use the [Get voices](/docs/api-reference/voices/get) endpoint list all the available samples for a voice.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.voices.samples.audio.get(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            sample_id="VW7YKqPnjY4h39yTbx2L",
        )
        for chunk in response:
            print(chunk)
        """

        Validator(str).validate(voice_id, "voice_id")
        Validator(str).validate(sample_id, "sample_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/{{voice_id}}/samples/{{sample_id}}/audio",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .add_path("sample_id", sample_id)
            .serialize()
            .set_method("GET")
            .set_binary_download()
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response


class RawAudioClient:
    """
    Raw-response client for AudioClient.

    Each method delegates to the matching :class:`AudioClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: AudioClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = AudioClient.get(
            _call_client, voice_id, sample_id, request_options=request_options
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )


class AsyncAudioClient(AudioClient):
    """
    Async wrapper for AudioClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawAudioClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawAudioClient(self)

    def get(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Returns the audio corresponding to a sample attached to a voice.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        sample_id : str
            ID of the sample to be used. You can use the [Get voices](/docs/api-reference/voices/get) endpoint list all the available samples for a voice.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.voices.samples.audio.get(
                voice_id="21m00Tcm4TlvDq8ikWAM",
                sample_id="VW7YKqPnjY4h39yTbx2L",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().get(
            voice_id, sample_id, request_options=request_options
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


class AsyncRawAudioClient:
    """
    Async raw-response client for AsyncAudioClient.
    """

    def __init__(self, client: AsyncAudioClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncAudioClient.get(
            _call_client, voice_id, sample_id, request_options=request_options
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )
