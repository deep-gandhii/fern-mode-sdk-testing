from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DialogueTextAlignment(BaseModel):
    """Character-level alignment data (field names use snake_case in JSON).

    :param chars: chars, defaults to None
    :type chars: List[str], optional
    :param char_start_times_ms: char_start_times_ms, defaults to None
    :type char_start_times_ms: List[int], optional
    :param char_durations_ms: char_durations_ms, defaults to None
    :type char_durations_ms: List[int], optional
    """

    chars: Optional[List[str]] = Field(default=None)
    char_start_times_ms: Optional[List[int]] = Field(default=None)
    char_durations_ms: Optional[List[int]] = Field(default=None)
