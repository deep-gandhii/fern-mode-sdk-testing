from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DubbingTranscriptCharacter(BaseModel):
    """DubbingTranscriptCharacter

    :param text: text, defaults to None
    :type text: str, optional
    :param start_s: start_s, defaults to None
    :type start_s: float, optional
    :param end_s: end_s, defaults to None
    :type end_s: float, optional
    """

    text: Optional[str] = Field(default=None)
    start_s: Optional[float] = Field(default=None)
    end_s: Optional[float] = Field(default=None)
