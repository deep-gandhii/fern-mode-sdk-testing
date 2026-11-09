from typing import Any, Optional, Generator, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    AllowedOutputFormats,
    AudioWithTimestampsAndVoiceSegmentsResponseModel,
    BodyTextToDialogueFullWithTimestamps,
    BodyTextToDialogueFullWithTimestampsApplyTextNormalization,
    BodyTextToDialogueMultiVoiceStreamingV1TextToDialogueStreamPost,
    BodyTextToDialogueMultiVoiceStreamingV1TextToDialogueStreamPostApplyTextNormalization,
    BodyTextToDialogueMultiVoiceV1TextToDialoguePost,
    BodyTextToDialogueMultiVoiceV1TextToDialoguePostApplyTextNormalization,
    BodyTextToDialogueStreamWithTimestamps,
    BodyTextToDialogueStreamWithTimestampsApplyTextNormalization,
    DialogueInput,
    HttpValidationError,
    ModelSettingsResponseModel,
    OutputFormatOfTheGeneratedAudio4,
    OutputFormatOfTheGeneratedAudio5,
    PronunciationDictionaryVersionLocator,
    StreamingAudioChunkWithTimestampsAndVoiceSegmentsResponseModel,
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


class TextToDialogueClient(BaseService):
    """
    Fern-style resource client for TextToDialogueClient.
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
        self._stream_with_timestamps_config: SdkConfig = {}
        self._convert_with_timestamps_config: SdkConfig = {}

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

    def set_stream_with_timestamps_config(self, config: SdkConfig):
        """
        Sets method-level configuration for stream_with_timestamps.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._stream_with_timestamps_config = config
        return self

    def set_convert_with_timestamps_config(self, config: SdkConfig):
        """
        Sets method-level configuration for convert_with_timestamps.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._convert_with_timestamps_config = config
        return self

    @property
    def with_raw_response(self) -> "RawTextToDialogueClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawTextToDialogueClient(self)

    @cast_models
    def convert(
        self,
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Union[ModelSettingsResponseModel, None] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueMultiVoiceV1TextToDialoguePostApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio4, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Converts a list of text and voice ID pairs into speech (dialogue) and returns audio.

        Parameters
        ----------
        inputs : typing.Sequence[DialogueInput]
            A list of dialogue inputs, each containing text and a voice ID which will be converted into speech. The maximum number of unique voice IDs is 10. For reliable generation, keep the total character count across all `inputs[].text` values at or below 2,000 characters per request. Longer requests can terminate early in streaming responses or return a validation error.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        settings : typing.Optional[ModelSettingsResponseModel]
            Settings controlling the dialogue generation.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        apply_text_normalization : typing.Optional[BodyTextToDialogueMultiVoiceV1TextToDialoguePostApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio4]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM and WAV formats with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            The generated audio file

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import OutputFormatOfTheGeneratedAudio4

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.text_to_dialogue.convert(
            output_format="alaw_8000",
            enable_logging=True,
            inputs=[
                {
                    "text": "[giggling] Knock knock",
                    "voice_id": "JBFqnCBsd6RMkjVDRZzb"
                },
                {
                    "text": "[curious] Who is there?",
                    "voice_id": "Aw4FAjKCGjjNkVhN1Xmq"
                }
            ],
        )
        for chunk in response:
            print(chunk)
        """

        Validator(
            OutputFormatOfTheGeneratedAudio4
        ).is_optional().is_nullable().validate(output_format, "output_format")
        Validator(bool).is_optional().is_nullable().validate(
            enable_logging, "enable_logging"
        )

        resolved_config = self._get_resolved_config(
            self._convert_config, request_options
        )

        request_body = BodyTextToDialogueMultiVoiceV1TextToDialoguePost(
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyTextToDialogueMultiVoiceV1TextToDialoguePost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/text-to-dialogue",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("output_format", output_format, nullable=True)
            .add_query("enable_logging", enable_logging, nullable=True)
            .serialize()
            .set_method("POST")
            .set_binary_download()
            .set_body(request_body)
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response

    @cast_models
    def stream(
        self,
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Optional[ModelSettingsResponseModel] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueMultiVoiceStreamingV1TextToDialogueStreamPostApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Converts a list of text and voice ID pairs into speech (dialogue) and returns an audio stream.

        Parameters
        ----------
        inputs : typing.Sequence[DialogueInput]
            A list of dialogue inputs, each containing text and a voice ID which will be converted into speech. The maximum number of unique voice IDs is 10. For reliable generation, keep the total character count across all `inputs[].text` values at or below 2,000 characters per request. Longer requests can terminate early in streaming responses or return a validation error.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        settings : typing.Optional[ModelSettingsResponseModel]
            Settings controlling the dialogue generation.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        apply_text_normalization : typing.Optional[BodyTextToDialogueMultiVoiceStreamingV1TextToDialogueStreamPostApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        output_format : typing.Optional[AllowedOutputFormats]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            Streaming audio data

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.text_to_dialogue.stream(
            output_format="mp3_22050_32",
            enable_logging=True,
            inputs=[
                {
                    "text": "[giggling] Knock knock",
                    "voice_id": "JBFqnCBsd6RMkjVDRZzb"
                },
                {
                    "text": "[curious] Who is there?",
                    "voice_id": "Aw4FAjKCGjjNkVhN1Xmq"
                }
            ],
        )
        for chunk in response:
            print(chunk)
        """

        Validator(AllowedOutputFormats).is_optional().is_nullable().validate(
            output_format, "output_format"
        )
        Validator(bool).is_optional().is_nullable().validate(
            enable_logging, "enable_logging"
        )

        resolved_config = self._get_resolved_config(
            self._stream_config, request_options
        )

        request_body = BodyTextToDialogueMultiVoiceStreamingV1TextToDialogueStreamPost(
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(
            BodyTextToDialogueMultiVoiceStreamingV1TextToDialogueStreamPost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/text-to-dialogue/stream",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("output_format", output_format, nullable=True)
            .add_query("enable_logging", enable_logging, nullable=True)
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
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Optional[ModelSettingsResponseModel] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueStreamWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[
        StreamingAudioChunkWithTimestampsAndVoiceSegmentsResponseModel, None, None
    ]:
        """
        Converts a list of text and voice ID pairs into speech (dialogue) and returns a stream of JSON blobs containing audio as a base64 encoded string and timestamps

        Parameters
        ----------
        inputs : typing.Sequence[DialogueInput]
            A list of dialogue inputs, each containing text and a voice ID which will be converted into speech. The maximum number of unique voice IDs is 10. For reliable generation, keep the total character count across all `inputs[].text` values at or below 2,000 characters per request. Longer requests can terminate early in streaming responses or return a validation error.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        settings : typing.Optional[ModelSettingsResponseModel]
            Settings controlling the dialogue generation.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        apply_text_normalization : typing.Optional[BodyTextToDialogueStreamWithTimestampsApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        output_format : typing.Optional[AllowedOutputFormats]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[StreamingAudioChunkWithTimestampsAndVoiceSegmentsResponseModel]
            Stream of transcription chunks

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.text_to_dialogue.stream_with_timestamps(
            output_format="mp3_22050_32",
            enable_logging=True,
            inputs=[
                {
                    "text": "text",
                    "voice_id": "voice_id"
                }
            ],
            model_id="eleven_v3",
            language_code="language_code",
            settings={
                "stability": 0.42
            },
            pronunciation_dictionary_locators=[
                {
                    "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                    "version_id": "version_id"
                }
            ],
            seed=2,
            apply_text_normalization="auto",
        )
        for chunk in response:
            print(chunk)
        """

        Validator(AllowedOutputFormats).is_optional().is_nullable().validate(
            output_format, "output_format"
        )
        Validator(bool).is_optional().is_nullable().validate(
            enable_logging, "enable_logging"
        )

        resolved_config = self._get_resolved_config(
            self._stream_with_timestamps_config, request_options
        )

        request_body = BodyTextToDialogueStreamWithTimestamps(
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyTextToDialogueStreamWithTimestamps).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/text-to-dialogue/stream/with-timestamps",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("output_format", output_format, nullable=True)
            .add_query("enable_logging", enable_logging, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        for response, status, _ in self.stream_request(serialized_request):
            yield (
                StreamingAudioChunkWithTimestampsAndVoiceSegmentsResponseModel.model_validate(
                    response
                )
                if should_validate_response(resolved_config)
                else construct_lenient(
                    StreamingAudioChunkWithTimestampsAndVoiceSegmentsResponseModel,
                    response,
                )
            )

    @cast_models
    def convert_with_timestamps(
        self,
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Optional[ModelSettingsResponseModel] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueFullWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio5, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AudioWithTimestampsAndVoiceSegmentsResponseModel:
        """
        Generate dialogue from text with precise character-level timing information for audio-text synchronization.

        Parameters
        ----------
        inputs : typing.Sequence[DialogueInput]
            A list of dialogue inputs, each containing text and a voice ID which will be converted into speech. The maximum number of unique voice IDs is 10. For reliable generation, keep the total character count across all `inputs[].text` values at or below 2,000 characters per request. Longer requests can terminate early in streaming responses or return a validation error.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        settings : typing.Optional[ModelSettingsResponseModel]
            Settings controlling the dialogue generation.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        apply_text_normalization : typing.Optional[BodyTextToDialogueFullWithTimestampsApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio5]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM and WAV formats with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudioWithTimestampsAndVoiceSegmentsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import OutputFormatOfTheGeneratedAudio5

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.text_to_dialogue.convert_with_timestamps(
            output_format="alaw_8000",
            enable_logging=True,
            inputs=[
                {
                    "text": "text",
                    "voice_id": "voice_id"
                }
            ],
            model_id="eleven_v3",
            language_code="language_code",
            settings={
                "stability": 0.42
            },
            pronunciation_dictionary_locators=[
                {
                    "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                    "version_id": "version_id"
                }
            ],
            seed=3,
            apply_text_normalization="auto",
        )
        """

        Validator(
            OutputFormatOfTheGeneratedAudio5
        ).is_optional().is_nullable().validate(output_format, "output_format")
        Validator(bool).is_optional().is_nullable().validate(
            enable_logging, "enable_logging"
        )

        resolved_config = self._get_resolved_config(
            self._convert_with_timestamps_config, request_options
        )

        request_body = BodyTextToDialogueFullWithTimestamps(
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyTextToDialogueFullWithTimestamps).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/text-to-dialogue/with-timestamps",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("output_format", output_format, nullable=True)
            .add_query("enable_logging", enable_logging, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AudioWithTimestampsAndVoiceSegmentsResponseModel.model_validate(
                    response
                )
                if should_validate_response(resolved_config)
                else construct_lenient(
                    AudioWithTimestampsAndVoiceSegmentsResponseModel, response
                )
            )
        )


class RawTextToDialogueClient:
    """
    Raw-response client for TextToDialogueClient.

    Each method delegates to the matching :class:`TextToDialogueClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: TextToDialogueClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def convert(
        self,
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Union[ModelSettingsResponseModel, None] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueMultiVoiceV1TextToDialoguePostApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio4, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = TextToDialogueClient.convert(
            _call_client,
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                        "output_format": output_format,
                        "enable_logging": enable_logging,
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
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Optional[ModelSettingsResponseModel] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueMultiVoiceStreamingV1TextToDialogueStreamPostApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = TextToDialogueClient.stream(
            _call_client,
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                        "output_format": output_format,
                        "enable_logging": enable_logging,
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
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Optional[ModelSettingsResponseModel] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueStreamWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[
        Generator[
            StreamingAudioChunkWithTimestampsAndVoiceSegmentsResponseModel, None, None
        ]
    ]:
        _call_client = self._client._for_one_call()
        data = TextToDialogueClient.stream_with_timestamps(
            _call_client,
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                        "output_format": output_format,
                        "enable_logging": enable_logging,
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
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Optional[ModelSettingsResponseModel] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueFullWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio5, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AudioWithTimestampsAndVoiceSegmentsResponseModel]:
        data = TextToDialogueClient.convert_with_timestamps(
            self._client,
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                        "output_format": output_format,
                        "enable_logging": enable_logging,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncTextToDialogueClient(TextToDialogueClient):
    """
    Async wrapper for TextToDialogueClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawTextToDialogueClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawTextToDialogueClient(self)

    def convert(
        self,
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Union[ModelSettingsResponseModel, None] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueMultiVoiceV1TextToDialoguePostApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio4, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Converts a list of text and voice ID pairs into speech (dialogue) and returns audio.

        Parameters
        ----------
        inputs : typing.Sequence[DialogueInput]
            A list of dialogue inputs, each containing text and a voice ID which will be converted into speech. The maximum number of unique voice IDs is 10. For reliable generation, keep the total character count across all `inputs[].text` values at or below 2,000 characters per request. Longer requests can terminate early in streaming responses or return a validation error.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        settings : typing.Optional[ModelSettingsResponseModel]
            Settings controlling the dialogue generation.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        apply_text_normalization : typing.Optional[BodyTextToDialogueMultiVoiceV1TextToDialoguePostApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio4]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM and WAV formats with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

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
        from fern.types import OutputFormatOfTheGeneratedAudio4

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.text_to_dialogue.convert(
                output_format="alaw_8000",
                enable_logging=True,
                inputs=[
                    {
                        "text": "[giggling] Knock knock",
                        "voice_id": "JBFqnCBsd6RMkjVDRZzb"
                    },
                    {
                        "text": "[curious] Who is there?",
                        "voice_id": "Aw4FAjKCGjjNkVhN1Xmq"
                    }
                ],
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().convert(
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                        "output_format": output_format,
                        "enable_logging": enable_logging,
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
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Optional[ModelSettingsResponseModel] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueMultiVoiceStreamingV1TextToDialogueStreamPostApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Converts a list of text and voice ID pairs into speech (dialogue) and returns an audio stream.

        Parameters
        ----------
        inputs : typing.Sequence[DialogueInput]
            A list of dialogue inputs, each containing text and a voice ID which will be converted into speech. The maximum number of unique voice IDs is 10. For reliable generation, keep the total character count across all `inputs[].text` values at or below 2,000 characters per request. Longer requests can terminate early in streaming responses or return a validation error.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        settings : typing.Optional[ModelSettingsResponseModel]
            Settings controlling the dialogue generation.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        apply_text_normalization : typing.Optional[BodyTextToDialogueMultiVoiceStreamingV1TextToDialogueStreamPostApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        output_format : typing.Optional[AllowedOutputFormats]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

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
        from fern.types import AllowedOutputFormats

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.text_to_dialogue.stream(
                output_format="mp3_22050_32",
                enable_logging=True,
                inputs=[
                    {
                        "text": "[giggling] Knock knock",
                        "voice_id": "JBFqnCBsd6RMkjVDRZzb"
                    },
                    {
                        "text": "[curious] Who is there?",
                        "voice_id": "Aw4FAjKCGjjNkVhN1Xmq"
                    }
                ],
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().stream(
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                        "output_format": output_format,
                        "enable_logging": enable_logging,
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
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Optional[ModelSettingsResponseModel] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueStreamWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[
        StreamingAudioChunkWithTimestampsAndVoiceSegmentsResponseModel, None
    ]:  # type: ignore[override]
        """
        Converts a list of text and voice ID pairs into speech (dialogue) and returns a stream of JSON blobs containing audio as a base64 encoded string and timestamps

        Parameters
        ----------
        inputs : typing.Sequence[DialogueInput]
            A list of dialogue inputs, each containing text and a voice ID which will be converted into speech. The maximum number of unique voice IDs is 10. For reliable generation, keep the total character count across all `inputs[].text` values at or below 2,000 characters per request. Longer requests can terminate early in streaming responses or return a validation error.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        settings : typing.Optional[ModelSettingsResponseModel]
            Settings controlling the dialogue generation.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        apply_text_normalization : typing.Optional[BodyTextToDialogueStreamWithTimestampsApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        output_format : typing.Optional[AllowedOutputFormats]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[StreamingAudioChunkWithTimestampsAndVoiceSegmentsResponseModel]
            Stream of transcription chunks

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.text_to_dialogue.stream_with_timestamps(
                output_format="mp3_22050_32",
                enable_logging=True,
                inputs=[
                    {
                        "text": "text",
                        "voice_id": "voice_id"
                    }
                ],
                model_id="eleven_v3",
                language_code="language_code",
                settings={
                    "stability": 0.42
                },
                pronunciation_dictionary_locators=[
                    {
                        "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                        "version_id": "version_id"
                    }
                ],
                seed=2,
                apply_text_normalization="auto",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().stream_with_timestamps(
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                        "output_format": output_format,
                        "enable_logging": enable_logging,
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
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Optional[ModelSettingsResponseModel] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueFullWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio5, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AudioWithTimestampsAndVoiceSegmentsResponseModel]:  # type: ignore[override]
        """
        Generate dialogue from text with precise character-level timing information for audio-text synchronization.

        Parameters
        ----------
        inputs : typing.Sequence[DialogueInput]
            A list of dialogue inputs, each containing text and a voice ID which will be converted into speech. The maximum number of unique voice IDs is 10. For reliable generation, keep the total character count across all `inputs[].text` values at or below 2,000 characters per request. Longer requests can terminate early in streaming responses or return a validation error.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        language_code : typing.Optional[str]
            Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.

        settings : typing.Optional[ModelSettingsResponseModel]
            Settings controlling the dialogue generation.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        apply_text_normalization : typing.Optional[BodyTextToDialogueFullWithTimestampsApplyTextNormalization]
            This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio5]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM and WAV formats with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudioWithTimestampsAndVoiceSegmentsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import OutputFormatOfTheGeneratedAudio5

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.text_to_dialogue.convert_with_timestamps(
                output_format="alaw_8000",
                enable_logging=True,
                inputs=[
                    {
                        "text": "text",
                        "voice_id": "voice_id"
                    }
                ],
                model_id="eleven_v3",
                language_code="language_code",
                settings={
                    "stability": 0.42
                },
                pronunciation_dictionary_locators=[
                    {
                        "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                        "version_id": "version_id"
                    }
                ],
                seed=3,
                apply_text_normalization="auto",
            )


        asyncio.run(main())
        """
        return to_async(super().convert_with_timestamps)(
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                        "output_format": output_format,
                        "enable_logging": enable_logging,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawTextToDialogueClient:
    """
    Async raw-response client for AsyncTextToDialogueClient.
    """

    def __init__(self, client: AsyncTextToDialogueClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def convert(
        self,
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Union[ModelSettingsResponseModel, None] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueMultiVoiceV1TextToDialoguePostApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio4, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncTextToDialogueClient.convert(
            _call_client,
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                        "output_format": output_format,
                        "enable_logging": enable_logging,
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
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Optional[ModelSettingsResponseModel] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueMultiVoiceStreamingV1TextToDialogueStreamPostApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncTextToDialogueClient.stream(
            _call_client,
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                        "output_format": output_format,
                        "enable_logging": enable_logging,
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
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Optional[ModelSettingsResponseModel] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueStreamWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[
        AsyncGenerator[
            StreamingAudioChunkWithTimestampsAndVoiceSegmentsResponseModel, None
        ]
    ]:
        _call_client = self._client._for_one_call()
        data = AsyncTextToDialogueClient.stream_with_timestamps(
            _call_client,
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                        "output_format": output_format,
                        "enable_logging": enable_logging,
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
        *,
        inputs: List[DialogueInput],
        model_id: Optional[str] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        settings: Optional[ModelSettingsResponseModel] = SENTINEL,
        pronunciation_dictionary_locators: Union[
            List[PronunciationDictionaryVersionLocator], None
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        apply_text_normalization: Optional[
            BodyTextToDialogueFullWithTimestampsApplyTextNormalization
        ] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio5, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AudioWithTimestampsAndVoiceSegmentsResponseModel]:
        data = await AsyncTextToDialogueClient.convert_with_timestamps(
            self._client,
            inputs=inputs,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "language_code": language_code,
                        "settings": settings,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "seed": seed,
                        "apply_text_normalization": apply_text_normalization,
                        "output_format": output_format,
                        "enable_logging": enable_logging,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
