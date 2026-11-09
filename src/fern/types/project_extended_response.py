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
from .project_creation_meta_response_model import ProjectCreationMetaResponseModel
from .caption_style_model import CaptionStyleModel
from .studio_agent_settings_model import StudioAgentSettingsModel
from .quality_preset_type import QualityPresetType
from .chapter_response import ChapterResponse
from .pronunciation_dictionary_version_response_model import (
    PronunciationDictionaryVersionResponseModel,
)
from .pronunciation_dictionary_locator_response_model import (
    PronunciationDictionaryLocatorResponseModel,
)
from .project_voice_response_model import ProjectVoiceResponseModel
from .voice import Voice
from .direct_publishing_read_response_model import DirectPublishingReadResponseModel
from .project_video_response_model import ProjectVideoResponseModel
from .project_external_audio_response_model import ProjectExternalAudioResponseModel
from .project_image_response_model import ProjectImageResponseModel

ProjectExtendedResponseTargetAudience = typing.Union[
    typing.Literal["children", "young adult", "adult", "all ages"], typing.Any
]

ProjectState = typing.Union[
    typing.Literal["creating", "default", "converting", "in_queue"], typing.Any
]

ProjectExtendedResponseAccessLevel = typing.Union[
    typing.Literal["admin", "editor", "commenter", "viewer"], typing.Any
]

ProjectExtendedResponseFiction = typing.Union[
    typing.Literal["fiction", "non-fiction"], typing.Any
]

ProjectExtendedResponseSourceType = typing.Union[
    typing.Literal["blank", "book", "article", "genfm", "video", "screenplay"],
    typing.Any,
]

ProjectExtendedResponseAspectRatio = typing.Union[
    typing.Literal["16:9", "9:16", "4:5", "1:1"], typing.Any
]

ProjectExtendedResponseApplyTextNormalization = typing.Union[
    typing.Literal["auto", "on", "off", "apply_english"], typing.Any
]


# fernMode variant type for a shared-component member of ProjectExtendedResponseAssetsItem
class ProjectExtendedResponseAssetsItem_Video(ProjectVideoResponseModel):
    pass


# fernMode variant type for a shared-component member of ProjectExtendedResponseAssetsItem
class ProjectExtendedResponseAssetsItem_Audio(ProjectExternalAudioResponseModel):
    pass


# fernMode variant type for a shared-component member of ProjectExtendedResponseAssetsItem
class ProjectExtendedResponseAssetsItem_Image(ProjectImageResponseModel):
    pass


# Union type for ProjectExtendedResponseAssetsItem
# Pydantic will attempt to validate against each type in order
ProjectExtendedResponseAssetsItem = Union[
    ProjectVideoResponseModel,
    ProjectExternalAudioResponseModel,
    ProjectImageResponseModel,
]
# TypeAdapter for runtime validation of ProjectExtendedResponseAssetsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ProjectExtendedResponseAssetsItem_adapter = TypeAdapter(
    ProjectExtendedResponseAssetsItem
)


