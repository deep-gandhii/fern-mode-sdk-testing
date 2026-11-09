from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .dubbing_transcript_word import DubbingTranscriptWord


class DubbingTranscriptUtterance(BaseModel):
    """DubbingTranscriptUtterance

    :param text: text, defaults to None
    :type text: str, optional
    :param speaker_id: speaker_id, defaults to None
    :type speaker_id: str, optional
    :param start_s: start_s, defaults to None
    :type start_s: float, optional
    :param end_s: end_s, defaults to None
    :type end_s: float, optional
    :param words: words, defaults to None
    :type words: List[DubbingTranscriptWord], optional
    """

    text: Optional[str] = Field(default=None)
    speaker_id: Optional[str] = Field(default=None)
    start_s: Optional[float] = Field(default=None)
    end_s: Optional[float] = Field(default=None)
    words: Optional[List[DubbingTranscriptWord]] = Field(default=None)
