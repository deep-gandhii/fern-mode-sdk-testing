from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ForcedAlignmentCharacterResponseModel(BaseModel):
    """Model representing a single character with its timing information from the aligner.

    :param text: The character that was transcribed.
    :type text: str
    :param start: The start time of the character in seconds.
    :type start: float
    :param end: The end time of the character in seconds.
    :type end: float
    """

    text: str = Field(description="The character that was transcribed.")
    start: float = Field(description="The start time of the character in seconds.")
    end: float = Field(description="The end time of the character in seconds.")
