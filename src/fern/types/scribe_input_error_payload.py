from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ScribeInputErrorPayloadMessageType = typing.Union[
    typing.Literal["input_error"], typing.Any
]


class ScribeInputErrorPayload(BaseModel):
    """Payload for input errors.

    :param message_type: The message type identifier.
    :type message_type: ScribeInputErrorPayloadMessageType
    :param error: Input error details.
    :type error: str
    """

    message_type: ScribeInputErrorPayloadMessageType = Field(
        default="input_error", description="The message type identifier."
    )
    error: str = Field(description="Input error details.")
