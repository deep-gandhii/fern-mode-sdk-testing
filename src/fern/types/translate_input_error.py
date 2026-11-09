from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslateInputErrorMessageType = typing.Union[typing.Literal["input_error"], typing.Any]


class TranslateInputError(BaseModel):
    """TranslateInputError

    :param message_type: message_type
    :type message_type: TranslateInputErrorMessageType
    :param error: error
    :type error: str
    """

    message_type: TranslateInputErrorMessageType = Field(default="input_error")
    error: str
