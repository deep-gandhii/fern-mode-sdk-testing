from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ScribeTranscriberErrorPayloadMessageType = typing.Union[
    typing.Literal["transcriber_error"], typing.Any
]


class ScribeTranscriberErrorPayload(BaseModel):
    """Payload for transcriber errors.

    :param message_type: The message type identifier.
    :type message_type: ScribeTranscriberErrorPayloadMessageType
    :param error: Transcriber error details.
    :type error: str
    """

    message_type: ScribeTranscriberErrorPayloadMessageType = Field(
        default="transcriber_error", description="The message type identifier."
    )
    error: str = Field(description="Transcriber error details.")
