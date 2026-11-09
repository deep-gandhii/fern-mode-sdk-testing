from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ScribeChunkSizeExceededErrorPayloadMessageType = typing.Union[
    typing.Literal["chunk_size_exceeded"], typing.Any
]


class ScribeChunkSizeExceededErrorPayload(BaseModel):
    """Payload for chunk size exceeded errors.

    :param message_type: The message type identifier.
    :type message_type: ScribeChunkSizeExceededErrorPayloadMessageType
    :param error: Chunk size exceeded error details.
    :type error: str
    """

    message_type: ScribeChunkSizeExceededErrorPayloadMessageType = Field(
        default="chunk_size_exceeded", description="The message type identifier."
    )
    error: str = Field(description="Chunk size exceeded error details.")
