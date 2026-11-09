from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslateErrorPayloadMessageType = typing.Union[typing.Literal["error"], typing.Any]


class TranslateErrorPayload(BaseModel):
    """Error encountered during translation.

    :param message_type: The message type identifier.
    :type message_type: TranslateErrorPayloadMessageType
    :param error: Error message.
    :type error: str
    """

    message_type: TranslateErrorPayloadMessageType = Field(
        default="error", description="The message type identifier."
    )
    error: str = Field(description="Error message.")
