from __future__ import annotations
import typing
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .export_options import ExportOptions, ExportOptions_adapter
from .segmented_json_export_options import SegmentedJsonExportOptions
from .docx_export_options import DocxExportOptions
from .pdf_export_options import PdfExportOptions
from .txt_export_options import TxtExportOptions
from .html_export_options import HtmlExportOptions
from .srt_export_options import SrtExportOptions

BodySpeechToTextV1SpeechToTextPostModelId = typing.Union[
    typing.Literal["scribe_v2", "scribe_v1"], typing.Any
]

BodySpeechToTextV1SpeechToTextPostTimestampsGranularity = typing.Union[
    typing.Literal["none", "word", "character"], typing.Any
]

BodySpeechToTextV1SpeechToTextPostFileFormat = typing.Union[
    typing.Literal["pcm_s16le_16", "other"], typing.Any
]

BodySpeechToTextV1SpeechToTextPostMultichannelOutputStyle = typing.Union[
    typing.Literal["separate", "combined"], typing.Any
]

# Union type for BodySpeechToTextV1SpeechToTextPostWebhookMetadata
# Pydantic will attempt to validate against each type in order
BodySpeechToTextV1SpeechToTextPostWebhookMetadata = Union[str, Dict[str, Any]]
# TypeAdapter for runtime validation of BodySpeechToTextV1SpeechToTextPostWebhookMetadata
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodySpeechToTextV1SpeechToTextPostWebhookMetadata_adapter = TypeAdapter(
    BodySpeechToTextV1SpeechToTextPostWebhookMetadata
)


# Union type for BodySpeechToTextV1SpeechToTextPostEntityDetection
# Pydantic will attempt to validate against each type in order
BodySpeechToTextV1SpeechToTextPostEntityDetection = Union[str, List[str]]
# TypeAdapter for runtime validation of BodySpeechToTextV1SpeechToTextPostEntityDetection
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodySpeechToTextV1SpeechToTextPostEntityDetection_adapter = TypeAdapter(
    BodySpeechToTextV1SpeechToTextPostEntityDetection
)


# Union type for BodySpeechToTextV1SpeechToTextPostEntityRedaction
# Pydantic will attempt to validate against each type in order
BodySpeechToTextV1SpeechToTextPostEntityRedaction = Union[str, List[str]]
# TypeAdapter for runtime validation of BodySpeechToTextV1SpeechToTextPostEntityRedaction
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodySpeechToTextV1SpeechToTextPostEntityRedaction_adapter = TypeAdapter(
    BodySpeechToTextV1SpeechToTextPostEntityRedaction
)


