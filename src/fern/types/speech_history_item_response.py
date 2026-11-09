from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .history_alignments_response_model import HistoryAlignmentsResponseModel
from .dialogue_input_response_model import DialogueInputResponseModel

SpeechHistoryItemResponseVoiceCategory = typing.Union[
    typing.Literal["premade", "cloned", "generated", "professional"], typing.Any
]

SpeechHistoryItemResponseSource = typing.Union[
    typing.Literal[
        "TTS",
        "STS",
        "Projects",
        "PD",
        "AN",
        "Dubbing",
        "PlayAPI",
        "ConvAI",
        "VoiceGeneration",
        "InVPC",
        "Flows",
    ],
    typing.Any,
]


class SpeechHistoryItemResponse(BaseModel):
    """SpeechHistoryItemResponse

    :param history_item_id: The ID of the history item.
    :type history_item_id: str
    :param request_id: The ID of the request., defaults to None
    :type request_id: str, optional
    :param voice_id: The ID of the voice used., defaults to None
    :type voice_id: str, optional
    :param model_id: The ID of the model., defaults to None
    :type model_id: str, optional
    :param voice_name: The name of the voice., defaults to None
    :type voice_name: str, optional
    :param voice_category: The category of the voice. Either 'premade', 'cloned', 'generated' or 'professional'., defaults to None
    :type voice_category: SpeechHistoryItemResponseVoiceCategory, optional
    :param text: The text used to generate the audio item., defaults to None
    :type text: str, optional
    :param date_unix: Unix timestamp of when the item was created.
    :type date_unix: int
    :param character_count_change_from: The character count change from.
    :type character_count_change_from: int
    :param character_count_change_to: The character count change to.
    :type character_count_change_to: int
    :param content_type: The content type of the generated item.
    :type content_type: str
    :param state: state
    :type state: Any
    :param settings: The settings of the history item., defaults to None
    :type settings: Dict[str, Any], optional
    :param share_link_id: The ID of the share link., defaults to None
    :type share_link_id: str, optional
    :param source: The source of the history item. Either TTS (text to speech), STS (speech to text), AN (audio native), Projects, Dubbing, PlayAPI, PD (pronunciation dictionary) or ConvAI (Agents Platform)., defaults to None
    :type source: SpeechHistoryItemResponseSource, optional
    :param alignments: The alignments of the history item., defaults to None
    :type alignments: HistoryAlignmentsResponseModel, optional
    :param dialogue: The dialogue (voice and text pairs) used to generate the audio item. If this is set then the top level `text` and `voice_id` fields will be empty., defaults to None
    :type dialogue: List[DialogueInputResponseModel], optional
    :param output_format: The output format the audio was originally generated in., defaults to None
    :type output_format: str, optional
    """

    history_item_id: str = Field(description="The ID of the history item.")
    request_id: Optional[str] = Field(
        default=None, description="The ID of the request."
    )
    voice_id: Optional[str] = Field(
        default=None, description="The ID of the voice used."
    )
    model_id: Optional[str] = Field(default=None, description="The ID of the model.")
    voice_name: Optional[str] = Field(
        default=None, description="The name of the voice."
    )
    voice_category: Optional[SpeechHistoryItemResponseVoiceCategory] = Field(
        default=None,
        description="The category of the voice. Either 'premade', 'cloned', 'generated' or 'professional'.",
    )
    text: Optional[str] = Field(
        default=None, description="The text used to generate the audio item."
    )
    date_unix: int = Field(description="Unix timestamp of when the item was created.")
    character_count_change_from: int = Field(
        description="The character count change from."
    )
    character_count_change_to: int = Field(description="The character count change to.")
    content_type: str = Field(description="The content type of the generated item.")
    state: Any
    settings: Optional[Dict[str, Any]] = Field(
        default=None, description="The settings of the history item."
    )
    share_link_id: Optional[str] = Field(
        default=None, description="The ID of the share link."
    )
    source: Optional[SpeechHistoryItemResponseSource] = Field(
        default=None,
        description="The source of the history item. Either TTS (text to speech), STS (speech to text), AN (audio native), Projects, Dubbing, PlayAPI, PD (pronunciation dictionary) or ConvAI (Agents Platform).",
    )
    alignments: Optional[HistoryAlignmentsResponseModel] = Field(
        default=None, description="The alignments of the history item."
    )
    dialogue: Optional[List[DialogueInputResponseModel]] = Field(
        default=None,
        description="The dialogue (voice and text pairs) used to generate the audio item. If this is set then the top level `text` and `voice_id` fields will be empty.",
    )
    output_format: Optional[str] = Field(
        default=None,
        description="The output format the audio was originally generated in.",
    )
