from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .voice_statistics_response_model import VoiceStatisticsResponseModel


class ChapterStatisticsResponse(BaseModel):
    """ChapterStatisticsResponse

    :param characters_unconverted: The number of unconverted characters.
    :type characters_unconverted: int
    :param characters_converted: The number of converted characters.
    :type characters_converted: int
    :param paragraphs_converted: The number of converted paragraphs.
    :type paragraphs_converted: int
    :param paragraphs_unconverted: The number of unconverted paragraphs.
    :type paragraphs_unconverted: int
    :param credits_needed_to_convert: The number of credits needed to convert the remaining paragraphs., defaults to None
    :type credits_needed_to_convert: int, optional
    :param voice_statistics: Per-voice breakdown of character counts., defaults to None
    :type voice_statistics: List[VoiceStatisticsResponseModel], optional
    """

    characters_unconverted: int = Field(
        description="The number of unconverted characters."
    )
    characters_converted: int = Field(description="The number of converted characters.")
    paragraphs_converted: int = Field(description="The number of converted paragraphs.")
    paragraphs_unconverted: int = Field(
        description="The number of unconverted paragraphs."
    )
    credits_needed_to_convert: Optional[int] = Field(
        default=None,
        description="The number of credits needed to convert the remaining paragraphs.",
    )
    voice_statistics: Optional[List[VoiceStatisticsResponseModel]] = Field(
        default=None, description="Per-voice breakdown of character counts."
    )
