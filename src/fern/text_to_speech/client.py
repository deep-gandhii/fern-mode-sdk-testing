from typing import Any, Optional, Generator, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    AudioWithTimestampsResponse,
    BodyTextToSpeechFull,
    BodyTextToSpeechFullApplyTextNormalization,
    BodyTextToSpeechFullWithTimestamps,
    BodyTextToSpeechFullWithTimestampsApplyTextNormalization,
    BodyTextToSpeechStream,
    BodyTextToSpeechStreamApplyTextNormalization,
    BodyTextToSpeechStreamWithTimestamps,
    BodyTextToSpeechStreamWithTimestampsApplyTextNormalization,
    HttpValidationError,
    OutputFormatOfTheGeneratedAudio1,
    OutputFormatOfTheGeneratedAudio2,
    OutputFormatOfTheGeneratedAudio3,
    PronunciationDictionaryVersionLocator,
    StreamingAudioChunkWithTimestampsResponse,
    StreamWithTimestampsOutputFormat,
    VoiceSettings,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable, AsyncGenerator
import asyncio
import threading


class TextToSpeechClient(BaseService):
    """
    Fern-style resource client for TextToSpeechClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._convert_config: SdkConfig = {}
        self._convert_with_timestamps_config: SdkConfig = {}
        self._stream_config: SdkConfig = {}
        self._stream_with_timestamps_config: SdkConfig = {}

    def set_convert_config(self, config: SdkConfig):
        """
        Sets method-level configuration for convert.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._convert_config = config
        return self

    def set_convert_with_timestamps_config(self, config: SdkConfig):
        """
        Sets method-level configuration for convert_with_timestamps.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._convert_with_timestamps_config = config
        return self

    def set_stream_config(self, config: SdkConfig):
        """
        Sets method-level configuration for stream.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._stream_config = config
        return self

    def set_stream_with_timestamps_config(self, config: SdkConfig):
        """
        Sets method-level configuration for stream_with_timestamps.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._stream_with_timestamps_config = config
        return self

    @property
    def with_raw_response(self) -> "RawTextToSpeechClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawTextToSpeechClient(self)

    @cast_models
    def convert(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Union[VoiceSettings, None] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Union[List[str], None] = SENTINEL,
        next_request_ids: Union[List[str], None] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechFullApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio1, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Converts text into speech using a voice of your choice and returns audio.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. Use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        text : str
            The text that will get converted into speech.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        voice_settings : typing.Optional[VoiceSettings]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        previous_text : typing.Optional[str]
            The text that came before the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        next_text : typing.Optional[str]
            The text that comes after the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        previous_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that were generated before this generation. Can be used to improve the speech's continuity when splitting up a large task into multiple requests. The results will be best when the same model is used across the generations. In case both previous_text and previous_request_ids is send, previous_text will be ignored. A maximum of 3 request_ids can be send.

        next_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that come after this generation. next_request_ids is especially useful for maintaining the speech's continuity when regenerating a sample that has had some audio quality issues. For example, if you have generated 3 speech clips, and you want to improve clip 2, passing the request id of clip 3 as a next_request_id (and that of clip 1 as a previous_request_id) will help maintain natural flow in the combined speech. The results will be best when the same model is used across the generations. In case both next_text and next_request_ids is send, next_text will be ignored. A maximum of 3 request_ids can be send.

        use_pvc_as_ivc : typing.Optional[bool]
            If true, we won't use PVC version of the voice for the generation but the IVC version. This is a temporary workaround for higher latency in PVC versions.

        apply_text_normalization : typing.Optional[BodyTextToSpeechFullApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        apply_language_text_normalization : typing.Optional[bool]
            This parameter controls language text normalization. This helps with proper pronunciation of text in some supported languages. WARNING: This parameter can heavily increase the latency of the request. Currently only supported for Japanese.

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

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio1]
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
        from fern.types import OutputFormatOfTheGeneratedAudio1

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.text_to_speech.convert(
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            enable_logging=True,
            output_format="mp3_44100_128",
            text="The first move is what sets everything in motion.",
            model_id="eleven_multilingual_v2",
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
            OutputFormatOfTheGeneratedAudio1
        ).is_optional().is_nullable().validate(output_format, "output_format")

        resolved_config = self._get_resolved_config(
            self._convert_config, request_options
        )

        request_body = BodyTextToSpeechFull(
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyTextToSpeechFull).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/text-to-speech/{{voice_id}}",
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
            .set_body(request_body)
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response

    @cast_models
    def convert_with_timestamps(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        pronunciation_dictionary_locators: Optional[
            List[PronunciationDictionaryVersionLocator]
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Optional[List[str]] = SENTINEL,
        next_request_ids: Optional[List[str]] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechFullWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio2, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AudioWithTimestampsResponse:
        """
        Generate speech from text with precise character-level timing information for audio-text synchronization.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        text : str
            The text that will get converted into speech.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        voice_settings : typing.Optional[VoiceSettings]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        previous_text : typing.Optional[str]
            The text that came before the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        next_text : typing.Optional[str]
            The text that comes after the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        previous_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that were generated before this generation. Can be used to improve the speech's continuity when splitting up a large task into multiple requests. The results will be best when the same model is used across the generations. In case both previous_text and previous_request_ids is send, previous_text will be ignored. A maximum of 3 request_ids can be send.

        next_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that come after this generation. next_request_ids is especially useful for maintaining the speech's continuity when regenerating a sample that has had some audio quality issues. For example, if you have generated 3 speech clips, and you want to improve clip 2, passing the request id of clip 3 as a next_request_id (and that of clip 1 as a previous_request_id) will help maintain natural flow in the combined speech. The results will be best when the same model is used across the generations. In case both next_text and next_request_ids is send, next_text will be ignored. A maximum of 3 request_ids can be send.

        use_pvc_as_ivc : typing.Optional[bool]
            If true, we won't use PVC version of the voice for the generation but the IVC version. This is a temporary workaround for higher latency in PVC versions.

        apply_text_normalization : typing.Optional[BodyTextToSpeechFullWithTimestampsApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        apply_language_text_normalization : typing.Optional[bool]
            This parameter controls language text normalization. This helps with proper pronunciation of text in some supported languages. WARNING: This parameter can heavily increase the latency of the request. Currently only supported for Japanese.

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

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio2]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM and WAV formats with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudioWithTimestampsResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import OutputFormatOfTheGeneratedAudio2

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.text_to_speech.convert_with_timestamps(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            enable_logging=True,
            output_format="alaw_8000",
            text="This is a test for the API of ElevenLabs.",
            model_id="eleven_multilingual_v2",
            language_code="language_code",
            voice_settings={
                "stability": 0.62,
                "use_speaker_boost": True,
                "similarity_boost": 0.18,
                "style": 2.67,
                "speed": 5.4
            },
            pronunciation_dictionary_locators=[
                {
                    "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                    "version_id": "version_id"
                }
            ],
            seed=4,
            previous_text="previous_text",
            next_text="next_text",
            previous_request_ids=[
                "previous_request_ids"
            ],
            next_request_ids=[
                "next_request_ids"
            ],
            apply_text_normalization="auto",
            apply_language_text_normalization=True,
        )
        """

        Validator(str).validate(voice_id, "voice_id")
        Validator(bool).is_optional().is_nullable().validate(
            enable_logging, "enable_logging"
        )
        Validator(int).is_optional().is_nullable().validate(
            optimize_streaming_latency, "optimize_streaming_latency"
        )
        Validator(
            OutputFormatOfTheGeneratedAudio2
        ).is_optional().is_nullable().validate(output_format, "output_format")

        resolved_config = self._get_resolved_config(
            self._convert_with_timestamps_config, request_options
        )

        request_body = BodyTextToSpeechFullWithTimestamps(
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyTextToSpeechFullWithTimestamps).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/text-to-speech/{{voice_id}}/with-timestamps",
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
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AudioWithTimestampsResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AudioWithTimestampsResponse, response)
            )
        )

    @cast_models
    def stream(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Union[List[str], None] = SENTINEL,
        next_request_ids: Union[List[str], None] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechStreamApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio3, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Converts text into speech using a voice of your choice and returns audio as an audio stream.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. Use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        text : str
            The text that will get converted into speech.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        voice_settings : typing.Optional[VoiceSettings]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        previous_text : typing.Optional[str]
            The text that came before the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        next_text : typing.Optional[str]
            The text that comes after the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        previous_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that were generated before this generation. Can be used to improve the speech's continuity when splitting up a large task into multiple requests. The results will be best when the same model is used across the generations. In case both previous_text and previous_request_ids is send, previous_text will be ignored. A maximum of 3 request_ids can be send.

        next_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that come after this generation. next_request_ids is especially useful for maintaining the speech's continuity when regenerating a sample that has had some audio quality issues. For example, if you have generated 3 speech clips, and you want to improve clip 2, passing the request id of clip 3 as a next_request_id (and that of clip 1 as a previous_request_id) will help maintain natural flow in the combined speech. The results will be best when the same model is used across the generations. In case both next_text and next_request_ids is send, next_text will be ignored. A maximum of 3 request_ids can be send.

        use_pvc_as_ivc : typing.Optional[bool]
            If true, we won't use PVC version of the voice for the generation but the IVC version. This is a temporary workaround for higher latency in PVC versions.

        apply_text_normalization : typing.Optional[BodyTextToSpeechStreamApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        apply_language_text_normalization : typing.Optional[bool]
            This parameter controls language text normalization. This helps with proper pronunciation of text in some supported languages. WARNING: This parameter can heavily increase the latency of the request. Currently only supported for Japanese.

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

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio3]
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
        from fern.types import OutputFormatOfTheGeneratedAudio3

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.text_to_speech.stream(
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            enable_logging=True,
            output_format="mp3_44100_128",
            text="The first move is what sets everything in motion.",
            model_id="eleven_multilingual_v2",
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
            OutputFormatOfTheGeneratedAudio3
        ).is_optional().is_nullable().validate(output_format, "output_format")

        resolved_config = self._get_resolved_config(
            self._stream_config, request_options
        )

        request_body = BodyTextToSpeechStream(
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyTextToSpeechStream).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/text-to-speech/{{voice_id}}/stream",
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
            .set_body(request_body)
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response

    @cast_models
    def stream_with_timestamps(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Union[List[str], None] = SENTINEL,
        next_request_ids: Union[List[str], None] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechStreamWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[StreamWithTimestampsOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[StreamingAudioChunkWithTimestampsResponse, None, None]:
        """
        Converts text into speech using a voice of your choice and returns a stream of JSONs containing audio as a base64 encoded string together with information on when which character was spoken.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. Use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        text : str
            The text that will get converted into speech.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        voice_settings : typing.Optional[VoiceSettings]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        previous_text : typing.Optional[str]
            The text that came before the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        next_text : typing.Optional[str]
            The text that comes after the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        previous_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that were generated before this generation. Can be used to improve the speech's continuity when splitting up a large task into multiple requests. The results will be best when the same model is used across the generations. In case both previous_text and previous_request_ids is send, previous_text will be ignored. A maximum of 3 request_ids can be send.

        next_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that come after this generation. next_request_ids is especially useful for maintaining the speech's continuity when regenerating a sample that has had some audio quality issues. For example, if you have generated 3 speech clips, and you want to improve clip 2, passing the request id of clip 3 as a next_request_id (and that of clip 1 as a previous_request_id) will help maintain natural flow in the combined speech. The results will be best when the same model is used across the generations. In case both next_text and next_request_ids is send, next_text will be ignored. A maximum of 3 request_ids can be send.

        use_pvc_as_ivc : typing.Optional[bool]
            If true, we won't use PVC version of the voice for the generation but the IVC version. This is a temporary workaround for higher latency in PVC versions.

        apply_text_normalization : typing.Optional[BodyTextToSpeechStreamWithTimestampsApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        apply_language_text_normalization : typing.Optional[bool]
            This parameter controls language text normalization. This helps with proper pronunciation of text in some supported languages. WARNING: This parameter can heavily increase the latency of the request. Currently only supported for Japanese.

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

        output_format : typing.Optional[StreamWithTimestampsOutputFormat]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[StreamingAudioChunkWithTimestampsResponse]
            Stream of transcription chunks

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import StreamWithTimestampsOutputFormat

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.text_to_speech.stream_with_timestamps(
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            enable_logging=True,
            output_format="mp3_44100_128",
            text="The first move is what sets everything in motion.",
            model_id="eleven_multilingual_v2",
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
            StreamWithTimestampsOutputFormat
        ).is_optional().is_nullable().validate(output_format, "output_format")

        resolved_config = self._get_resolved_config(
            self._stream_with_timestamps_config, request_options
        )

        request_body = BodyTextToSpeechStreamWithTimestamps(
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyTextToSpeechStreamWithTimestamps).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/text-to-speech/{{voice_id}}/stream/with-timestamps",
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
            .set_body(request_body)
        )

        for response, status, _ in self.stream_request(serialized_request):
            yield (
                StreamingAudioChunkWithTimestampsResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    StreamingAudioChunkWithTimestampsResponse, response
                )
            )