class BodySpeechToTextV1SpeechToTextPost(BaseModel):
    """BodySpeechToTextV1SpeechToTextPost

    :param model_id: The ID of the model to use for transcription.
    :type model_id: BodySpeechToTextV1SpeechToTextPostModelId
    :param file: The file to transcribe (100ms minimum audio length). All major audio and video formats are supported. Exactly one of the file or cloud_storage_url parameters must be provided. The file size must be less than 5.0GB., defaults to None
    :type file: bytes, optional
    :param language_code: An ISO-639-1 or ISO-639-3 language_code corresponding to the language of the audio file. Can sometimes improve transcription performance if known beforehand. Defaults to null, in this case the language is predicted automatically., defaults to None
    :type language_code: str, optional
    :param tag_audio_events: Whether to tag audio events like (laughter), (footsteps), etc. in the transcription., defaults to None
    :type tag_audio_events: bool, optional
    :param num_speakers: The maximum amount of speakers talking in the uploaded file. Can help with predicting who speaks when. The maximum amount of speakers that can be predicted is 32. Defaults to null, in this case the amount of speakers is set to the maximum value the model supports., defaults to None
    :type num_speakers: int, optional
    :param timestamps_granularity: The granularity of the timestamps in the transcription. 'word' provides word-level timestamps and 'character' provides character-level timestamps per word., defaults to None
    :type timestamps_granularity: BodySpeechToTextV1SpeechToTextPostTimestampsGranularity, optional
    :param diarize: Whether to annotate which speaker is currently talking in the uploaded file., defaults to None
    :type diarize: bool, optional
    :param diarization_threshold: Diarization threshold to apply during speaker diarization. A higher value means there will be a lower chance of one speaker being diarized as two different speakers but also a higher chance of two different speakers being diarized as one speaker (less total speakers predicted). A low value means there will be a higher chance of one speaker being diarized as two different speakers but also a lower chance of two different speakers being diarized as one speaker (more total speakers predicted). Can only be set when diarize=True and num_speakers=None. Defaults to None, in which case we will choose a threshold based on the model_id (0.22 usually)., defaults to None
    :type diarization_threshold: float, optional
    :param additional_formats: additional_formats, defaults to None
    :type additional_formats: List[ExportOptions], optional
    :param file_format: The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform., defaults to None
    :type file_format: BodySpeechToTextV1SpeechToTextPostFileFormat, optional
    :param cloud_storage_url: [Deprecated] This parameter is deprecated and will be removed in the future. Use 'source_url' instead.The HTTPS URL of the file to transcribe. Exactly one of the file or cloud_storage_url parameters must be provided. The file must be accessible via HTTPS and the file size must be less than 2GB. Any valid HTTPS URL is accepted, including URLs from cloud storage providers (AWS S3, Google Cloud Storage, Cloudflare R2, etc.), CDNs, or any other HTTPS source. URLs can be pre-signed or include authentication tokens in query parameters., defaults to None
    :type cloud_storage_url: str, optional
    :param source_url: The URL of an audio or video file to transcribe. Supports hosted video or audio files, YouTube video URLs, TikTok video URLs, and other video hosting services., defaults to None
    :type source_url: str, optional
    :param webhook: Whether to send the transcription result to configured speech-to-text webhooks. If set the request will return early without the transcription, which will be delivered later via webhook., defaults to None
    :type webhook: bool, optional
    :param webhook_id: Optional specific webhook ID to send the transcription result to. Only valid when webhook is set to true. If not provided, transcription will be sent to all configured speech-to-text webhooks., defaults to None
    :type webhook_id: str, optional
    :param temperature: Controls the randomness of the transcription output. Accepts values between 0.0 and 2.0, where higher values result in more diverse and less deterministic results. If omitted, we will use a temperature based on the model you selected which is usually 0., defaults to None
    :type temperature: float, optional
    :param seed: If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be an integer between 0 and 2147483647., defaults to None
    :type seed: int, optional
    :param use_multi_channel: Whether the audio file contains multiple channels where each channel contains a single speaker. When enabled, each channel is transcribed independently. By default a separate transcript is returned per channel; set multichannel_output_style='combined' to instead receive a single transcript with all channels merged and sorted by time. Each word in the response includes a 'channel_index' field indicating which channel it was spoken on. A maximum of 5 channels is supported. Each channel is billed independently at the full audio duration, so cost scales linearly with the number of channels., defaults to None
    :type use_multi_channel: bool, optional
    :param multichannel_output_style: Controls the response shape when use_multi_channel is enabled. 'separate' (default) returns one transcript per channel under 'transcripts'. 'combined' merges all channels into a single transcript whose words are sorted by start time, each carrying a 'channel_index' - matching the single-channel response shape. 'combined' requires timestamps (timestamps_granularity must not be 'none') and does not support entity detection or redaction., defaults to None
    :type multichannel_output_style: BodySpeechToTextV1SpeechToTextPostMultichannelOutputStyle, optional
    :param webhook_metadata: Optional metadata to be included in the webhook response. This should be a JSON string representing an object with a maximum depth of 2 levels and maximum size of 16KB. Useful for tracking internal IDs, job references, or other contextual information., defaults to None
    :type webhook_metadata: BodySpeechToTextV1SpeechToTextPostWebhookMetadata, optional
    :param entity_detection: Detect entities in the transcript. Can be 'all' to detect all entities, a single entity type or category string, or a list of entity types/categories. Categories include 'pii', 'phi', 'pci', 'other', 'offensive_language'. When enabled, detected entities will be returned in the 'entities' field with their text, type, and character positions. Usage of this parameter will incur an additional 30% surcharge on the base transcription cost., defaults to None
    :type entity_detection: BodySpeechToTextV1SpeechToTextPostEntityDetection, optional
    :param no_verbatim: If true, the transcription will not have any filler words, false starts and non-speech sounds. Only supported with scribe_v2 model., defaults to None
    :type no_verbatim: bool, optional
    :param use_speaker_library: Whether to use the speaker library for identifying known speakers during diarization. When enabled and diarize is true, detected speakers will be matched against registered speakers in the workspace's speaker library., defaults to None
    :type use_speaker_library: bool, optional
    :param detect_speaker_roles: Whether to detect speaker roles (agent vs customer). Requires diarize=true. Cannot be used with use_multi_channel=true. When enabled, speaker_id values will be 'agent' and 'customer' instead of 'speaker_0', 'speaker_1', etc. Usage incurs an additional 10% surcharge on base transcription cost., defaults to None
    :type detect_speaker_roles: bool, optional
    :param entity_redaction: Redact entities from the transcript text. Accepts the same format as entity_detection: 'all', a category ('pii', 'phi'), or specific entity types. Must be a subset of entity_detection. When redaction is enabled, the entities field will not be returned. Usage of this parameter will incur an additional 30% surcharge on the base transcription cost., defaults to None
    :type entity_redaction: BodySpeechToTextV1SpeechToTextPostEntityRedaction, optional
    :param entity_redaction_mode: How to format redacted entities. 'redacted' replaces with {REDACTED}, 'entity_type' replaces with {ENTITY_TYPE}, 'enumerated_entity_type' replaces with {ENTITY_TYPE_N} where N enumerates each occurrence. Only used when entity_redaction is set., defaults to None
    :type entity_redaction_mode: str, optional
    :param keyterms: A list of keyterms to bias the transcription towards. The keyterms are words or phrases you want the model to recognise more accurately. The number of keyterms cannot exceed 1000. The length of each keyterm must be less than 50 characters. Keyterms can contain at most 5 words (after normalisation). For example ["hello", "world", "technical term"]. The following characters are not supported: `<`, `>`, `{`, `}`, `[`, `]`, `\\`. Usage of this parameter will incur an additional 20% surcharge on the base transcription cost. When more than 100 keyterms are provided, a minimum billable duration of 20 seconds applies per request., defaults to None
    :type keyterms: List[str], optional
    """

    model_id: BodySpeechToTextV1SpeechToTextPostModelId = Field(
        description="The ID of the model to use for transcription."
    )
    file: Optional[bytes] = Field(
        default=None,
        description="The file to transcribe (100ms minimum audio length). All major audio and video formats are supported. Exactly one of the file or cloud_storage_url parameters must be provided. The file size must be less than 5.0GB.",
    )
    language_code: Optional[str] = Field(
        default=None,
        description="An ISO-639-1 or ISO-639-3 language_code corresponding to the language of the audio file. Can sometimes improve transcription performance if known beforehand. Defaults to null, in this case the language is predicted automatically.",
    )
    tag_audio_events: Optional[bool] = Field(
        default=None,
        description="Whether to tag audio events like (laughter), (footsteps), etc. in the transcription.",
    )
    num_speakers: Optional[int] = Field(
        default=None,
        description="The maximum amount of speakers talking in the uploaded file. Can help with predicting who speaks when. The maximum amount of speakers that can be predicted is 32. Defaults to null, in this case the amount of speakers is set to the maximum value the model supports.",
    )
    timestamps_granularity: Optional[
        BodySpeechToTextV1SpeechToTextPostTimestampsGranularity
    ] = Field(
        default=None,
        description="The granularity of the timestamps in the transcription. 'word' provides word-level timestamps and 'character' provides character-level timestamps per word.",
    )
    diarize: Optional[bool] = Field(
        default=None,
        description="Whether to annotate which speaker is currently talking in the uploaded file.",
    )
    diarization_threshold: Optional[float] = Field(
        default=None,
        description="Diarization threshold to apply during speaker diarization. A higher value means there will be a lower chance of one speaker being diarized as two different speakers but also a higher chance of two different speakers being diarized as one speaker (less total speakers predicted). A low value means there will be a higher chance of one speaker being diarized as two different speakers but also a lower chance of two different speakers being diarized as one speaker (more total speakers predicted). Can only be set when diarize=True and num_speakers=None. Defaults to None, in which case we will choose a threshold based on the model_id (0.22 usually).",
    )
    additional_formats: Optional[List[ExportOptions]] = Field(default=None)
    file_format: Optional[BodySpeechToTextV1SpeechToTextPostFileFormat] = Field(
        default=None,
        description="The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform.",
    )
    cloud_storage_url: Optional[str] = Field(
        default=None,
        description="[Deprecated] This parameter is deprecated and will be removed in the future. Use 'source_url' instead.The HTTPS URL of the file to transcribe. Exactly one of the file or cloud_storage_url parameters must be provided. The file must be accessible via HTTPS and the file size must be less than 2GB. Any valid HTTPS URL is accepted, including URLs from cloud storage providers (AWS S3, Google Cloud Storage, Cloudflare R2, etc.), CDNs, or any other HTTPS source. URLs can be pre-signed or include authentication tokens in query parameters.",
    )
    source_url: Optional[str] = Field(
        default=None,
        description="The URL of an audio or video file to transcribe. Supports hosted video or audio files, YouTube video URLs, TikTok video URLs, and other video hosting services.",
    )
    webhook: Optional[bool] = Field(
        default=None,
        description="Whether to send the transcription result to configured speech-to-text webhooks. If set the request will return early without the transcription, which will be delivered later via webhook.",
    )
    webhook_id: Optional[str] = Field(
        default=None,
        description="Optional specific webhook ID to send the transcription result to. Only valid when webhook is set to true. If not provided, transcription will be sent to all configured speech-to-text webhooks.",
    )
    temperature: Optional[float] = Field(
        default=None,
        description="Controls the randomness of the transcription output. Accepts values between 0.0 and 2.0, where higher values result in more diverse and less deterministic results. If omitted, we will use a temperature based on the model you selected which is usually 0.",
    )
    seed: Optional[int] = Field(
        default=None,
        description="If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be an integer between 0 and 2147483647.",
    )
    use_multi_channel: Optional[bool] = Field(
        default=None,
        description="Whether the audio file contains multiple channels where each channel contains a single speaker. When enabled, each channel is transcribed independently. By default a separate transcript is returned per channel; set multichannel_output_style='combined' to instead receive a single transcript with all channels merged and sorted by time. Each word in the response includes a 'channel_index' field indicating which channel it was spoken on. A maximum of 5 channels is supported. Each channel is billed independently at the full audio duration, so cost scales linearly with the number of channels.",
    )
    multichannel_output_style: Optional[
        BodySpeechToTextV1SpeechToTextPostMultichannelOutputStyle
    ] = Field(
        default=None,
        description="Controls the response shape when use_multi_channel is enabled. 'separate' (default) returns one transcript per channel under 'transcripts'. 'combined' merges all channels into a single transcript whose words are sorted by start time, each carrying a 'channel_index' - matching the single-channel response shape. 'combined' requires timestamps (timestamps_granularity must not be 'none') and does not support entity detection or redaction.",
    )
    webhook_metadata: Optional[BodySpeechToTextV1SpeechToTextPostWebhookMetadata] = (
        Field(
            default=None,
            description="Optional metadata to be included in the webhook response. This should be a JSON string representing an object with a maximum depth of 2 levels and maximum size of 16KB. Useful for tracking internal IDs, job references, or other contextual information.",
        )
    )
    entity_detection: Optional[BodySpeechToTextV1SpeechToTextPostEntityDetection] = (
        Field(
            default=None,
            description="Detect entities in the transcript. Can be 'all' to detect all entities, a single entity type or category string, or a list of entity types/categories. Categories include 'pii', 'phi', 'pci', 'other', 'offensive_language'. When enabled, detected entities will be returned in the 'entities' field with their text, type, and character positions. Usage of this parameter will incur an additional 30% surcharge on the base transcription cost.",
        )
    )
    no_verbatim: Optional[bool] = Field(
        default=None,
        description="If true, the transcription will not have any filler words, false starts and non-speech sounds. Only supported with scribe_v2 model.",
    )
    use_speaker_library: Optional[bool] = Field(
        default=None,
        description="Whether to use the speaker library for identifying known speakers during diarization. When enabled and diarize is true, detected speakers will be matched against registered speakers in the workspace's speaker library.",
    )
    detect_speaker_roles: Optional[bool] = Field(
        default=None,
        description="Whether to detect speaker roles (agent vs customer). Requires diarize=true. Cannot be used with use_multi_channel=true. When enabled, speaker_id values will be 'agent' and 'customer' instead of 'speaker_0', 'speaker_1', etc. Usage incurs an additional 10% surcharge on base transcription cost.",
    )
    entity_redaction: Optional[BodySpeechToTextV1SpeechToTextPostEntityRedaction] = (
        Field(
            default=None,
            description="Redact entities from the transcript text. Accepts the same format as entity_detection: 'all', a category ('pii', 'phi'), or specific entity types. Must be a subset of entity_detection. When redaction is enabled, the entities field will not be returned. Usage of this parameter will incur an additional 30% surcharge on the base transcription cost.",
        )
    )
    entity_redaction_mode: Optional[str] = Field(
        default=None,
        description="How to format redacted entities. 'redacted' replaces with {REDACTED}, 'entity_type' replaces with {ENTITY_TYPE}, 'enumerated_entity_type' replaces with {ENTITY_TYPE_N} where N enumerates each occurrence. Only used when entity_redaction is set.",
    )
    keyterms: Optional[List[str]] = Field(
        default=None,
        description='A list of keyterms to bias the transcription towards. The keyterms are words or phrases you want the model to recognise more accurately. The number of keyterms cannot exceed 1000. The length of each keyterm must be less than 50 characters. Keyterms can contain at most 5 words (after normalisation). For example ["hello", "world", "technical term"]. The following characters are not supported: `<`, `>`, `{`, `}`, `[`, `]`, `\\`. Usage of this parameter will incur an additional 20% surcharge on the base transcription cost. When more than 100 keyterms are provided, a minimum billable duration of 20 seconds applies per request.',
    )
