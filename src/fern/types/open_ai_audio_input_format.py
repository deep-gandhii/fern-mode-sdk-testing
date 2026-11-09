from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .open_ai_audio_format import OpenAiAudioFormat


class OpenAiAudioInputFormat(BaseModel):
    """OpenAiAudioInputFormat

    :param type: type, defaults to None
    :type type: OpenAiAudioFormat, optional
    :param rate: rate, defaults to None
    :type rate: int, optional
    """

    type: Optional[OpenAiAudioFormat] = Field(default=None)
    rate: Optional[int] = Field(default=None)
