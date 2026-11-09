from __future__ import annotations
import typing
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .quality_preset_type import QualityPresetType
from .podcast_conversation_mode import PodcastConversationMode
from .podcast_bulletin_mode import PodcastBulletinMode
from .podcast_text_source import PodcastTextSource
from .podcast_url_source import PodcastUrlSource


# fernMode variant type for a shared-component member of BodyCreatePodcastV1StudioPodcastsPostMode
class BodyCreatePodcastV1StudioPodcastsPostMode_Conversation(PodcastConversationMode):
    pass


# fernMode variant type for a shared-component member of BodyCreatePodcastV1StudioPodcastsPostMode
class BodyCreatePodcastV1StudioPodcastsPostMode_Bulletin(PodcastBulletinMode):
    pass


# Union type for BodyCreatePodcastV1StudioPodcastsPostMode
# Pydantic will attempt to validate against each type in order
BodyCreatePodcastV1StudioPodcastsPostMode = Union[
    PodcastConversationMode, PodcastBulletinMode
]
# TypeAdapter for runtime validation of BodyCreatePodcastV1StudioPodcastsPostMode
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodyCreatePodcastV1StudioPodcastsPostMode_adapter = TypeAdapter(
    BodyCreatePodcastV1StudioPodcastsPostMode
)


# fernMode variant type for a shared-component member of SourceTwoItem
class SourceTwoItem_Text(PodcastTextSource):
    pass


# fernMode variant type for a shared-component member of SourceTwoItem
class SourceTwoItem_Url(PodcastUrlSource):
    pass


# Union type for SourceTwoItem
# Pydantic will attempt to validate against each type in order
SourceTwoItem = Union[PodcastTextSource, PodcastUrlSource]
# TypeAdapter for runtime validation of SourceTwoItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

SourceTwoItem_adapter = TypeAdapter(SourceTwoItem)


# Union type for BodyCreatePodcastV1StudioPodcastsPostSource
# Pydantic will attempt to validate against each type in order
BodyCreatePodcastV1StudioPodcastsPostSource = Union[
    PodcastTextSource, PodcastUrlSource, List[SourceTwoItem]
]
# TypeAdapter for runtime validation of BodyCreatePodcastV1StudioPodcastsPostSource
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodyCreatePodcastV1StudioPodcastsPostSource_adapter = TypeAdapter(
    BodyCreatePodcastV1StudioPodcastsPostSource
)


BodyCreatePodcastV1StudioPodcastsPostDurationScale = typing.Union[
    typing.Literal["short", "default", "long"], typing.Any
]

BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization = typing.Union[
    typing.Literal["auto", "on", "off", "apply_english"], typing.Any
]


