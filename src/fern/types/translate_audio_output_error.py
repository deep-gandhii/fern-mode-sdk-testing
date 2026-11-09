from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslateAudioOutputErrorMessageType = typing.Union[
    typing.Literal["audio_output_error"], typing.Any
]


class TranslateAudioOutputError(BaseModel):
    """TranslateAudioOutputError

    :param message_type: message_type
    :type message_type: TranslateAudioOutputErrorMessageType
    :param error: error
    :type error: str
    """

    message_type: TranslateAudioOutputErrorMessageType = Field(
        default="audio_output_error"
    )
    error: str
