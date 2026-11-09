from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .open_ai_audio_output_format import OpenAiAudioOutputFormat


class OpenAiAudioOutputConfig(BaseModel):
    """OpenAiAudioOutputConfig

    :param format: format, defaults to None
    :type format: OpenAiAudioOutputFormat, optional
    :param voice: voice, defaults to None
    :type voice: str, optional
    """

    format: Optional[OpenAiAudioOutputFormat] = Field(default=None)
    voice: Optional[str] = Field(default=None)
