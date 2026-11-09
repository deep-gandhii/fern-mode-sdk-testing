from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslateTranscriberErrorMessageType = typing.Union[
    typing.Literal["transcriber_error"], typing.Any
]


class TranslateTranscriberError(BaseModel):
    """TranslateTranscriberError

    :param message_type: message_type
    :type message_type: TranslateTranscriberErrorMessageType
    :param error: error
    :type error: str
    """

    message_type: TranslateTranscriberErrorMessageType = Field(
        default="transcriber_error"
    )
    error: str
