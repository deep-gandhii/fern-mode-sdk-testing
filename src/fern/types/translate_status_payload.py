from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslateStatusPayloadMessageType = typing.Union[typing.Literal["status"], typing.Any]


class TranslateStatusPayload(BaseModel):
    """Session lifecycle update.

    :param message_type: The message type identifier.
    :type message_type: TranslateStatusPayloadMessageType
    :param status: Current session status (`started` or `stopped`).
    :type status: str
    """

    message_type: TranslateStatusPayloadMessageType = Field(
        default="status", description="The message type identifier."
    )
    status: str = Field(description="Current session status (`started` or `stopped`).")
