from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .quality_preset_type import QualityPresetType

BodyCreateStudioProjectV1StudioProjectsPostTargetAudience = typing.Union[
    typing.Literal["children", "young adult", "adult", "all ages"], typing.Any
]

BodyCreateStudioProjectV1StudioProjectsPostFiction = typing.Union[
    typing.Literal["fiction", "non-fiction"], typing.Any
]

BodyCreateStudioProjectV1StudioProjectsPostApplyTextNormalization = typing.Union[
    typing.Literal["auto", "on", "off", "apply_english"], typing.Any
]

BodyCreateStudioProjectV1StudioProjectsPostSourceType = typing.Union[
    typing.Literal["blank", "book", "article", "genfm", "video", "screenplay"],
    typing.Any,
]


class BodyCreateStudioProjectV1StudioProjectsPost(BaseModel):
    """BodyCreateStudioProjectV1StudioProjectsPost

    :param name: The name of the Studio project, used for identification only.
    :type name: str
    :param default_title_voice_id: The voice_id that corresponds to the default voice used for new titles., defaults to None
    :type default_title_voice_id: str, optional
    :param default_paragraph_voice_id: The voice_id that corresponds to the default voice used for new paragraphs., defaults to None
    :type default_paragraph_voice_id: str, optional
    :param default_model_id: The ID of the model to be used for this Studio project, you can query GET /v1/models to list all available models., defaults to None
    :type default_model_id: str, optional
    :param from_url: An optional URL from which we will extract content to initialize the Studio project. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank., defaults to None
    :type from_url: str, optional
    :param from_document: An optional .epub, .pdf, .txt or similar file can be provided. If provided, we will initialize the Studio project with its content. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank., defaults to None
    :type from_document: bytes, optional
    :param from_content_json: An optional content to initialize the Studio project with. If this is set, 'from_url' and 'from_document' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank. Example: [{"name": "Chapter A", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "A", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "B", "type": "tts_node"}]}, {"sub_type": "h1", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "C", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "D", "type": "tts_node"}]}]}, {"name": "Chapter B", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "E", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "F", "type": "tts_node"}]}, {"sub_type": "h2", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "G", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "H", "type": "tts_node"}]}]}], defaults to None
    :type from_content_json: str, optional
    :param quality_preset: quality_preset, defaults to None
    :type quality_preset: QualityPresetType, optional
    :param title: An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download., defaults to None
    :type title: str, optional
    :param author: An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download., defaults to None
    :type author: str, optional
    :param description: An optional description of the Studio project., defaults to None
    :type description: str, optional
    :param genres: An optional list of genres associated with the Studio project., defaults to None
    :type genres: List[str], optional
    :param target_audience: An optional target audience of the Studio project., defaults to None
    :type target_audience: BodyCreateStudioProjectV1StudioProjectsPostTargetAudience, optional
    :param language: An optional language of the Studio project. Two-letter language code (ISO 639-1)., defaults to None
    :type language: str, optional
    :param content_type: An optional content type of the Studio project., defaults to None
    :type content_type: str, optional
    :param original_publication_date: An optional original publication date of the Studio project, in the format YYYY-MM-DD or YYYY., defaults to None
    :type original_publication_date: str, optional
    :param mature_content: An optional specification of whether this Studio project contains mature content., defaults to None
    :type mature_content: bool, optional
    :param isbn_number: An optional ISBN number of the Studio project you want to create, this will be added as metadata to the mp3 file on Studio project or chapter download., defaults to None
    :type isbn_number: str, optional
    :param acx_volume_normalization: [Deprecated] When the Studio project is downloaded, should the returned audio have postprocessing in order to make it compliant with audiobook normalized volume requirements, defaults to None
    :type acx_volume_normalization: bool, optional
    :param volume_normalization: When the Studio project is downloaded, should the returned audio have postprocessing in order to make it compliant with audiobook normalized volume requirements, defaults to None
    :type volume_normalization: bool, optional
    :param pronunciation_dictionary_locators: A list of pronunciation dictionary locators (pronunciation_dictionary_id, version_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"Vmd4Zor6fplcA7WrINey\\",\\"version_id\\":\\"hRPaxjlTdR7wFMhV4w0b\\"}"' --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"JzWtcGQMJ6bnlWwyMo7e\\",\\"version_id\\":\\"lbmwxiLu4q6txYxgdZqn\\"}"'., defaults to None
    :type pronunciation_dictionary_locators: List[str], optional
    :param callback_url: A url that will be called by our service when the Studio project is converted. Request will contain a json blob containing the status of the conversion Messages: 1. When project was converted successfully: { type: "project_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", conversion_status: "success", project_snapshot_id: "22m00Tcm4TlvDq8ikMAT", error_details: None, } } 2. When project conversion failed: { type: "project_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", conversion_status: "error", project_snapshot_id: None, error_details: "Error details if conversion failed" } } 3. When chapter was converted successfully: { type: "chapter_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", chapter_id: "22m00Tcm4TlvDq8ikMAT", conversion_status: "success", chapter_snapshot_id: "23m00Tcm4TlvDq8ikMAV", error_details: None, } } 4. When chapter conversion failed: { type: "chapter_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", chapter_id: "22m00Tcm4TlvDq8ikMAT", conversion_status: "error", chapter_snapshot_id: None, error_details: "Error details if conversion failed" } }, defaults to None
    :type callback_url: str, optional
    :param fiction: An optional specification of whether the content of this Studio project is fiction., defaults to None
    :type fiction: BodyCreateStudioProjectV1StudioProjectsPostFiction, optional
    :param apply_text_normalization: This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English., defaults to None
    :type apply_text_normalization: BodyCreateStudioProjectV1StudioProjectsPostApplyTextNormalization, optional
    :param auto_convert: Whether to auto convert the Studio project to audio or not., defaults to None
    :type auto_convert: bool, optional
    :param auto_assign_voices: [Alpha Feature] Whether automatically assign voices to phrases in the create Project., defaults to None
    :type auto_assign_voices: bool, optional
    :param source_type: The type of Studio project to create., defaults to None
    :type source_type: BodyCreateStudioProjectV1StudioProjectsPostSourceType, optional
    :param voice_settings: Optional voice settings overrides for the project, encoded as a list of JSON strings. Example: ["{\\"voice_id\\": \\"21m00Tcm4TlvDq8ikWAM\\", \\"stability\\": 0.7, \\"similarity_boost\\": 0.8, \\"style\\": 0.5, \\"speed\\": 1.0, \\"use_speaker_boost\\": true}"], defaults to None
    :type voice_settings: List[str], optional
    :param create_publishing_read: If true, creates a corresponding read for direct publishing in draft state, defaults to None
    :type create_publishing_read: bool, optional
    """

    name: str = Field(
        description="The name of the Studio project, used for identification only."
    )
    default_title_voice_id: Optional[str] = Field(
        default=None,
        description="The voice_id that corresponds to the default voice used for new titles.",
    )
    default_paragraph_voice_id: Optional[str] = Field(
        default=None,
        description="The voice_id that corresponds to the default voice used for new paragraphs.",
    )
    default_model_id: Optional[str] = Field(
        default=None,
        description="The ID of the model to be used for this Studio project, you can query GET /v1/models to list all available models.",
    )
    from_url: Optional[str] = Field(
        default=None,
        description="An optional URL from which we will extract content to initialize the Studio project. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.",
    )
    from_document: Optional[bytes] = Field(
        default=None,
        description="An optional .epub, .pdf, .txt or similar file can be provided. If provided, we will initialize the Studio project with its content. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.",
    )
    from_content_json: Optional[str] = Field(
        default=None,
        description='An optional content to initialize the Studio project with. If this is set, \'from_url\' and \'from_document\' must be null. If neither \'from_url\', \'from_document\', \'from_content\' are provided we will initialize the Studio project as blank. Example: [{"name": "Chapter A", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "A", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "B", "type": "tts_node"}]}, {"sub_type": "h1", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "C", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "D", "type": "tts_node"}]}]}, {"name": "Chapter B", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "E", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "F", "type": "tts_node"}]}, {"sub_type": "h2", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "G", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "H", "type": "tts_node"}]}]}]',
    )
    quality_preset: Optional[QualityPresetType] = Field(default=None)
    title: Optional[str] = Field(
        default=None,
        description="An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download.",
    )
    author: Optional[str] = Field(
        default=None,
        description="An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download.",
    )
    description: Optional[str] = Field(
        default=None, description="An optional description of the Studio project."
    )
    genres: Optional[List[str]] = Field(
        default=None,
        description="An optional list of genres associated with the Studio project.",
    )
    target_audience: Optional[
        BodyCreateStudioProjectV1StudioProjectsPostTargetAudience
    ] = Field(
        default=None, description="An optional target audience of the Studio project."
    )
    language: Optional[str] = Field(
        default=None,
        description="An optional language of the Studio project. Two-letter language code (ISO 639-1).",
    )
    content_type: Optional[str] = Field(
        default=None, description="An optional content type of the Studio project."
    )
    original_publication_date: Optional[str] = Field(
        default=None,
        description="An optional original publication date of the Studio project, in the format YYYY-MM-DD or YYYY.",
    )
    mature_content: Optional[bool] = Field(
        default=None,
        description="An optional specification of whether this Studio project contains mature content.",
    )
    isbn_number: Optional[str] = Field(
        default=None,
        description="An optional ISBN number of the Studio project you want to create, this will be added as metadata to the mp3 file on Studio project or chapter download.",
    )
    acx_volume_normalization: Optional[bool] = Field(
        default=None,
        description="[Deprecated] When the Studio project is downloaded, should the returned audio have postprocessing in order to make it compliant with audiobook normalized volume requirements",
    )
    volume_normalization: Optional[bool] = Field(
        default=None,
        description="When the Studio project is downloaded, should the returned audio have postprocessing in order to make it compliant with audiobook normalized volume requirements",
    )
    pronunciation_dictionary_locators: Optional[List[str]] = Field(
        default=None,
        description='A list of pronunciation dictionary locators (pronunciation_dictionary_id, version_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form \'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"Vmd4Zor6fplcA7WrINey\\",\\"version_id\\":\\"hRPaxjlTdR7wFMhV4w0b\\"}"\' --form \'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"JzWtcGQMJ6bnlWwyMo7e\\",\\"version_id\\":\\"lbmwxiLu4q6txYxgdZqn\\"}"\'.',
    )
    callback_url: Optional[str] = Field(
        default=None,
        description='A url that will be called by our service when the Studio project is converted. Request will contain a json blob containing the status of the conversion Messages: 1. When project was converted successfully: { type: "project_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", conversion_status: "success", project_snapshot_id: "22m00Tcm4TlvDq8ikMAT", error_details: None, } } 2. When project conversion failed: { type: "project_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", conversion_status: "error", project_snapshot_id: None, error_details: "Error details if conversion failed" } } 3. When chapter was converted successfully: { type: "chapter_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", chapter_id: "22m00Tcm4TlvDq8ikMAT", conversion_status: "success", chapter_snapshot_id: "23m00Tcm4TlvDq8ikMAV", error_details: None, } } 4. When chapter conversion failed: { type: "chapter_conversion_status", event_timestamp: 1234567890, data: { request_id: "1234567890", project_id: "21m00Tcm4TlvDq8ikWAM", chapter_id: "22m00Tcm4TlvDq8ikMAT", conversion_status: "error", chapter_snapshot_id: None, error_details: "Error details if conversion failed" } }',
    )
    fiction: Optional[BodyCreateStudioProjectV1StudioProjectsPostFiction] = Field(
        default=None,
        description="An optional specification of whether the content of this Studio project is fiction.",
    )
    apply_text_normalization: Optional[
        BodyCreateStudioProjectV1StudioProjectsPostApplyTextNormalization
    ] = Field(
        default=None,
        description="This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English.",
    )
    auto_convert: Optional[bool] = Field(
        default=None,
        description="Whether to auto convert the Studio project to audio or not.",
    )
    auto_assign_voices: Optional[bool] = Field(
        default=None,
        description="[Alpha Feature] Whether automatically assign voices to phrases in the create Project.",
    )
    source_type: Optional[BodyCreateStudioProjectV1StudioProjectsPostSourceType] = (
        Field(default=None, description="The type of Studio project to create.")
    )
    voice_settings: Optional[List[str]] = Field(
        default=None,
        description='Optional voice settings overrides for the project, encoded as a list of JSON strings. Example: ["{\\"voice_id\\": \\"21m00Tcm4TlvDq8ikWAM\\", \\"stability\\": 0.7, \\"similarity_boost\\": 0.8, \\"style\\": 0.5, \\"speed\\": 1.0, \\"use_speaker_boost\\": true}"]',
    )
    create_publishing_read: Optional[bool] = Field(
        default=None,
        description="If true, creates a corresponding read for direct publishing in draft state",
    )
