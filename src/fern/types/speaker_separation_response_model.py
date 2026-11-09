from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .speaker_response_model import SpeakerResponseModel

SpeakerSeparationResponseModelStatus = typing.Union[
    typing.Literal["not_started", "pending", "completed", "failed"], typing.Any
]


class SpeakerSeparationResponseModel(BaseModel):
    """SpeakerSeparationResponseModel

    :param voice_id: The ID of the voice.
    :type voice_id: str
    :param sample_id: The ID of the sample.
    :type sample_id: str
    :param status: The status of the speaker separation.
    :type status: SpeakerSeparationResponseModelStatus
    :param speakers: The speakers of the sample., defaults to None
    :type speakers: Dict[str, SpeakerResponseModel], optional
    :param selected_speaker_ids: The IDs of the selected speakers., defaults to None
    :type selected_speaker_ids: List[str], optional
    """

    voice_id: str = Field(description="The ID of the voice.")
    sample_id: str = Field(description="The ID of the sample.")
    status: SpeakerSeparationResponseModelStatus = Field(
        description="The status of the speaker separation."
    )
    speakers: Optional[Dict[str, SpeakerResponseModel]] = Field(
        default=None, description="The speakers of the sample."
    )
    selected_speaker_ids: Optional[List[str]] = Field(
        default=None, description="The IDs of the selected speakers."
    )
