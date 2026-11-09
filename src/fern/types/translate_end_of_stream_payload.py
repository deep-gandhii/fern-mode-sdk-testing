from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslateEndOfStreamPayloadMessageType = typing.Union[
    typing.Literal["end_of_stream"], typing.Any
]


class TranslateEndOfStreamPayload(BaseModel):
    """Signal that the client has finished sending audio.

    :param message_type: The message type identifier.
    :type message_type: TranslateEndOfStreamPayloadMessageType
    """

    message_type: TranslateEndOfStreamPayloadMessageType = Field(
        default="end_of_stream", description="The message type identifier."
    )
