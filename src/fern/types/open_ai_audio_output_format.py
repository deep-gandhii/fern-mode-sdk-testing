from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .open_ai_audio_format import OpenAiAudioFormat


class OpenAiAudioOutputFormat(BaseModel):
    """OpenAiAudioOutputFormat

    :param type: type, defaults to None
    :type type: OpenAiAudioFormat, optional
    """

    type: Optional[OpenAiAudioFormat] = Field(default=None)
