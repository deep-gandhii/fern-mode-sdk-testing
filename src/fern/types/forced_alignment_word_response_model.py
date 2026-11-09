from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ForcedAlignmentWordResponseModel(BaseModel):
    """Model representing a single word with its timing information from the aligner.

    :param text: The word that was transcribed.
    :type text: str
    :param start: The start time of the word in seconds.
    :type start: float
    :param end: The end time of the word in seconds.
    :type end: float
    :param loss: The average alignment loss/confidence score for this word, calculated from its constituent characters.
    :type loss: float
    """

    text: str = Field(description="The word that was transcribed.")
    start: float = Field(description="The start time of the word in seconds.")
    end: float = Field(description="The end time of the word in seconds.")
    loss: float = Field(
        description="The average alignment loss/confidence score for this word, calculated from its constituent characters."
    )
