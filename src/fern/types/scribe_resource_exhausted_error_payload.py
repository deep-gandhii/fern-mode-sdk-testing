from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ScribeResourceExhaustedErrorPayloadMessageType = typing.Union[
    typing.Literal["resource_exhausted"], typing.Any
]


class ScribeResourceExhaustedErrorPayload(BaseModel):
    """Payload for resource exhausted errors.

    :param message_type: The message type identifier.
    :type message_type: ScribeResourceExhaustedErrorPayloadMessageType
    :param error: Resource exhausted error details.
    :type error: str
    """

    message_type: ScribeResourceExhaustedErrorPayloadMessageType = Field(
        default="resource_exhausted", description="The message type identifier."
    )
    error: str = Field(description="Resource exhausted error details.")
