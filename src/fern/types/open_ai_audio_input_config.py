from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .open_ai_audio_input_format import OpenAiAudioInputFormat
from .open_ai_turn_detection import OpenAiTurnDetection


class OpenAiAudioInputConfig(BaseModel):
    """OpenAiAudioInputConfig

    :param format: format, defaults to None
    :type format: OpenAiAudioInputFormat, optional
    :param turn_detection: turn_detection, defaults to None
    :type turn_detection: OpenAiTurnDetection, optional
    """

    format: Optional[OpenAiAudioInputFormat] = Field(default=None)
    turn_detection: Optional[OpenAiTurnDetection] = Field(default=None)
