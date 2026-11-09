from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .utterance_response_model import UtteranceResponseModel


class SpeakerResponseModel(BaseModel):
    """SpeakerResponseModel

    :param speaker_id: The ID of the speaker.
    :type speaker_id: str
    :param duration_secs: The duration of the speaker segment in seconds.
    :type duration_secs: float
    :param utterances: The utterances of the speaker., defaults to None
    :type utterances: List[UtteranceResponseModel], optional
    """

    speaker_id: str = Field(description="The ID of the speaker.")
    duration_secs: float = Field(
        description="The duration of the speaker segment in seconds."
    )
    utterances: Optional[List[UtteranceResponseModel]] = Field(
        default=None, description="The utterances of the speaker."
    )
