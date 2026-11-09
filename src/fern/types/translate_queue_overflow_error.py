from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslateQueueOverflowErrorMessageType = typing.Union[
    typing.Literal["queue_overflow"], typing.Any
]


class TranslateQueueOverflowError(BaseModel):
    """TranslateQueueOverflowError

    :param message_type: message_type
    :type message_type: TranslateQueueOverflowErrorMessageType
    :param error: error
    :type error: str
    """

    message_type: TranslateQueueOverflowErrorMessageType = Field(
        default="queue_overflow"
    )
    error: str
