from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .forced_alignment_character_response_model import (
    ForcedAlignmentCharacterResponseModel,
)
from .forced_alignment_word_response_model import ForcedAlignmentWordResponseModel


class ForcedAlignmentResponseModel(BaseModel):
    """Model representing the response from the aligner service.

    :param characters: List of characters with their timing information.
    :type characters: List[ForcedAlignmentCharacterResponseModel]
    :param words: List of words with their timing information.
    :type words: List[ForcedAlignmentWordResponseModel]
    :param loss: The average alignment loss/confidence score for the entire transcript, calculated from all characters.
    :type loss: float
    """

    characters: List[ForcedAlignmentCharacterResponseModel] = Field(
        description="List of characters with their timing information."
    )
    words: List[ForcedAlignmentWordResponseModel] = Field(
        description="List of words with their timing information."
    )
    loss: float = Field(
        description="The average alignment loss/confidence score for the entire transcript, calculated from all characters."
    )
