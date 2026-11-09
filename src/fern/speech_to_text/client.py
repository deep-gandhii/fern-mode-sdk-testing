from typing import Any, Optional, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types.speech_to_text_convert_response import SpeechToTextConvertResponse_adapter
from ..types import (
    BodySpeechToTextV1SpeechToTextPost,
    BodySpeechToTextV1SpeechToTextPostEntityDetection,
    BodySpeechToTextV1SpeechToTextPostEntityRedaction,
    BodySpeechToTextV1SpeechToTextPostFileFormat,
    BodySpeechToTextV1SpeechToTextPostModelId,
    BodySpeechToTextV1SpeechToTextPostMultichannelOutputStyle,
    BodySpeechToTextV1SpeechToTextPostTimestampsGranularity,
    BodySpeechToTextV1SpeechToTextPostWebhookMetadata,
    ExportOptions,
    HttpValidationError,
    SpeechToTextConvertResponse,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.transport.api_error import ApiError
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .transcripts.client import (
        TranscriptsClient as _TranscriptsClient,
        AsyncTranscriptsClient as _AsyncTranscriptsClient,
    )


class SpeechToTextClient(BaseService):
    """
    Fern-style resource client for SpeechToTextClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._transcripts: Any = None
        self._convert_config: SdkConfig = {}

    @property
    def transcripts(self) -> "_TranscriptsClient":
        """Lazily construct and return the transcripts sub-resource client."""
        if self._transcripts is None:
            from .transcripts.client import TranscriptsClient

            _child = TranscriptsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._transcripts = _child
        return self._transcripts

    def set_base_url(self, base_url: Union[ElevenLabsEnvironment, str]):
        """
        Sets the base URL for this resource client and every sub-resource client already built.

        A child is constructed with a COPY of this client's base URL and then cached, so the
        inherited setter -- which only rebinds the receiver -- left an already-materialised child
        routing to the old host. Switching environment after one call had built a child kept
        sending that child's requests to the previous server, silently and with no error.

        :param base_url: The base URL to be set, as a string or an ElevenLabsEnvironment enum member.
        :return: The resource client.
        """
        super().set_base_url(base_url)
        if self._transcripts is not None:
            self._transcripts.set_base_url(base_url)

        return self

    def set_config(self, config: SdkConfig):
        """
        Sets service-level configuration for this resource client and every sub-resource client
        already built.

        A child is constructed holding a reference to this client's config and is then cached,
        and both this setter and `set_retry` REBIND `_service_config` rather than mutating it --
        so an already-materialised child kept the config it was born with. The parent wins:
        last writer overwrites, the same rule `set_base_url` and `set_timeout` follow, which keeps
        a client and its children in exact agreement. Narrower scopes are untouched, because
        method-level config (`set_<method>_config`) and per-call `request_options` live in their
        own attributes and are never overwritten by this.

        :param SdkConfig config: Configuration dictionary to override SDK-level defaults.
        :return: The resource client.
        """
        super().set_config(config)
        if self._transcripts is not None:
            self._transcripts.set_config(config)

        return self

    def set_timeout(self, timeout: float):
        """
        Sets the timeout for this resource client and every sub-resource client already built.

        A child is constructed with a COPY of this client's timeout and its request handler is
        built from it, so the inherited setter -- which only rebinds the receiver and rebuilds the
        receiver's handler -- left an already-materialised child on the old timeout.

        :param float timeout: The timeout (in seconds) to be set.
        :return: The resource client.
        """
        super().set_timeout(timeout)
        if self._transcripts is not None:
            self._transcripts.set_timeout(timeout)

        return self

    def set_convert_config(self, config: SdkConfig):
        """
        Sets method-level configuration for convert.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._convert_config = config
        return self

    @property
    def with_raw_response(self) -> "RawSpeechToTextClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawSpeechToTextClient(self)

    @cast_models
    def convert(
        self,
        *,
        model_id: BodySpeechToTextV1SpeechToTextPostModelId,
        file: Union[bytes, None] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        tag_audio_events: Optional[bool] = SENTINEL,
        num_speakers: Union[int, None] = SENTINEL,
        timestamps_granularity: Optional[
            BodySpeechToTextV1SpeechToTextPostTimestampsGranularity
        ] = SENTINEL,
        diarize: Optional[bool] = SENTINEL,
        diarization_threshold: Union[float, None] = SENTINEL,
        additional_formats: Optional[List[ExportOptions]] = SENTINEL,
        file_format: Optional[BodySpeechToTextV1SpeechToTextPostFileFormat] = SENTINEL,
        cloud_storage_url: Union[str, None] = SENTINEL,
        source_url: Union[str, None] = SENTINEL,
        webhook: Optional[bool] = SENTINEL,
        webhook_id: Union[str, None] = SENTINEL,
        temperature: Union[float, None] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        use_multi_channel: Optional[bool] = SENTINEL,
        multichannel_output_style: Optional[
            BodySpeechToTextV1SpeechToTextPostMultichannelOutputStyle
        ] = SENTINEL,
        webhook_metadata: Union[
            BodySpeechToTextV1SpeechToTextPostWebhookMetadata, None
        ] = SENTINEL,
        entity_detection: Union[
            BodySpeechToTextV1SpeechToTextPostEntityDetection, None
        ] = SENTINEL,
        no_verbatim: Optional[bool] = SENTINEL,
        use_speaker_library: Optional[bool] = SENTINEL,
        detect_speaker_roles: Optional[bool] = SENTINEL,
        entity_redaction: Union[
            BodySpeechToTextV1SpeechToTextPostEntityRedaction, None
        ] = SENTINEL,
        entity_redaction_mode: Optional[str] = SENTINEL,
        keyterms: Optional[List[str]] = SENTINEL,
        token: Union[str, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Union[SpeechToTextConvertResponse, Any]:
        """
        Transcribe an audio or video file. If webhook is set to true, the request will be processed asynchronously and results sent to configured webhooks. When use_multi_channel is true and the provided audio has multiple channels, a 'transcripts' object with separate transcripts for each channel is returned; set multichannel_output_style='combined' to instead receive a single transcript with all channels merged and sorted by time. Otherwise, returns a single transcript. The optional webhook_metadata parameter allows you to attach custom data that will be included in webhook responses for request correlation and tracking.

        Parameters
        ----------
        model_id : BodySpeechToTextV1SpeechToTextPostModelId
            The ID of the model to use for transcription.

        file : typing.Optional[core.File]
            The file to transcribe (100ms minimum audio length). All major audio and video formats are supported. Exactly one of the file or cloud_storage_url parameters must be provided. The file size must be less than 5.0GB.

        language_code : typing.Optional[str]
            An ISO-639-1 or ISO-639-3 language_code corresponding to the language of the audio file. Can sometimes improve transcription performance if known beforehand. Defaults to null, in this case the language is predicted automatically.

        tag_audio_events : typing.Optional[bool]
            Whether to tag audio events like (laughter), (footsteps), etc. in the transcription.

        num_speakers : typing.Optional[int]
            The maximum amount of speakers talking in the uploaded file. Can help with predicting who speaks when. The maximum amount of speakers that can be predicted is 32. Defaults to null, in this case the amount of speakers is set to the maximum value the model supports.

        timestamps_granularity : typing.Optional[BodySpeechToTextV1SpeechToTextPostTimestampsGranularity]
            The granularity of the timestamps in the transcription. 'word' provides word-level timestamps and 'character' provides character-level timestamps per word.

        diarize : typing.Optional[bool]
            Whether to annotate which speaker is currently talking in the uploaded file.

        diarization_threshold : typing.Optional[float]
            Diarization threshold to apply during speaker diarization. A higher value means there will be a lower chance of one speaker being diarized as two different speakers but also a higher chance of two different speakers being diarized as one speaker (less total speakers predicted). A low value means there will be a higher chance of one speaker being diarized as two different speakers but also a lower chance of two different speakers being diarized as one speaker (more total speakers predicted). Can only be set when diarize=True and num_speakers=None. Defaults to None, in which case we will choose a threshold based on the model_id (0.22 usually).

        additional_formats : typing.Optional[typing.Sequence[ExportOptions]]

        file_format : typing.Optional[BodySpeechToTextV1SpeechToTextPostFileFormat]
            The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform.

        cloud_storage_url : typing.Optional[str]
            [Deprecated] This parameter is deprecated and will be removed in the future. Use 'source_url' instead.The HTTPS URL of the file to transcribe. Exactly one of the file or cloud_storage_url parameters must be provided. The file must be accessible via HTTPS and the file size must be less than 2GB. Any valid HTTPS URL is accepted, including URLs from cloud storage providers (AWS S3, Google Cloud Storage, Cloudflare R2, etc.), CDNs, or any other HTTPS source. URLs can be pre-signed or include authentication tokens in query parameters.

        source_url : typing.Optional[str]
            The URL of an audio or video file to transcribe. Supports hosted video or audio files, YouTube video URLs, TikTok video URLs, and other video hosting services.

        webhook : typing.Optional[bool]
            Whether to send the transcription result to configured speech-to-text webhooks.  If set the request will return early without the transcription, which will be delivered later via webhook.

        webhook_id : typing.Optional[str]
            Optional specific webhook ID to send the transcription result to. Only valid when webhook is set to true. If not provided, transcription will be sent to all configured speech-to-text webhooks.

        temperature : typing.Optional[float]
            Controls the randomness of the transcription output. Accepts values between 0.0 and 2.0, where higher values result in more diverse and less deterministic results. If omitted, we will use a temperature based on the model you selected which is usually 0.

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be an integer between 0 and 2147483647.

        use_multi_channel : typing.Optional[bool]
            Whether the audio file contains multiple channels where each channel contains a single speaker. When enabled, each channel is transcribed independently. By default a separate transcript is returned per channel; set multichannel_output_style='combined' to instead receive a single transcript with all channels merged and sorted by time. Each word in the response includes a 'channel_index' field indicating which channel it was spoken on. A maximum of 5 channels is supported. Each channel is billed independently at the full audio duration, so cost scales linearly with the number of channels.

        multichannel_output_style : typing.Optional[BodySpeechToTextV1SpeechToTextPostMultichannelOutputStyle]
            Controls the response shape when use_multi_channel is enabled. 'separate' (default) returns one transcript per channel under 'transcripts'. 'combined' merges all channels into a single transcript whose words are sorted by start time, each carrying a 'channel_index' - matching the single-channel response shape. 'combined' requires timestamps (timestamps_granularity must not be 'none') and does not support entity detection or redaction.

        webhook_metadata : typing.Optional[BodySpeechToTextV1SpeechToTextPostWebhookMetadata]
            Optional metadata to be included in the webhook response. This should be a JSON string representing an object with a maximum depth of 2 levels and maximum size of 16KB. Useful for tracking internal IDs, job references, or other contextual information.

        entity_detection : typing.Optional[BodySpeechToTextV1SpeechToTextPostEntityDetection]
            Detect entities in the transcript. Can be 'all' to detect all entities, a single entity type or category string, or a list of entity types/categories. Categories include 'pii', 'phi', 'pci', 'other', 'offensive_language'. When enabled, detected entities will be returned in the 'entities' field with their text, type, and character positions. Usage of this parameter will incur an additional 30% surcharge on the base transcription cost.

        no_verbatim : typing.Optional[bool]
            If true, the transcription will not have any filler words, false starts and non-speech sounds. Only supported with scribe_v2 model.

        use_speaker_library : typing.Optional[bool]
            Whether to use the speaker library for identifying known speakers during diarization. When enabled and diarize is true, detected speakers will be matched against registered speakers in the workspace's speaker library.

        detect_speaker_roles : typing.Optional[bool]
            Whether to detect speaker roles (agent vs customer). Requires diarize=true. Cannot be used with use_multi_channel=true. When enabled, speaker_id values will be 'agent' and 'customer' instead of 'speaker_0', 'speaker_1', etc. Usage incurs an additional 10% surcharge on base transcription cost.

        entity_redaction : typing.Optional[BodySpeechToTextV1SpeechToTextPostEntityRedaction]
            Redact entities from the transcript text. Accepts the same format as entity_detection: 'all', a category ('pii', 'phi'), or specific entity types. Must be a subset of entity_detection. When redaction is enabled, the entities field will not be returned. Usage of this parameter will incur an additional 30% surcharge on the base transcription cost.

        entity_redaction_mode : typing.Optional[str]
            How to format redacted entities. 'redacted' replaces with {REDACTED}, 'entity_type' replaces with {ENTITY_TYPE}, 'enumerated_entity_type' replaces with {ENTITY_TYPE_N} where N enumerates each occurrence. Only used when entity_redaction is set.

        keyterms : typing.Optional[typing.Sequence[str]]
            A list of keyterms to bias the transcription towards.           The keyterms are words or phrases you want the model to recognise more accurately.           The number of keyterms cannot exceed 1000.           The length of each keyterm must be less than 50 characters.           Keyterms can contain at most 5 words (after normalisation).           For example ["hello", "world", "technical term"].           The following characters are not supported: `<`, `>`, `{`, `}`, `[`, `]`, `\\`.           Usage of this parameter will incur an additional 20% surcharge on the base transcription cost.           When more than 100 keyterms are provided, a minimum billable duration of 20 seconds applies per request.

        token : typing.Optional[str]
            A single-use authentication token created via POST /v1/single-use-token/batch_scribe. This token can only be used once and expires after 15 minutes. Alternative to API key or bearer token authentication for frontend clients.

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean log and transcript storage features are unavailable for this request. Zero retention mode may only be used by enterprise customers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Union[SpeechToTextConvertResponse, typing.Any]
            Synchronous transcription result

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.speech_to_text.convert(
            token="token",
            enable_logging=True,
            model_id="scribe_v2",
            file="file",
            language_code="language_code",
            tag_audio_events=True,
            num_speakers=3,
            timestamps_granularity="none",
            diarize=True,
            diarization_threshold=0.18,
            additional_formats=[
                {
                    "include_speakers": True,
                    "include_timestamps": True,
                    "format": "segmented_json",
                    "segment_on_silence_longer_than_s": 7.13,
                    "max_segment_duration_s": 2.39,
                    "max_segment_chars": 7
                }
            ],
            file_format="pcm_s16le_16",
            source_url="source_url",
            webhook=False,
            webhook_id="webhook_id",
            temperature=1.33,
            seed=428677088,
            use_multi_channel=True,
            multichannel_output_style="separate",
            webhook_metadata="Utconsectetur",
            entity_detection="pariatur ve",
            no_verbatim=False,
            use_speaker_library=False,
            detect_speaker_roles=False,
            entity_redaction="sed pariatur",
            entity_redaction_mode="enumerated_entity_type",
            keyterms=[
                "keyterms"
            ],
        )
        """

        Validator(str).is_optional().is_nullable().validate(token, "token")
        Validator(bool).is_optional().is_nullable().validate(
            enable_logging, "enable_logging"
        )

        resolved_config = self._get_resolved_config(
            self._convert_config, request_options
        )

        request_body = BodySpeechToTextV1SpeechToTextPost(
            model_id=model_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "language_code": language_code,
                        "tag_audio_events": tag_audio_events,
                        "num_speakers": num_speakers,
                        "timestamps_granularity": timestamps_granularity,
                        "diarize": diarize,
                        "diarization_threshold": diarization_threshold,
                        "additional_formats": additional_formats,
                        "file_format": file_format,
                        "cloud_storage_url": cloud_storage_url,
                        "source_url": source_url,
                        "webhook": webhook,
                        "webhook_id": webhook_id,
                        "temperature": temperature,
                        "seed": seed,
                        "use_multi_channel": use_multi_channel,
                        "multichannel_output_style": multichannel_output_style,
                        "webhook_metadata": webhook_metadata,
                        "entity_detection": entity_detection,
                        "no_verbatim": no_verbatim,
                        "use_speaker_library": use_speaker_library,
                        "detect_speaker_roles": detect_speaker_roles,
                        "entity_redaction": entity_redaction,
                        "entity_redaction_mode": entity_redaction_mode,
                        "keyterms": keyterms,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodySpeechToTextV1SpeechToTextPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/speech-to-text",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("token", token, nullable=True)
            .add_query("enable_logging", enable_logging, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, status, _ = self.send_request(serialized_request)
        if status in {200, 202} and response in (b"", ""):
            return None
        if status == 200:
            return (
                None
                if response in (b"", "")
                else (
                    SpeechToTextConvertResponse_adapter.validate_python(response)
                    if should_validate_response(resolved_config)
                    else construct_lenient(SpeechToTextConvertResponse, response)
                )
            )
        if status == 202:
            return response
        raise ApiError("Error on deserializing the response.", status, response)


class RawSpeechToTextClient:
    """
    Raw-response client for SpeechToTextClient.

    Each method delegates to the matching :class:`SpeechToTextClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: SpeechToTextClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def convert(
        self,
        *,
        model_id: BodySpeechToTextV1SpeechToTextPostModelId,
        file: Union[bytes, None] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        tag_audio_events: Optional[bool] = SENTINEL,
        num_speakers: Union[int, None] = SENTINEL,
        timestamps_granularity: Optional[
            BodySpeechToTextV1SpeechToTextPostTimestampsGranularity
        ] = SENTINEL,
        diarize: Optional[bool] = SENTINEL,
        diarization_threshold: Union[float, None] = SENTINEL,
        additional_formats: Optional[List[ExportOptions]] = SENTINEL,
        file_format: Optional[BodySpeechToTextV1SpeechToTextPostFileFormat] = SENTINEL,
        cloud_storage_url: Union[str, None] = SENTINEL,
        source_url: Union[str, None] = SENTINEL,
        webhook: Optional[bool] = SENTINEL,
        webhook_id: Union[str, None] = SENTINEL,
        temperature: Union[float, None] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        use_multi_channel: Optional[bool] = SENTINEL,
        multichannel_output_style: Optional[
            BodySpeechToTextV1SpeechToTextPostMultichannelOutputStyle
        ] = SENTINEL,
        webhook_metadata: Union[
            BodySpeechToTextV1SpeechToTextPostWebhookMetadata, None
        ] = SENTINEL,
        entity_detection: Union[
            BodySpeechToTextV1SpeechToTextPostEntityDetection, None
        ] = SENTINEL,
        no_verbatim: Optional[bool] = SENTINEL,
        use_speaker_library: Optional[bool] = SENTINEL,
        detect_speaker_roles: Optional[bool] = SENTINEL,
        entity_redaction: Union[
            BodySpeechToTextV1SpeechToTextPostEntityRedaction, None
        ] = SENTINEL,
        entity_redaction_mode: Optional[str] = SENTINEL,
        keyterms: Optional[List[str]] = SENTINEL,
        token: Union[str, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Union[SpeechToTextConvertResponse, Any]]:
        data = SpeechToTextClient.convert(
            self._client,
            model_id=model_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "language_code": language_code,
                        "tag_audio_events": tag_audio_events,
                        "num_speakers": num_speakers,
                        "timestamps_granularity": timestamps_granularity,
                        "diarize": diarize,
                        "diarization_threshold": diarization_threshold,
                        "additional_formats": additional_formats,
                        "file_format": file_format,
                        "cloud_storage_url": cloud_storage_url,
                        "source_url": source_url,
                        "webhook": webhook,
                        "webhook_id": webhook_id,
                        "temperature": temperature,
                        "seed": seed,
                        "use_multi_channel": use_multi_channel,
                        "multichannel_output_style": multichannel_output_style,
                        "webhook_metadata": webhook_metadata,
                        "entity_detection": entity_detection,
                        "no_verbatim": no_verbatim,
                        "use_speaker_library": use_speaker_library,
                        "detect_speaker_roles": detect_speaker_roles,
                        "entity_redaction": entity_redaction,
                        "entity_redaction_mode": entity_redaction_mode,
                        "keyterms": keyterms,
                        "token": token,
                        "enable_logging": enable_logging,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncSpeechToTextClient(SpeechToTextClient):
    """
    Async wrapper for SpeechToTextClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def transcripts(self) -> "_AsyncTranscriptsClient":
        """Lazily construct and return the async transcripts sub-resource client."""
        if self._transcripts is None:
            from .transcripts.client import AsyncTranscriptsClient

            _child = AsyncTranscriptsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._transcripts = _child
        return self._transcripts

    @property
    def with_raw_response(self) -> "AsyncRawSpeechToTextClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawSpeechToTextClient(self)

    def convert(
        self,
        *,
        model_id: BodySpeechToTextV1SpeechToTextPostModelId,
        file: Union[bytes, None] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        tag_audio_events: Optional[bool] = SENTINEL,
        num_speakers: Union[int, None] = SENTINEL,
        timestamps_granularity: Optional[
            BodySpeechToTextV1SpeechToTextPostTimestampsGranularity
        ] = SENTINEL,
        diarize: Optional[bool] = SENTINEL,
        diarization_threshold: Union[float, None] = SENTINEL,
        additional_formats: Optional[List[ExportOptions]] = SENTINEL,
        file_format: Optional[BodySpeechToTextV1SpeechToTextPostFileFormat] = SENTINEL,
        cloud_storage_url: Union[str, None] = SENTINEL,
        source_url: Union[str, None] = SENTINEL,
        webhook: Optional[bool] = SENTINEL,
        webhook_id: Union[str, None] = SENTINEL,
        temperature: Union[float, None] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        use_multi_channel: Optional[bool] = SENTINEL,
        multichannel_output_style: Optional[
            BodySpeechToTextV1SpeechToTextPostMultichannelOutputStyle
        ] = SENTINEL,
        webhook_metadata: Union[
            BodySpeechToTextV1SpeechToTextPostWebhookMetadata, None
        ] = SENTINEL,
        entity_detection: Union[
            BodySpeechToTextV1SpeechToTextPostEntityDetection, None
        ] = SENTINEL,
        no_verbatim: Optional[bool] = SENTINEL,
        use_speaker_library: Optional[bool] = SENTINEL,
        detect_speaker_roles: Optional[bool] = SENTINEL,
        entity_redaction: Union[
            BodySpeechToTextV1SpeechToTextPostEntityRedaction, None
        ] = SENTINEL,
        entity_redaction_mode: Optional[str] = SENTINEL,
        keyterms: Optional[List[str]] = SENTINEL,
        token: Union[str, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Union[SpeechToTextConvertResponse, Any]]:  # type: ignore[override]
        """
        Transcribe an audio or video file. If webhook is set to true, the request will be processed asynchronously and results sent to configured webhooks. When use_multi_channel is true and the provided audio has multiple channels, a 'transcripts' object with separate transcripts for each channel is returned; set multichannel_output_style='combined' to instead receive a single transcript with all channels merged and sorted by time. Otherwise, returns a single transcript. The optional webhook_metadata parameter allows you to attach custom data that will be included in webhook responses for request correlation and tracking.

        Parameters
        ----------
        model_id : BodySpeechToTextV1SpeechToTextPostModelId
            The ID of the model to use for transcription.

        file : typing.Optional[core.File]
            The file to transcribe (100ms minimum audio length). All major audio and video formats are supported. Exactly one of the file or cloud_storage_url parameters must be provided. The file size must be less than 5.0GB.

        language_code : typing.Optional[str]
            An ISO-639-1 or ISO-639-3 language_code corresponding to the language of the audio file. Can sometimes improve transcription performance if known beforehand. Defaults to null, in this case the language is predicted automatically.

        tag_audio_events : typing.Optional[bool]
            Whether to tag audio events like (laughter), (footsteps), etc. in the transcription.

        num_speakers : typing.Optional[int]
            The maximum amount of speakers talking in the uploaded file. Can help with predicting who speaks when. The maximum amount of speakers that can be predicted is 32. Defaults to null, in this case the amount of speakers is set to the maximum value the model supports.

        timestamps_granularity : typing.Optional[BodySpeechToTextV1SpeechToTextPostTimestampsGranularity]
            The granularity of the timestamps in the transcription. 'word' provides word-level timestamps and 'character' provides character-level timestamps per word.

        diarize : typing.Optional[bool]
            Whether to annotate which speaker is currently talking in the uploaded file.

        diarization_threshold : typing.Optional[float]
            Diarization threshold to apply during speaker diarization. A higher value means there will be a lower chance of one speaker being diarized as two different speakers but also a higher chance of two different speakers being diarized as one speaker (less total speakers predicted). A low value means there will be a higher chance of one speaker being diarized as two different speakers but also a lower chance of two different speakers being diarized as one speaker (more total speakers predicted). Can only be set when diarize=True and num_speakers=None. Defaults to None, in which case we will choose a threshold based on the model_id (0.22 usually).

        additional_formats : typing.Optional[typing.Sequence[ExportOptions]]

        file_format : typing.Optional[BodySpeechToTextV1SpeechToTextPostFileFormat]
            The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform.

        cloud_storage_url : typing.Optional[str]
            [Deprecated] This parameter is deprecated and will be removed in the future. Use 'source_url' instead.The HTTPS URL of the file to transcribe. Exactly one of the file or cloud_storage_url parameters must be provided. The file must be accessible via HTTPS and the file size must be less than 2GB. Any valid HTTPS URL is accepted, including URLs from cloud storage providers (AWS S3, Google Cloud Storage, Cloudflare R2, etc.), CDNs, or any other HTTPS source. URLs can be pre-signed or include authentication tokens in query parameters.

        source_url : typing.Optional[str]
            The URL of an audio or video file to transcribe. Supports hosted video or audio files, YouTube video URLs, TikTok video URLs, and other video hosting services.

        webhook : typing.Optional[bool]
            Whether to send the transcription result to configured speech-to-text webhooks.  If set the request will return early without the transcription, which will be delivered later via webhook.

        webhook_id : typing.Optional[str]
            Optional specific webhook ID to send the transcription result to. Only valid when webhook is set to true. If not provided, transcription will be sent to all configured speech-to-text webhooks.

        temperature : typing.Optional[float]
            Controls the randomness of the transcription output. Accepts values between 0.0 and 2.0, where higher values result in more diverse and less deterministic results. If omitted, we will use a temperature based on the model you selected which is usually 0.

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be an integer between 0 and 2147483647.

        use_multi_channel : typing.Optional[bool]
            Whether the audio file contains multiple channels where each channel contains a single speaker. When enabled, each channel is transcribed independently. By default a separate transcript is returned per channel; set multichannel_output_style='combined' to instead receive a single transcript with all channels merged and sorted by time. Each word in the response includes a 'channel_index' field indicating which channel it was spoken on. A maximum of 5 channels is supported. Each channel is billed independently at the full audio duration, so cost scales linearly with the number of channels.

        multichannel_output_style : typing.Optional[BodySpeechToTextV1SpeechToTextPostMultichannelOutputStyle]
            Controls the response shape when use_multi_channel is enabled. 'separate' (default) returns one transcript per channel under 'transcripts'. 'combined' merges all channels into a single transcript whose words are sorted by start time, each carrying a 'channel_index' - matching the single-channel response shape. 'combined' requires timestamps (timestamps_granularity must not be 'none') and does not support entity detection or redaction.

        webhook_metadata : typing.Optional[BodySpeechToTextV1SpeechToTextPostWebhookMetadata]
            Optional metadata to be included in the webhook response. This should be a JSON string representing an object with a maximum depth of 2 levels and maximum size of 16KB. Useful for tracking internal IDs, job references, or other contextual information.

        entity_detection : typing.Optional[BodySpeechToTextV1SpeechToTextPostEntityDetection]
            Detect entities in the transcript. Can be 'all' to detect all entities, a single entity type or category string, or a list of entity types/categories. Categories include 'pii', 'phi', 'pci', 'other', 'offensive_language'. When enabled, detected entities will be returned in the 'entities' field with their text, type, and character positions. Usage of this parameter will incur an additional 30% surcharge on the base transcription cost.

        no_verbatim : typing.Optional[bool]
            If true, the transcription will not have any filler words, false starts and non-speech sounds. Only supported with scribe_v2 model.

        use_speaker_library : typing.Optional[bool]
            Whether to use the speaker library for identifying known speakers during diarization. When enabled and diarize is true, detected speakers will be matched against registered speakers in the workspace's speaker library.

        detect_speaker_roles : typing.Optional[bool]
            Whether to detect speaker roles (agent vs customer). Requires diarize=true. Cannot be used with use_multi_channel=true. When enabled, speaker_id values will be 'agent' and 'customer' instead of 'speaker_0', 'speaker_1', etc. Usage incurs an additional 10% surcharge on base transcription cost.

        entity_redaction : typing.Optional[BodySpeechToTextV1SpeechToTextPostEntityRedaction]
            Redact entities from the transcript text. Accepts the same format as entity_detection: 'all', a category ('pii', 'phi'), or specific entity types. Must be a subset of entity_detection. When redaction is enabled, the entities field will not be returned. Usage of this parameter will incur an additional 30% surcharge on the base transcription cost.

        entity_redaction_mode : typing.Optional[str]
            How to format redacted entities. 'redacted' replaces with {REDACTED}, 'entity_type' replaces with {ENTITY_TYPE}, 'enumerated_entity_type' replaces with {ENTITY_TYPE_N} where N enumerates each occurrence. Only used when entity_redaction is set.

        keyterms : typing.Optional[typing.Sequence[str]]
            A list of keyterms to bias the transcription towards.           The keyterms are words or phrases you want the model to recognise more accurately.           The number of keyterms cannot exceed 1000.           The length of each keyterm must be less than 50 characters.           Keyterms can contain at most 5 words (after normalisation).           For example ["hello", "world", "technical term"].           The following characters are not supported: `<`, `>`, `{`, `}`, `[`, `]`, `\\`.           Usage of this parameter will incur an additional 20% surcharge on the base transcription cost.           When more than 100 keyterms are provided, a minimum billable duration of 20 seconds applies per request.

        token : typing.Optional[str]
            A single-use authentication token created via POST /v1/single-use-token/batch_scribe. This token can only be used once and expires after 15 minutes. Alternative to API key or bearer token authentication for frontend clients.

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean log and transcript storage features are unavailable for this request. Zero retention mode may only be used by enterprise customers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Union[SpeechToTextConvertResponse, typing.Any]
            Synchronous transcription result

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.speech_to_text.convert(
                token="token",
                enable_logging=True,
                model_id="scribe_v2",
                file="file",
                language_code="language_code",
                tag_audio_events=True,
                num_speakers=3,
                timestamps_granularity="none",
                diarize=True,
                diarization_threshold=0.18,
                additional_formats=[
                    {
                        "include_speakers": True,
                        "include_timestamps": True,
                        "format": "segmented_json",
                        "segment_on_silence_longer_than_s": 7.13,
                        "max_segment_duration_s": 2.39,
                        "max_segment_chars": 7
                    }
                ],
                file_format="pcm_s16le_16",
                source_url="source_url",
                webhook=False,
                webhook_id="webhook_id",
                temperature=1.33,
                seed=428677088,
                use_multi_channel=True,
                multichannel_output_style="separate",
                webhook_metadata="Utconsectetur",
                entity_detection="pariatur ve",
                no_verbatim=False,
                use_speaker_library=False,
                detect_speaker_roles=False,
                entity_redaction="sed pariatur",
                entity_redaction_mode="enumerated_entity_type",
                keyterms=[
                    "keyterms"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().convert)(
            model_id=model_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "language_code": language_code,
                        "tag_audio_events": tag_audio_events,
                        "num_speakers": num_speakers,
                        "timestamps_granularity": timestamps_granularity,
                        "diarize": diarize,
                        "diarization_threshold": diarization_threshold,
                        "additional_formats": additional_formats,
                        "file_format": file_format,
                        "cloud_storage_url": cloud_storage_url,
                        "source_url": source_url,
                        "webhook": webhook,
                        "webhook_id": webhook_id,
                        "temperature": temperature,
                        "seed": seed,
                        "use_multi_channel": use_multi_channel,
                        "multichannel_output_style": multichannel_output_style,
                        "webhook_metadata": webhook_metadata,
                        "entity_detection": entity_detection,
                        "no_verbatim": no_verbatim,
                        "use_speaker_library": use_speaker_library,
                        "detect_speaker_roles": detect_speaker_roles,
                        "entity_redaction": entity_redaction,
                        "entity_redaction_mode": entity_redaction_mode,
                        "keyterms": keyterms,
                        "token": token,
                        "enable_logging": enable_logging,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawSpeechToTextClient:
    """
    Async raw-response client for AsyncSpeechToTextClient.
    """

    def __init__(self, client: AsyncSpeechToTextClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def convert(
        self,
        *,
        model_id: BodySpeechToTextV1SpeechToTextPostModelId,
        file: Union[bytes, None] = SENTINEL,
        language_code: Union[str, None] = SENTINEL,
        tag_audio_events: Optional[bool] = SENTINEL,
        num_speakers: Union[int, None] = SENTINEL,
        timestamps_granularity: Optional[
            BodySpeechToTextV1SpeechToTextPostTimestampsGranularity
        ] = SENTINEL,
        diarize: Optional[bool] = SENTINEL,
        diarization_threshold: Union[float, None] = SENTINEL,
        additional_formats: Optional[List[ExportOptions]] = SENTINEL,
        file_format: Optional[BodySpeechToTextV1SpeechToTextPostFileFormat] = SENTINEL,
        cloud_storage_url: Union[str, None] = SENTINEL,
        source_url: Union[str, None] = SENTINEL,
        webhook: Optional[bool] = SENTINEL,
        webhook_id: Union[str, None] = SENTINEL,
        temperature: Union[float, None] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        use_multi_channel: Optional[bool] = SENTINEL,
        multichannel_output_style: Optional[
            BodySpeechToTextV1SpeechToTextPostMultichannelOutputStyle
        ] = SENTINEL,
        webhook_metadata: Union[
            BodySpeechToTextV1SpeechToTextPostWebhookMetadata, None
        ] = SENTINEL,
        entity_detection: Union[
            BodySpeechToTextV1SpeechToTextPostEntityDetection, None
        ] = SENTINEL,
        no_verbatim: Optional[bool] = SENTINEL,
        use_speaker_library: Optional[bool] = SENTINEL,
        detect_speaker_roles: Optional[bool] = SENTINEL,
        entity_redaction: Union[
            BodySpeechToTextV1SpeechToTextPostEntityRedaction, None
        ] = SENTINEL,
        entity_redaction_mode: Optional[str] = SENTINEL,
        keyterms: Optional[List[str]] = SENTINEL,
        token: Union[str, None] = SENTINEL,
        enable_logging: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Union[SpeechToTextConvertResponse, Any]]:
        data = await AsyncSpeechToTextClient.convert(
            self._client,
            model_id=model_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "language_code": language_code,
                        "tag_audio_events": tag_audio_events,
                        "num_speakers": num_speakers,
                        "timestamps_granularity": timestamps_granularity,
                        "diarize": diarize,
                        "diarization_threshold": diarization_threshold,
                        "additional_formats": additional_formats,
                        "file_format": file_format,
                        "cloud_storage_url": cloud_storage_url,
                        "source_url": source_url,
                        "webhook": webhook,
                        "webhook_id": webhook_id,
                        "temperature": temperature,
                        "seed": seed,
                        "use_multi_channel": use_multi_channel,
                        "multichannel_output_style": multichannel_output_style,
                        "webhook_metadata": webhook_metadata,
                        "entity_detection": entity_detection,
                        "no_verbatim": no_verbatim,
                        "use_speaker_library": use_speaker_library,
                        "detect_speaker_roles": detect_speaker_roles,
                        "entity_redaction": entity_redaction,
                        "entity_redaction_mode": entity_redaction_mode,
                        "keyterms": keyterms,
                        "token": token,
                        "enable_logging": enable_logging,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
