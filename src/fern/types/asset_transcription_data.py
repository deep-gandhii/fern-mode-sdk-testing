from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class AssetTranscriptionData(BaseModel):
    """AssetTranscriptionData

    :param language_code: language_code
    :type language_code: str
    :param text: text
    :type text: str
    :param words: words
    :type words: List[str]
    :param word_start_times_ms: word_start_times_ms
    :type word_start_times_ms: List[int]
    :param word_end_times_ms: word_end_times_ms
    :type word_end_times_ms: List[int]
    :param word_speaker_ids: word_speaker_ids
    :type word_speaker_ids: List[str]
    """

    language_code: str
    text: str
    words: List[str]
    word_start_times_ms: List[int]
    word_end_times_ms: List[int]
    word_speaker_ids: List[str]
