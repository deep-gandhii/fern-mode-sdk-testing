from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .dubbing_transcript_character import DubbingTranscriptCharacter


class DubbingTranscriptWord(BaseModel):
    """DubbingTranscriptWord

    :param text: text, defaults to None
    :type text: str, optional
    :param word_type: word_type, defaults to None
    :type word_type: str, optional
    :param start_s: start_s, defaults to None
    :type start_s: float, optional
    :param end_s: end_s, defaults to None
    :type end_s: float, optional
    :param characters: characters, defaults to None
    :type characters: List[DubbingTranscriptCharacter], optional
    """

    text: Optional[str] = Field(default=None)
    word_type: Optional[str] = Field(default=None)
    start_s: Optional[float] = Field(default=None)
    end_s: Optional[float] = Field(default=None)
    characters: Optional[List[DubbingTranscriptCharacter]] = Field(default=None)
