from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class AudioSegment(BaseModel):
    """AudioSegment

    :param start_ms: start_ms
    :type start_ms: int
    :param end_ms: end_ms
    :type end_ms: int
    :param description: description
    :type description: str
    :param segment_type: segment_type, defaults to None
    :type segment_type: str, optional
    :param has_speech: has_speech, defaults to None
    :type has_speech: bool, optional
    :param has_music: has_music, defaults to None
    :type has_music: bool, optional
    :param pacing: pacing, defaults to None
    :type pacing: str, optional
    """

    start_ms: int
    end_ms: int
    description: str
    segment_type: Optional[str] = Field(default=None)
    has_speech: Optional[bool] = Field(default=None)
    has_music: Optional[bool] = Field(default=None)
    pacing: Optional[str] = Field(default=None)