class RawTextToSpeechClient:
    """
    Raw-response client for TextToSpeechClient.

    Each method delegates to the matching :class:`TextToSpeechClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: TextToSpeechClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def convert(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Union[VoiceSettings, None] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Union[List[str], None] = SENTINEL,
        next_request_ids: Union[List[str], None] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechFullApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio1, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = TextToSpeechClient.convert(
            _call_client,
            voice_id,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
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

    def convert_with_timestamps(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        pronunciation_dictionary_locators: Optional[
            List[PronunciationDictionaryVersionLocator]
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Optional[List[str]] = SENTINEL,
        next_request_ids: Optional[List[str]] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechFullWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio2, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AudioWithTimestampsResponse]:
        data = TextToSpeechClient.convert_with_timestamps(
            self._client,
            voice_id,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
                        "enable_logging": enable_logging,
                        "optimize_streaming_latency": optimize_streaming_latency,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def stream(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Union[List[str], None] = SENTINEL,
        next_request_ids: Union[List[str], None] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechStreamApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio3, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = TextToSpeechClient.stream(
            _call_client,
            voice_id,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
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

    def stream_with_timestamps(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Union[List[str], None] = SENTINEL,
        next_request_ids: Union[List[str], None] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechStreamWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[StreamWithTimestampsOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[StreamingAudioChunkWithTimestampsResponse, None, None]]:
        _call_client = self._client._for_one_call()
        data = TextToSpeechClient.stream_with_timestamps(
            _call_client,
            voice_id,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
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


class AsyncTextToSpeechClient(TextToSpeechClient):
    """
    Async wrapper for TextToSpeechClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawTextToSpeechClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawTextToSpeechClient(self)

    def convert(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Union[VoiceSettings, None] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Union[List[str], None] = SENTINEL,
        next_request_ids: Union[List[str], None] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechFullApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio1, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Converts text into speech using a voice of your choice and returns audio.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. Use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        text : str
            The text that will get converted into speech.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        voice_settings : typing.Optional[VoiceSettings]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        previous_text : typing.Optional[str]
            The text that came before the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        next_text : typing.Optional[str]
            The text that comes after the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        previous_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that were generated before this generation. Can be used to improve the speech's continuity when splitting up a large task into multiple requests. The results will be best when the same model is used across the generations. In case both previous_text and previous_request_ids is send, previous_text will be ignored. A maximum of 3 request_ids can be send.

        next_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that come after this generation. next_request_ids is especially useful for maintaining the speech's continuity when regenerating a sample that has had some audio quality issues. For example, if you have generated 3 speech clips, and you want to improve clip 2, passing the request id of clip 3 as a next_request_id (and that of clip 1 as a previous_request_id) will help maintain natural flow in the combined speech. The results will be best when the same model is used across the generations. In case both next_text and next_request_ids is send, next_text will be ignored. A maximum of 3 request_ids can be send.

        use_pvc_as_ivc : typing.Optional[bool]
            If true, we won't use PVC version of the voice for the generation but the IVC version. This is a temporary workaround for higher latency in PVC versions.

        apply_text_normalization : typing.Optional[BodyTextToSpeechFullApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        apply_language_text_normalization : typing.Optional[bool]
            This parameter controls language text normalization. This helps with proper pronunciation of text in some supported languages. WARNING: This parameter can heavily increase the latency of the request. Currently only supported for Japanese.

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

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio1]
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
        from fern.types import OutputFormatOfTheGeneratedAudio1

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.text_to_speech.convert(
                voice_id="JBFqnCBsd6RMkjVDRZzb",
                enable_logging=True,
                output_format="mp3_44100_128",
                text="The first move is what sets everything in motion.",
                model_id="eleven_multilingual_v2",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().convert(
            voice_id,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
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

    def convert_with_timestamps(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        pronunciation_dictionary_locators: Optional[
            List[PronunciationDictionaryVersionLocator]
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Optional[List[str]] = SENTINEL,
        next_request_ids: Optional[List[str]] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechFullWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio2, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AudioWithTimestampsResponse]:  # type: ignore[override]
        """
        Generate speech from text with precise character-level timing information for audio-text synchronization.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        text : str
            The text that will get converted into speech.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        voice_settings : typing.Optional[VoiceSettings]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        previous_text : typing.Optional[str]
            The text that came before the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        next_text : typing.Optional[str]
            The text that comes after the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        previous_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that were generated before this generation. Can be used to improve the speech's continuity when splitting up a large task into multiple requests. The results will be best when the same model is used across the generations. In case both previous_text and previous_request_ids is send, previous_text will be ignored. A maximum of 3 request_ids can be send.

        next_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that come after this generation. next_request_ids is especially useful for maintaining the speech's continuity when regenerating a sample that has had some audio quality issues. For example, if you have generated 3 speech clips, and you want to improve clip 2, passing the request id of clip 3 as a next_request_id (and that of clip 1 as a previous_request_id) will help maintain natural flow in the combined speech. The results will be best when the same model is used across the generations. In case both next_text and next_request_ids is send, next_text will be ignored. A maximum of 3 request_ids can be send.

        use_pvc_as_ivc : typing.Optional[bool]
            If true, we won't use PVC version of the voice for the generation but the IVC version. This is a temporary workaround for higher latency in PVC versions.

        apply_text_normalization : typing.Optional[BodyTextToSpeechFullWithTimestampsApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        apply_language_text_normalization : typing.Optional[bool]
            This parameter controls language text normalization. This helps with proper pronunciation of text in some supported languages. WARNING: This parameter can heavily increase the latency of the request. Currently only supported for Japanese.

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

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio2]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM and WAV formats with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudioWithTimestampsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import OutputFormatOfTheGeneratedAudio2

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.text_to_speech.convert_with_timestamps(
                voice_id="21m00Tcm4TlvDq8ikWAM",
                enable_logging=True,
                output_format="alaw_8000",
                text="This is a test for the API of ElevenLabs.",
                model_id="eleven_multilingual_v2",
                language_code="language_code",
                voice_settings={
                    "stability": 0.62,
                    "use_speaker_boost": True,
                    "similarity_boost": 0.18,
                    "style": 2.67,
                    "speed": 5.4
                },
                pronunciation_dictionary_locators=[
                    {
                        "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                        "version_id": "version_id"
                    }
                ],
                seed=4,
                previous_text="previous_text",
                next_text="next_text",
                previous_request_ids=[
                    "previous_request_ids"
                ],
                next_request_ids=[
                    "next_request_ids"
                ],
                apply_text_normalization="auto",
                apply_language_text_normalization=True,
            )


        asyncio.run(main())
        """
        return to_async(super().convert_with_timestamps)(
            voice_id,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
                        "enable_logging": enable_logging,
                        "optimize_streaming_latency": optimize_streaming_latency,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def stream(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Union[List[str], None] = SENTINEL,
        next_request_ids: Union[List[str], None] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechStreamApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio3, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Converts text into speech using a voice of your choice and returns audio as an audio stream.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. Use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        text : str
            The text that will get converted into speech.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        voice_settings : typing.Optional[VoiceSettings]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        previous_text : typing.Optional[str]
            The text that came before the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        next_text : typing.Optional[str]
            The text that comes after the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        previous_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that were generated before this generation. Can be used to improve the speech's continuity when splitting up a large task into multiple requests. The results will be best when the same model is used across the generations. In case both previous_text and previous_request_ids is send, previous_text will be ignored. A maximum of 3 request_ids can be send.

        next_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that come after this generation. next_request_ids is especially useful for maintaining the speech's continuity when regenerating a sample that has had some audio quality issues. For example, if you have generated 3 speech clips, and you want to improve clip 2, passing the request id of clip 3 as a next_request_id (and that of clip 1 as a previous_request_id) will help maintain natural flow in the combined speech. The results will be best when the same model is used across the generations. In case both next_text and next_request_ids is send, next_text will be ignored. A maximum of 3 request_ids can be send.

        use_pvc_as_ivc : typing.Optional[bool]
            If true, we won't use PVC version of the voice for the generation but the IVC version. This is a temporary workaround for higher latency in PVC versions.

        apply_text_normalization : typing.Optional[BodyTextToSpeechStreamApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        apply_language_text_normalization : typing.Optional[bool]
            This parameter controls language text normalization. This helps with proper pronunciation of text in some supported languages. WARNING: This parameter can heavily increase the latency of the request. Currently only supported for Japanese.

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

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio3]
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
        from fern.types import OutputFormatOfTheGeneratedAudio3

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.text_to_speech.stream(
                voice_id="JBFqnCBsd6RMkjVDRZzb",
                enable_logging=True,
                output_format="mp3_44100_128",
                text="The first move is what sets everything in motion.",
                model_id="eleven_multilingual_v2",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().stream(
            voice_id,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
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

    def stream_with_timestamps(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Union[List[str], None] = SENTINEL,
        next_request_ids: Union[List[str], None] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechStreamWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[StreamWithTimestampsOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[StreamingAudioChunkWithTimestampsResponse, None]:  # type: ignore[override]
        """
        Converts text into speech using a voice of your choice and returns a stream of JSONs containing audio as a base64 encoded string together with information on when which character was spoken.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. Use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        text : str
            The text that will get converted into speech.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        voice_settings : typing.Optional[VoiceSettings]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        previous_text : typing.Optional[str]
            The text that came before the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        next_text : typing.Optional[str]
            The text that comes after the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.

        previous_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that were generated before this generation. Can be used to improve the speech's continuity when splitting up a large task into multiple requests. The results will be best when the same model is used across the generations. In case both previous_text and previous_request_ids is send, previous_text will be ignored. A maximum of 3 request_ids can be send.

        next_request_ids : typing.Optional[typing.Sequence[str]]
            A list of request_id of the samples that come after this generation. next_request_ids is especially useful for maintaining the speech's continuity when regenerating a sample that has had some audio quality issues. For example, if you have generated 3 speech clips, and you want to improve clip 2, passing the request id of clip 3 as a next_request_id (and that of clip 1 as a previous_request_id) will help maintain natural flow in the combined speech. The results will be best when the same model is used across the generations. In case both next_text and next_request_ids is send, next_text will be ignored. A maximum of 3 request_ids can be send.

        use_pvc_as_ivc : typing.Optional[bool]
            If true, we won't use PVC version of the voice for the generation but the IVC version. This is a temporary workaround for higher latency in PVC versions.

        apply_text_normalization : typing.Optional[BodyTextToSpeechStreamWithTimestampsApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        apply_language_text_normalization : typing.Optional[bool]
            This parameter controls language text normalization. This helps with proper pronunciation of text in some supported languages. WARNING: This parameter can heavily increase the latency of the request. Currently only supported for Japanese.

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

        output_format : typing.Optional[StreamWithTimestampsOutputFormat]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[StreamingAudioChunkWithTimestampsResponse]
            Stream of transcription chunks

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import StreamWithTimestampsOutputFormat

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.text_to_speech.stream_with_timestamps(
                voice_id="JBFqnCBsd6RMkjVDRZzb",
                enable_logging=True,
                output_format="mp3_44100_128",
                text="The first move is what sets everything in motion.",
                model_id="eleven_multilingual_v2",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().stream_with_timestamps(
            voice_id,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
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


class AsyncRawTextToSpeechClient:
    """
    Async raw-response client for AsyncTextToSpeechClient.
    """

    def __init__(self, client: AsyncTextToSpeechClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def convert(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Union[VoiceSettings, None] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Union[List[str], None] = SENTINEL,
        next_request_ids: Union[List[str], None] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechFullApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio1, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncTextToSpeechClient.convert(
            _call_client,
            voice_id,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
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

    async def convert_with_timestamps(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        pronunciation_dictionary_locators: Optional[
            List[PronunciationDictionaryVersionLocator]
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Optional[List[str]] = SENTINEL,
        next_request_ids: Optional[List[str]] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechFullWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio2, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AudioWithTimestampsResponse]:
        data = await AsyncTextToSpeechClient.convert_with_timestamps(
            self._client,
            voice_id,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
                        "enable_logging": enable_logging,
                        "optimize_streaming_latency": optimize_streaming_latency,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def stream(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Union[List[str], None] = SENTINEL,
        next_request_ids: Union[List[str], None] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechStreamApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio3, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncTextToSpeechClient.stream(
            _call_client,
            voice_id,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
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

    def stream_with_timestamps(
        self,
        voice_id: str,
        *,
        text: str,
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        previous_text: Union[str, None] = SENTINEL,
        next_text: Union[str, None] = SENTINEL,
        previous_request_ids: Union[List[str], None] = SENTINEL,
        next_request_ids: Union[List[str], None] = SENTINEL,
        use_pvc_as_ivc: Optional[bool] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToSpeechStreamWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        apply_language_text_normalization: Optional[bool] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        optimize_streaming_latency: Union[int, None] = SENTINEL,
        output_format: Union[StreamWithTimestampsOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[StreamingAudioChunkWithTimestampsResponse, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncTextToSpeechClient.stream_with_timestamps(
            _call_client,
            voice_id,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "voice_settings": voice_settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "previous_text": previous_text,
                        "next_text": next_text,
                        "previous_request_ids": previous_request_ids,
                        "next_request_ids": next_request_ids,
                        "use_pvc_as_ivc": use_pvc_as_ivc,
                        "apply_text_normalization": apply_text_normalization,
                        "apply_language_text_normalization": apply_language_text_normalization,
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
