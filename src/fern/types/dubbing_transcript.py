from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .dubbing_transcript_utterance import DubbingTranscriptUtterance


class DubbingTranscript(BaseModel):
    """DubbingTranscript

    :param language: language
    :type language: str
    :param utterances: utterances
    :type utterances: List[DubbingTranscriptUtterance]
    """

    language: str
    utterances: List[DubbingTranscriptUtterance]
