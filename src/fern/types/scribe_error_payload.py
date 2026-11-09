from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ScribeErrorPayloadMessageType = typing.Union[typing.Literal["error"], typing.Any]


class ScribeErrorPayload(BaseModel):
    """Payload for error events during transcription.

    :param message_type: The message type identifier.
    :type message_type: ScribeErrorPayloadMessageType
    :param error: Error message describing what went wrong.
    :type error: str
    """

    message_type: ScribeErrorPayloadMessageType = Field(
        default="error", description="The message type identifier."
    )
    error: str = Field(description="Error message describing what went wrong.")
