from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class HistoryAlignmentResponseModel(BaseModel):
    """HistoryAlignmentResponseModel

    :param characters: The characters in the alignment.
    :type characters: List[str]
    :param character_start_times_seconds: The start times of the characters in seconds.
    :type character_start_times_seconds: List[float]
    :param character_end_times_seconds: The end times of the characters in seconds.
    :type character_end_times_seconds: List[float]
    """

    characters: List[str] = Field(description="The characters in the alignment.")
    character_start_times_seconds: List[float] = Field(
        description="The start times of the characters in seconds."
    )
    character_end_times_seconds: List[float] = Field(
        description="The end times of the characters in seconds."
    )
