from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class WordTimestamp(BaseModel):
    """WordTimestamp

    :param word: word
    :type word: str
    :param start_ms: start_ms
    :type start_ms: int
    :param end_ms: end_ms
    :type end_ms: int
    """

    word: str
    start_ms: int
    end_ms: int
