from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class CharacterAlignmentResponseModel(BaseModel):
    """CharacterAlignmentResponseModel

    :param characters: characters
    :type characters: List[str]
    :param character_start_times_seconds: character_start_times_seconds
    :type character_start_times_seconds: List[float]
    :param character_end_times_seconds: character_end_times_seconds
    :type character_end_times_seconds: List[float]
    """

    characters: List[str]
    character_start_times_seconds: List[float]
    character_end_times_seconds: List[float]
