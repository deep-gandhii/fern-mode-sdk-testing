from typing import Any, Optional, Generator, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types import (
    HttpValidationError,
    OutputFormatOfTheGeneratedAudio6,
    OutputFormatOfTheGeneratedAudio7,
    SpeechToSpeechRequest,
    SpeechToSpeechRequestFileFormat,
    SpeechToSpeechStreamRequest,
    SpeechToSpeechStreamRequestFileFormat,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable, AsyncGenerator
import asyncio
import threading


class SpeechToSpeechClient(BaseService):
    """
    Fern-style resource client for SpeechToSpeechClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._convert_config: SdkConfig = {}
        self._stream_config: SdkConfig = {}

    def set_convert_config(self, config: SdkConfig):
        """
        Sets method-level configuration for convert.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._convert_config = config
        return self

    def set_stream_config(self, config: SdkConfig):
        """
        Sets method-level configuration for stream.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._stream_config = config
        return self

    @property
    def with_raw_response(self) -> "RawSpeechToSpeechClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawSpeechToSpeechClient(self)

    @cast_models
    def convert(
        self,
        voice_id: str,
        *,
        audio: bytes,
        model_id: Optional[str] = SENTINEL,
        voice_settings: Union[str, None] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        remove_background_noise: Optional[bool] = SENTINEL,
        file_format: Union[SpeechToSpeechRequestFileFormat, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio6, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Transform audio from one voice to another. Maintain full control over emotion, timing and delivery.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. Use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        audio : core.File
            The audio file which holds the content and emotion that will control the generated speech.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for speech to speech, you can check this using the can_do_voice_conversion property.

        voice_settings : typing.Optional[str]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request. Needs to be send as a JSON encoded string.

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        remove_background_noise : typing.Optional[bool]
            If set, will remove the background noise from your audio input using our audio isolation model. Only applies to Voice Changer.

        file_format : typing.Optional[SpeechToSpeechRequestFileFormat]
            The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform.

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

        optimize_streaming_latency : typing.Optional[int]
            You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model. Possible values:
            0 - default mode (no latency optimizations)
            1 - normal latency optimizations (about 50% of possible latency improvement of option 3)
            2 - strong latency optimizations (about 75% of possible latency improvement of option 3)
            3 - max latency optimizations
            4 - max latency optimizations, but also with text normalizer turned off for even more latency savings (best latency, but can mispronounce eg numbers and dates).

            Defaults to None.

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio6]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM and WAV formats with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            The generated audio file

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import OutputFormatOfTheGeneratedAudio6

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.speech_to_speech.convert(
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            enable_logging=True,
            output_format="mp3_44100_128",
            audio="audio",
            model_id="eleven_multilingual_sts_v2",
        )
        for chunk in response:
            print(chunk)
        """

        Validator(str).validate(voice_id, "voice_id")
        Validator(bool).is_optional().is_nullable().validate(
            enable_logging, "enable_logging"
        )
        Validator(int).is_optional().is_nullable().validate(
            optimize_streaming_latency, "optimize_streaming_latency"
        )
        Validator(
            OutputFormatOfTheGeneratedAudio6
        ).is_optional().is_nullable().validate(output_format, "output_format")

        resolved_config = self._get_resolved_config(
            self._convert_config, request_options
        )

        request_body = SpeechToSpeechRequest(
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "voice_settings": voice_settings,
                        "seed": seed,
                        "remove_background_noise": remove_background_noise,
                        "file_format": file_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(SpeechToSpeechRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/speech-to-speech/{{voice_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .add_query("enable_logging", enable_logging, nullable=True)
            .add_query(
                "optimize_streaming_latency", optimize_streaming_latency, nullable=True
            )
            .add_query("output_format", output_format, nullable=True)
            .serialize()
            .set_method("POST")
            .set_binary_download()
            .set_body(request_body, "multipart/form-data")
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response

    @cast_models
    def stream(
        self,
        voice_id: str,
        *,
        audio: bytes,
        model_id: Optional[str] = SENTINEL,
        voice_settings: Union[str, None] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        remove_background_noise: Optional[bool] = SENTINEL,
        file_format: Union[SpeechToSpeechStreamRequestFileFormat, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio7, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Stream audio from one voice to another. Maintain full control over emotion, timing and delivery.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. Use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        audio : core.File
            The audio file which holds the content and emotion that will control the generated speech.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for speech to speech, you can check this using the can_do_voice_conversion property.

        voice_settings : typing.Optional[str]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request. Needs to be send as a JSON encoded string.

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        remove_background_noise : typing.Optional[bool]
            If set, will remove the background noise from your audio input using our audio isolation model. Only applies to Voice Changer.

        file_format : typing.Optional[SpeechToSpeechStreamRequestFileFormat]
            The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform.

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

        optimize_streaming_latency : typing.Optional[int]
            You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model. Possible values:
            0 - default mode (no latency optimizations)
            1 - normal latency optimizations (about 50% of possible latency improvement of option 3)
            2 - strong latency optimizations (about 75% of possible latency improvement of option 3)
            3 - max latency optimizations
            4 - max latency optimizations, but also with text normalizer turned off for even more latency savings (best latency, but can mispronounce eg numbers and dates).

            Defaults to None.

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio7]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            Streaming audio data

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import OutputFormatOfTheGeneratedAudio7

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.speech_to_speech.stream(
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            enable_logging=True,
            output_format="mp3_44100_128",
            audio="audio",
            model_id="eleven_multilingual_sts_v2",
        )
        for chunk in response:
            print(chunk)
        """

        Validator(str).validate(voice_id, "voice_id")
        Validator(bool).is_optional().is_nullable().validate(
            enable_logging, "enable_logging"
        )
        Validator(int).is_optional().is_nullable().validate(
            optimize_streaming_latency, "optimize_streaming_latency"
        )
        Validator(
            OutputFormatOfTheGeneratedAudio7
        ).is_optional().is_nullable().validate(output_format, "output_format")

        resolved_config = self._get_resolved_config(
            self._stream_config, request_options
        )

        request_body = SpeechToSpeechStreamRequest(
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "voice_settings": voice_settings,
                        "seed": seed,
                        "remove_background_noise": remove_background_noise,
                        "file_format": file_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(SpeechToSpeechStreamRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/speech-to-speech/{{voice_id}}/stream",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .add_query("enable_logging", enable_logging, nullable=True)
            .add_query(
                "optimize_streaming_latency", optimize_streaming_latency, nullable=True
            )
            .add_query("output_format", output_format, nullable=True)
            .serialize()
            .set_method("POST")
            .set_binary_download()
            .set_body(request_body, "multipart/form-data")
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response


class RawSpeechToSpeechClient:
    """
    Raw-response client for SpeechToSpeechClient.

    Each method delegates to the matching :class:`SpeechToSpeechClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: SpeechToSpeechClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def convert(
        self,
        voice_id: str,
        *,
        audio: bytes,
        model_id: Optional[str] = SENTINEL,
        voice_settings: Union[str, None] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        remove_background_noise: Optional[bool] = SENTINEL,
        file_format: Union[SpeechToSpeechRequestFileFormat, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio6, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = SpeechToSpeechClient.convert(
            _call_client,
            voice_id,
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "voice_settings": voice_settings,
                        "seed": seed,
                        "remove_background_noise": remove_background_noise,
                        "file_format": file_format,
                        "enable_logging": enable_logging,
                        "optimize_streaming_latency": optimize_streaming_latency,
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

    def stream(
        self,
        voice_id: str,
        *,
        audio: bytes,
        model_id: Optional[str] = SENTINEL,
        voice_settings: Union[str, None] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        remove_background_noise: Optional[bool] = SENTINEL,
        file_format: Union[SpeechToSpeechStreamRequestFileFormat, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio7, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = SpeechToSpeechClient.stream(
            _call_client,
            voice_id,
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "voice_settings": voice_settings,
                        "seed": seed,
                        "remove_background_noise": remove_background_noise,
                        "file_format": file_format,
                        "enable_logging": enable_logging,
                        "optimize_streaming_latency": optimize_streaming_latency,
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


class AsyncSpeechToSpeechClient(SpeechToSpeechClient):
    """
    Async wrapper for SpeechToSpeechClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawSpeechToSpeechClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawSpeechToSpeechClient(self)

    def convert(
        self,
        voice_id: str,
        *,
        audio: bytes,
        model_id: Optional[str] = SENTINEL,
        voice_settings: Union[str, None] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        remove_background_noise: Optional[bool] = SENTINEL,
        file_format: Union[SpeechToSpeechRequestFileFormat, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio6, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Transform audio from one voice to another. Maintain full control over emotion, timing and delivery.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. Use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        audio : core.File
            The audio file which holds the content and emotion that will control the generated speech.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for speech to speech, you can check this using the can_do_voice_conversion property.

        voice_settings : typing.Optional[str]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request. Needs to be send as a JSON encoded string.

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        remove_background_noise : typing.Optional[bool]
            If set, will remove the background noise from your audio input using our audio isolation model. Only applies to Voice Changer.

        file_format : typing.Optional[SpeechToSpeechRequestFileFormat]
            The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform.

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

        optimize_streaming_latency : typing.Optional[int]
            You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model. Possible values:
            0 - default mode (no latency optimizations)
            1 - normal latency optimizations (about 50% of possible latency improvement of option 3)
            2 - strong latency optimizations (about 75% of possible latency improvement of option 3)
            3 - max latency optimizations
            4 - max latency optimizations, but also with text normalizer turned off for even more latency savings (best latency, but can mispronounce eg numbers and dates).

            Defaults to None.

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio6]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM and WAV formats with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The generated audio file

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import OutputFormatOfTheGeneratedAudio6

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.speech_to_speech.convert(
                voice_id="JBFqnCBsd6RMkjVDRZzb",
                enable_logging=True,
                output_format="mp3_44100_128",
                audio="audio",
                model_id="eleven_multilingual_sts_v2",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().convert(
            voice_id,
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "voice_settings": voice_settings,
                        "seed": seed,
                        "remove_background_noise": remove_background_noise,
                        "file_format": file_format,
                        "enable_logging": enable_logging,
                        "optimize_streaming_latency": optimize_streaming_latency,
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

    def stream(
        self,
        voice_id: str,
        *,
        audio: bytes,
        model_id: Optional[str] = SENTINEL,
        voice_settings: Union[str, None] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        remove_background_noise: Optional[bool] = SENTINEL,
        file_format: Union[SpeechToSpeechStreamRequestFileFormat, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio7, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Stream audio from one voice to another. Maintain full control over emotion, timing and delivery.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. Use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        audio : core.File
            The audio file which holds the content and emotion that will control the generated speech.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for speech to speech, you can check this using the can_do_voice_conversion property.

        voice_settings : typing.Optional[str]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request. Needs to be send as a JSON encoded string.

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        remove_background_noise : typing.Optional[bool]
            If set, will remove the background noise from your audio input using our audio isolation model. Only applies to Voice Changer.

        file_format : typing.Optional[SpeechToSpeechStreamRequestFileFormat]
            The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform.

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

        optimize_streaming_latency : typing.Optional[int]
            You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model. Possible values:
            0 - default mode (no latency optimizations)
            1 - normal latency optimizations (about 50% of possible latency improvement of option 3)
            2 - strong latency optimizations (about 75% of possible latency improvement of option 3)
            3 - max latency optimizations
            4 - max latency optimizations, but also with text normalizer turned off for even more latency savings (best latency, but can mispronounce eg numbers and dates).

            Defaults to None.

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio7]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

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
        from fern.types import OutputFormatOfTheGeneratedAudio7

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.speech_to_speech.stream(
                voice_id="JBFqnCBsd6RMkjVDRZzb",
                enable_logging=True,
                output_format="mp3_44100_128",
                audio="audio",
                model_id="eleven_multilingual_sts_v2",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().stream(
            voice_id,
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "voice_settings": voice_settings,
                        "seed": seed,
                        "remove_background_noise": remove_background_noise,
                        "file_format": file_format,
                        "enable_logging": enable_logging,
                        "optimize_streaming_latency": optimize_streaming_latency,
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


class AsyncRawSpeechToSpeechClient:
    """
    Async raw-response client for AsyncSpeechToSpeechClient.
    """

    def __init__(self, client: AsyncSpeechToSpeechClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def convert(
        self,
        voice_id: str,
        *,
        audio: bytes,
        model_id: Optional[str] = SENTINEL,
        voice_settings: Union[str, None] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        remove_background_noise: Optional[bool] = SENTINEL,
        file_format: Union[SpeechToSpeechRequestFileFormat, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio6, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncSpeechToSpeechClient.convert(
            _call_client,
            voice_id,
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "voice_settings": voice_settings,
                        "seed": seed,
                        "remove_background_noise": remove_background_noise,
                        "file_format": file_format,
                        "enable_logging": enable_logging,
                        "optimize_streaming_latency": optimize_streaming_latency,
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

    def stream(
        self,
        voice_id: str,
        *,
        audio: bytes,
        model_id: Optional[str] = SENTINEL,
        voice_settings: Union[str, None] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        remove_background_noise: Optional[bool] = SENTINEL,
        file_format: Union[SpeechToSpeechStreamRequestFileFormat, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio7, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncSpeechToSpeechClient.stream(
            _call_client,
            voice_id,
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "voice_settings": voice_settings,
                        "seed": seed,
                        "remove_background_noise": remove_background_noise,
                        "file_format": file_format,
                        "enable_logging": enable_logging,
                        "optimize_streaming_latency": optimize_streaming_latency,
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
