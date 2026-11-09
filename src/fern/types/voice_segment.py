from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class VoiceSegment(BaseModel):
    """VoiceSegment

    :param voice_id: The voice ID used for this segment
    :type voice_id: str
    :param start_time_seconds: Start time of this voice segment
    :type start_time_seconds: float
    :param end_time_seconds: End time of this voice segment
    :type end_time_seconds: float
    :param character_start_index: Start index in the characters array
    :type character_start_index: int
    :param character_end_index: End index in the characters array (exclusive)
    :type character_end_index: int
    :param dialogue_input_index: Line of the dialogue (script) that this segment is a part of.
    :type dialogue_input_index: int
    """

    voice_id: str = Field(description="The voice ID used for this segment")
    start_time_seconds: float = Field(description="Start time of this voice segment")
    end_time_seconds: float = Field(description="End time of this voice segment")
    character_start_index: int = Field(
        description="Start index in the characters array"
    )
    character_end_index: int = Field(
        description="End index in the characters array (exclusive)"
    )
    dialogue_input_index: int = Field(
        description="Line of the dialogue (script) that this segment is a part of."
    )
