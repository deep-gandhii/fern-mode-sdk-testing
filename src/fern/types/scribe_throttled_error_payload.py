from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ScribeThrottledErrorPayloadMessageType = typing.Union[
    typing.Literal["commit_throttled"], typing.Any
]


class ScribeThrottledErrorPayload(BaseModel):
    """Payload for throttled errors.

    :param message_type: The message type identifier.
    :type message_type: ScribeThrottledErrorPayloadMessageType
    :param error: Throttled error details.
    :type error: str
    """

    message_type: ScribeThrottledErrorPayloadMessageType = Field(
        default="commit_throttled", description="The message type identifier."
    )
    error: str = Field(description="Throttled error details.")
