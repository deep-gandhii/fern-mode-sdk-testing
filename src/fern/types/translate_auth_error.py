from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslateAuthErrorMessageType = typing.Union[typing.Literal["auth_error"], typing.Any]


class TranslateAuthError(BaseModel):
    """TranslateAuthError

    :param message_type: message_type
    :type message_type: TranslateAuthErrorMessageType
    :param error: error
    :type error: str
    """

    message_type: TranslateAuthErrorMessageType = Field(default="auth_error")
    error: str
