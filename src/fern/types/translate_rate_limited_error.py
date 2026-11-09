from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslateRateLimitedErrorMessageType = typing.Union[
    typing.Literal["rate_limited"], typing.Any
]


class TranslateRateLimitedError(BaseModel):
    """TranslateRateLimitedError

    :param message_type: message_type
    :type message_type: TranslateRateLimitedErrorMessageType
    :param error: error
    :type error: str
    """

    message_type: TranslateRateLimitedErrorMessageType = Field(default="rate_limited")
    error: str