class ProjectExtendedResponse(BaseModel):
    """ProjectExtendedResponse

    :param project_id: The ID of the project.
    :type project_id: str
    :param name: The name of the project.
    :type name: str
    :param create_date_unix: The creation date of the project.
    :type create_date_unix: int
    :param created_by_user_id: The user ID who created the project.
    :type created_by_user_id: str
    :param default_title_voice_ref_id: The default title project voice reference ID.
    :type default_title_voice_ref_id: str
    :param default_paragraph_voice_ref_id: The default paragraph project voice reference ID.
    :type default_paragraph_voice_ref_id: str
    :param default_model_id: The default model ID.
    :type default_model_id: str
    :param last_conversion_date_unix: The last conversion date of the project., defaults to None
    :type last_conversion_date_unix: int, optional
    :param can_be_downloaded: Whether the project can be downloaded.
    :type can_be_downloaded: bool
    :param title: The title of the project., defaults to None
    :type title: str, optional
    :param author: The author of the project., defaults to None
    :type author: str, optional
    :param description: The description of the project., defaults to None
    :type description: str, optional
    :param genres: List of genres of the project., defaults to None
    :type genres: List[str], optional
    :param cover_image_url: The cover image URL of the project., defaults to None
    :type cover_image_url: str, optional
    :param target_audience: The target audience of the project., defaults to None
    :type target_audience: ProjectExtendedResponseTargetAudience, optional
    :param language: Two-letter language code (ISO 639-1) of the language of the project., defaults to None
    :type language: str, optional
    :param content_type: The content type of the project, e.g. 'Novel' or 'Short Story', defaults to None
    :type content_type: str, optional
    :param original_publication_date: The original publication date of the project., defaults to None
    :type original_publication_date: str, optional
    :param mature_content: Whether the project contains mature content., defaults to None
    :type mature_content: bool, optional
    :param isbn_number: The ISBN number of the project., defaults to None
    :type isbn_number: str, optional
    :param volume_normalization: Whether the project uses volume normalization.
    :type volume_normalization: bool
    :param state: The state of the project.
    :type state: ProjectState
    :param access_level: The access level of the project.
    :type access_level: ProjectExtendedResponseAccessLevel
    :param fiction: Whether the project is fiction., defaults to None
    :type fiction: ProjectExtendedResponseFiction, optional
    :param quality_check_on: Whether quality check is enabled for this project.
    :type quality_check_on: bool
    :param quality_check_on_when_bulk_convert: Whether quality check is enabled on the project when bulk converting.
    :type quality_check_on_when_bulk_convert: bool
    :param creation_meta: The creation meta of the project., defaults to None
    :type creation_meta: ProjectCreationMetaResponseModel, optional
    :param source_type: The source type of the project., defaults to None
    :type source_type: ProjectExtendedResponseSourceType, optional
    :param chapters_enabled: Whether chapters are enabled for the project., defaults to None
    :type chapters_enabled: bool, optional
    :param captions_enabled: Whether captions are enabled for the project., defaults to None
    :type captions_enabled: bool, optional
    :param caption_style: Global styling to be applied to all captions, defaults to None
    :type caption_style: CaptionStyleModel, optional
    :param caption_style_template_overrides: Styling changes that have been made to the provided templates, defaults to None
    :type caption_style_template_overrides: Dict[str, CaptionStyleModel], optional
    :param public_share_id: The public share ID of the project., defaults to None
    :type public_share_id: str, optional
    :param aspect_ratio: The aspect ratio of the project., defaults to None
    :type aspect_ratio: ProjectExtendedResponseAspectRatio, optional
    :param agent_settings: Agent-related settings for the project, defaults to None
    :type agent_settings: StudioAgentSettingsModel, optional
    :param quality_preset: quality_preset
    :type quality_preset: QualityPresetType
    :param chapters: List of chapters of the project and their metadata.
    :type chapters: List[ChapterResponse]
    :param pronunciation_dictionary_versions: List of pronunciation dictionary versions of the project and their metadata.
    :type pronunciation_dictionary_versions: List[PronunciationDictionaryVersionResponseModel]
    :param pronunciation_dictionary_locators: List of pronunciation dictionary locators.
    :type pronunciation_dictionary_locators: List[PronunciationDictionaryLocatorResponseModel]
    :param apply_text_normalization: Whether text normalization is applied to the project.
    :type apply_text_normalization: ProjectExtendedResponseApplyTextNormalization
    :param experimental: Experimental features for the project., defaults to None
    :type experimental: Dict[str, Any], optional
    :param assets: List of uploaded assets e.g. videos, audios.
    :type assets: List[ProjectExtendedResponseAssetsItem]
    :param voices: List of configured project voices.
    :type voices: List[ProjectVoiceResponseModel]
    :param base_voices: List of voices used by the project., defaults to None
    :type base_voices: List[Voice], optional
    :param publishing_read: The ElevenReader data if the book was published., defaults to None
    :type publishing_read: DirectPublishingReadResponseModel, optional
    :param default_title_voice_id: The default title voice ID., defaults to None
    :type default_title_voice_id: str, optional
    :param default_paragraph_voice_id: The default paragraph voice ID., defaults to None
    :type default_paragraph_voice_id: str, optional
    """

    project_id: str = Field(description="The ID of the project.")
    name: str = Field(description="The name of the project.")
    create_date_unix: int = Field(description="The creation date of the project.")
    created_by_user_id: Optional[str] = Field(
        description="The user ID who created the project."
    )
    default_title_voice_ref_id: str = Field(
        description="The default title project voice reference ID."
    )
    default_paragraph_voice_ref_id: str = Field(
        description="The default paragraph project voice reference ID."
    )
    default_model_id: str = Field(description="The default model ID.")
    last_conversion_date_unix: Optional[int] = Field(
        default=None, description="The last conversion date of the project."
    )
    can_be_downloaded: bool = Field(
        description="Whether the project can be downloaded."
    )
    title: Optional[str] = Field(default=None, description="The title of the project.")
    author: Optional[str] = Field(
        default=None, description="The author of the project."
    )
    description: Optional[str] = Field(
        default=None, description="The description of the project."
    )
    genres: Optional[List[str]] = Field(
        default=None, description="List of genres of the project."
    )
    cover_image_url: Optional[str] = Field(
        default=None, description="The cover image URL of the project."
    )
    target_audience: Optional[ProjectExtendedResponseTargetAudience] = Field(
        default=None, description="The target audience of the project."
    )
    language: Optional[str] = Field(
        default=None,
        description="Two-letter language code (ISO 639-1) of the language of the project.",
    )
    content_type: Optional[str] = Field(
        default=None,
        description="The content type of the project, e.g. 'Novel' or 'Short Story'",
    )
    original_publication_date: Optional[str] = Field(
        default=None, description="The original publication date of the project."
    )
    mature_content: Optional[bool] = Field(
        default=None, description="Whether the project contains mature content."
    )
    isbn_number: Optional[str] = Field(
        default=None, description="The ISBN number of the project."
    )
    volume_normalization: bool = Field(
        description="Whether the project uses volume normalization."
    )
    state: ProjectState = Field(description="The state of the project.")
    access_level: ProjectExtendedResponseAccessLevel = Field(
        description="The access level of the project."
    )
    fiction: Optional[ProjectExtendedResponseFiction] = Field(
        default=None, description="Whether the project is fiction."
    )
    quality_check_on: bool = Field(
        description="Whether quality check is enabled for this project."
    )
    quality_check_on_when_bulk_convert: bool = Field(
        description="Whether quality check is enabled on the project when bulk converting."
    )
    creation_meta: Optional[ProjectCreationMetaResponseModel] = Field(
        default=None, description="The creation meta of the project."
    )
    source_type: Optional[ProjectExtendedResponseSourceType] = Field(
        default=None, description="The source type of the project."
    )
    chapters_enabled: Optional[bool] = Field(
        default=None, description="Whether chapters are enabled for the project."
    )
    captions_enabled: Optional[bool] = Field(
        default=None, description="Whether captions are enabled for the project."
    )
    caption_style: Optional[CaptionStyleModel] = Field(
        default=None, description="Global styling to be applied to all captions"
    )
    caption_style_template_overrides: Optional[Dict[str, CaptionStyleModel]] = Field(
        default=None,
        description="Styling changes that have been made to the provided templates",
    )
    public_share_id: Optional[str] = Field(
        default=None, description="The public share ID of the project."
    )
    aspect_ratio: Optional[ProjectExtendedResponseAspectRatio] = Field(
        default=None, description="The aspect ratio of the project."
    )
    agent_settings: Optional[StudioAgentSettingsModel] = Field(
        default=None, description="Agent-related settings for the project"
    )
    quality_preset: QualityPresetType
    chapters: List[ChapterResponse] = Field(
        description="List of chapters of the project and their metadata."
    )
    pronunciation_dictionary_versions: List[
        PronunciationDictionaryVersionResponseModel
    ] = Field(
        description="List of pronunciation dictionary versions of the project and their metadata."
    )
    pronunciation_dictionary_locators: List[
        PronunciationDictionaryLocatorResponseModel
    ] = Field(description="List of pronunciation dictionary locators.")
    apply_text_normalization: ProjectExtendedResponseApplyTextNormalization = Field(
        description="Whether text normalization is applied to the project."
    )
    experimental: Optional[Dict[str, Any]] = Field(
        default=None, description="Experimental features for the project."
    )
    assets: List[ProjectExtendedResponseAssetsItem] = Field(
        description="List of uploaded assets e.g. videos, audios."
    )
    voices: List[ProjectVoiceResponseModel] = Field(
        description="List of configured project voices."
    )
    base_voices: Optional[List[Voice]] = Field(
        default=None, description="List of voices used by the project."
    )
    publishing_read: Optional[DirectPublishingReadResponseModel] = Field(
        default=None, description="The ElevenReader data if the book was published."
    )
    default_title_voice_id: Optional[str] = Field(
        default=None, description="The default title voice ID."
    )
    default_paragraph_voice_id: Optional[str] = Field(
        default=None, description="The default paragraph voice ID."
    )
