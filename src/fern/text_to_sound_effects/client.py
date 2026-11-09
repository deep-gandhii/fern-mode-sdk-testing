from typing import Any, Optional, Generator, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types import AllowedOutputFormats, CreateSoundEffectRequest, HttpValidationError
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable, AsyncGenerator
import asyncio
import threading


class TextToSoundEffectsClient(BaseService):
    """
    Fern-style resource client for TextToSoundEffectsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._convert_config: SdkConfig = {}

    def set_convert_config(self, config: SdkConfig):
        """
        Sets method-level configuration for convert.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._convert_config = config
        return self

    @property
    def with_raw_response(self) -> "RawTextToSoundEffectsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawTextToSoundEffectsClient(self)

    @cast_models
    def convert(
        self,
        *,
        text: str,
        loop: Optional[bool] = SENTINEL,
        duration_seconds: Union[float, None] = SENTINEL,
        prompt_influence: Union[float, None] = SENTINEL,
        model_id: Optional[str] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Turn text into sound effects for your videos, voice-overs or video games using the most advanced sound effects models in the world.

        Parameters
        ----------
        text : str
            The text that will get converted into a sound effect.

        loop : typing.Optional[bool]
            Whether to create a sound effect that loops smoothly. Only available for the 'eleven_text_to_sound_v2 model'.

        duration_seconds : typing.Optional[float]
            The duration of the sound which will be generated in seconds. Must be at least 0.5 and at most 30. If set to None we will guess the optimal duration using the prompt. Defaults to None.

        prompt_influence : typing.Optional[float]
            A higher prompt influence makes your generation follow the prompt more closely while also making generations less variable. Must be a value between 0 and 1. Defaults to 0.3.

        model_id : typing.Optional[str]
            The model ID to use for the sound generation.

        output_format : typing.Optional[AllowedOutputFormats]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            The generated sound effect as an MP3 file

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.text_to_sound_effects.convert(
            output_format="mp3_22050_32",
            text="Spacious braam suitable for high-impact movie trailer moments",
        )
        for chunk in response:
            print(chunk)
        """

        Validator(AllowedOutputFormats).is_optional().is_nullable().validate(
            output_format, "output_format"
        )

        resolved_config = self._get_resolved_config(
            self._convert_config, request_options
        )

        request_body = CreateSoundEffectRequest(
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "loop": loop,
                        "duration_seconds": duration_seconds,
                        "prompt_influence": prompt_influence,
                        "model_id": model_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(CreateSoundEffectRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/sound-generation",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("output_format", output_format, nullable=True)
            .serialize()
            .set_method("POST")
            .set_binary_download()
            .set_body(request_body)
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response


class RawTextToSoundEffectsClient:
    """
    Raw-response client for TextToSoundEffectsClient.

    Each method delegates to the matching :class:`TextToSoundEffectsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: TextToSoundEffectsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def convert(
        self,
        *,
        text: str,
        loop: Optional[bool] = SENTINEL,
        duration_seconds: Union[float, None] = SENTINEL,
        prompt_influence: Union[float, None] = SENTINEL,
        model_id: Optional[str] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = TextToSoundEffectsClient.convert(
            _call_client,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "loop": loop,
                        "duration_seconds": duration_seconds,
                        "prompt_influence": prompt_influence,
                        "model_id": model_id,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )


class AsyncTextToSoundEffectsClient(TextToSoundEffectsClient):
    """
    Async wrapper for TextToSoundEffectsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawTextToSoundEffectsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawTextToSoundEffectsClient(self)

    def convert(
        self,
        *,
        text: str,
        loop: Optional[bool] = SENTINEL,
        duration_seconds: Union[float, None] = SENTINEL,
        prompt_influence: Union[float, None] = SENTINEL,
        model_id: Optional[str] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Turn text into sound effects for your videos, voice-overs or video games using the most advanced sound effects models in the world.

        Parameters
        ----------
        text : str
            The text that will get converted into a sound effect.

        loop : typing.Optional[bool]
            Whether to create a sound effect that loops smoothly. Only available for the 'eleven_text_to_sound_v2 model'.

        duration_seconds : typing.Optional[float]
            The duration of the sound which will be generated in seconds. Must be at least 0.5 and at most 30. If set to None we will guess the optimal duration using the prompt. Defaults to None.

        prompt_influence : typing.Optional[float]
            A higher prompt influence makes your generation follow the prompt more closely while also making generations less variable. Must be a value between 0 and 1. Defaults to 0.3.

        model_id : typing.Optional[str]
            The model ID to use for the sound generation.

        output_format : typing.Optional[AllowedOutputFormats]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The generated sound effect as an MP3 file

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.text_to_sound_effects.convert(
                output_format="mp3_22050_32",
                text="Spacious braam suitable for high-impact movie trailer moments",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().convert(
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "loop": loop,
                        "duration_seconds": duration_seconds,
                        "prompt_influence": prompt_influence,
                        "model_id": model_id,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
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


class AsyncRawTextToSoundEffectsClient:
    """
    Async raw-response client for AsyncTextToSoundEffectsClient.
    """

    def __init__(self, client: AsyncTextToSoundEffectsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def convert(
        self,
        *,
        text: str,
        loop: Optional[bool] = SENTINEL,
        duration_seconds: Union[float, None] = SENTINEL,
        prompt_influence: Union[float, None] = SENTINEL,
        model_id: Optional[str] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncTextToSoundEffectsClient.convert(
            _call_client,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "loop": loop,
                        "duration_seconds": duration_seconds,
                        "prompt_influence": prompt_influence,
                        "model_id": model_id,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )
