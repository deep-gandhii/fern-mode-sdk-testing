from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .open_ai_audio_input_config import OpenAiAudioInputConfig
from .open_ai_audio_output_config import OpenAiAudioOutputConfig


class OpenAiAudioConfig(BaseModel):
    """OpenAiAudioConfig

    :param input: input, defaults to None
    :type input: OpenAiAudioInputConfig, optional
    :param output: output, defaults to None
    :type output: OpenAiAudioOutputConfig, optional
    """

    input: Optional[OpenAiAudioInputConfig] = Field(default=None)
    output: Optional[OpenAiAudioOutputConfig] = Field(default=None)
