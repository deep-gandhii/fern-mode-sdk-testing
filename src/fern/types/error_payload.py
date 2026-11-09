from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ErrorPayloadType = typing.Union[typing.Literal["error"], typing.Any]


class ErrorPayload(BaseModel):
    """Payload for protocol-level errors sent by ElevenLabs before closing the connection.

    :param type: The message type identifier.
    :type type: ErrorPayloadType
    :param message: Human-readable description of the error.
    :type message: str
    """

    type: ErrorPayloadType = Field(
        default="error", description="The message type identifier."
    )
    message: str = Field(description="Human-readable description of the error.")
