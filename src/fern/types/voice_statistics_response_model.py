from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class VoiceStatisticsResponseModel(BaseModel):
    """VoiceStatisticsResponseModel

    :param project_voice_ref_id: The project voice reference ID.
    :type project_voice_ref_id: str
    :param characters_unconverted: The number of unconverted characters for this voice.
    :type characters_unconverted: int
    :param characters_converted: The number of converted characters for this voice.
    :type characters_converted: int
    :param credits_needed_to_convert: The number of credits needed to convert the remaining audio for this voice., defaults to None
    :type credits_needed_to_convert: int, optional
    :param voice_id: The voice ID., defaults to None
    :type voice_id: str, optional
    """

    project_voice_ref_id: str = Field(description="The project voice reference ID.")
    characters_unconverted: int = Field(
        description="The number of unconverted characters for this voice."
    )
    characters_converted: int = Field(
        description="The number of converted characters for this voice."
    )
    credits_needed_to_convert: Optional[int] = Field(
        default=None,
        description="The number of credits needed to convert the remaining audio for this voice.",
    )
    voice_id: Optional[str] = Field(default=None, description="The voice ID.")
