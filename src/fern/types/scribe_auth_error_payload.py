from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ScribeAuthErrorPayloadMessageType = typing.Union[
    typing.Literal["auth_error"], typing.Any
]


class ScribeAuthErrorPayload(BaseModel):
    """Payload for authentication errors.

    :param message_type: The message type identifier.
    :type message_type: ScribeAuthErrorPayloadMessageType
    :param error: Authentication error details.
    :type error: str
    """

    message_type: ScribeAuthErrorPayloadMessageType = Field(
        default="auth_error", description="The message type identifier."
    )
    error: str = Field(description="Authentication error details.")