class BodyCreatePodcastV1StudioPodcastsPost(BaseModel):
    """BodyCreatePodcastV1StudioPodcastsPost

    :param model_id: The ID of the model to be used for this Studio project, you can query GET /v1/models to list all available models.
    :type model_id: str
    :param mode: The type of podcast to generate. Can be 'conversation', an interaction between two voices, or 'bulletin', a monologue.
    :type mode: BodyCreatePodcastV1StudioPodcastsPostMode
    :param source: The source content for the Podcast.
    :type source: BodyCreatePodcastV1StudioPodcastsPostSource
    :param quality_preset: quality_preset, defaults to None
    :type quality_preset: QualityPresetType, optional
    :param duration_scale: Duration of the generated podcast. Must be one of: short - produces podcasts shorter than 3 minutes. default - produces podcasts roughly between 3-7 minutes. long - produces podcasts longer than 7 minutes., defaults to None
    :type duration_scale: BodyCreatePodcastV1StudioPodcastsPostDurationScale, optional
    :param language: An optional language of the Studio project. Two-letter language code (ISO 639-1)., defaults to None
    :type language: str, optional
    :param intro: The intro text that will always be added to the beginning of the podcast., defaults to None
    :type intro: str, optional
    :param outro: The outro text that will always be added to the end of the podcast., defaults to None
    :type outro: str, optional
    :param instructions_prompt: Additional instructions prompt for the podcast generation used to adjust the podcast's style and tone., defaults to None
    :type instructions_prompt: str, optional
    :param highlights: A brief summary or highlights of the Studio project's content, providing key points or themes. This should be between 10 and 70 characters., defaults to None
    :type highlights: List[str], optional
    :param callback_url: A url that will be called by our service when the Studio project is converted. Request will contain a json blob containing the status of the conversion Messages: 1. When project was converted successfully: { type: "project_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", conversion_status: "success", project_snapshot_id: "22m00Tcm4TlvDq8ikMAT", error_details: None, } } 2. When project conversion failed: { type: "project_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", conversion_status: "error", project_snapshot_id: None, error_details: "Error details if conversion failed" } } 3. When chapter was converted successfully: { type: "chapter_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", chapter_id: "22m00Tcm4TlvDq8ikMAT", conversion_status: "success", chapter_snapshot_id: "23m00Tcm4TlvDq8ikMAV", error_details: None, } } 4. When chapter conversion failed: { type: "chapter_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", chapter_id: "22m00Tcm4TlvDq8ikMAT", conversion_status: "error", chapter_snapshot_id: None, error_details: "Error details if conversion failed" } }, defaults to None
    :type callback_url: str, optional
    :param apply_text_normalization: This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English., defaults to None
    :type apply_text_normalization: BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization, optional
    """

    model_id: str = Field(
        description="The ID of the model to be used for this Studio project, you can query GET /v1/models to list all available models."
    )
    mode: BodyCreatePodcastV1StudioPodcastsPostMode = Field(
        description="The type of podcast to generate. Can be 'conversation', an interaction between two voices, or 'bulletin', a monologue."
    )
    source: BodyCreatePodcastV1StudioPodcastsPostSource = Field(
        description="The source content for the Podcast."
    )
    quality_preset: Optional[QualityPresetType] = Field(default=None)
    duration_scale: Optional[BodyCreatePodcastV1StudioPodcastsPostDurationScale] = (
        Field(
            default=None,
            description="Duration of the generated podcast. Must be one of: short - produces podcasts shorter than 3 minutes. default - produces podcasts roughly between 3-7 minutes. long - produces podcasts longer than 7 minutes.",
        )
    )
    language: Optional[str] = Field(
        default=None,
        description="An optional language of the Studio project. Two-letter language code (ISO 639-1).",
    )
    intro: Optional[str] = Field(
        default=None,
        description="The intro text that will always be added to the beginning of the podcast.",
    )
    outro: Optional[str] = Field(
        default=None,
        description="The outro text that will always be added to the end of the podcast.",
    )
    instructions_prompt: Optional[str] = Field(
        default=None,
        description="Additional instructions prompt for the podcast generation used to adjust the podcast's style and tone.",
    )
    highlights: Optional[List[str]] = Field(
        default=None,
        description="A brief summary or highlights of the Studio project's content, providing key points or themes. This should be between 10 and 70 characters.",
    )
    callback_url: Optional[str] = Field(
        default=None,
        description='A url that will be called by our service when the Studio project is converted. Request will contain a json blob containing the status of the conversion Messages: 1. When project was converted successfully: { type: "project_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", conversion_status: "success", project_snapshot_id: "22m00Tcm4TlvDq8ikMAT", error_details: None, } } 2. When project conversion failed: { type: "project_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", conversion_status: "error", project_snapshot_id: None, error_details: "Error details if conversion failed" } } 3. When chapter was converted successfully: { type: "chapter_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", chapter_id: "22m00Tcm4TlvDq8ikMAT", conversion_status: "success", chapter_snapshot_id: "23m00Tcm4TlvDq8ikMAV", error_details: None, } } 4. When chapter conversion failed: { type: "chapter_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", chapter_id: "22m00Tcm4TlvDq8ikMAT", conversion_status: "error", chapter_snapshot_id: None, error_details: "Error details if conversion failed" } }',
    )
    apply_text_normalization: Optional[
        BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization
    ] = Field(
        default=None,
        description="This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English.",
    )
