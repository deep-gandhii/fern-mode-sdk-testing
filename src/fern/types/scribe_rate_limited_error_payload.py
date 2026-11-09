from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ScribeRateLimitedErrorPayloadMessageType = typing.Union[
    typing.Literal["rate_limited"], typing.Any
]


class ScribeRateLimitedErrorPayload(BaseModel):
    """Payload for rate limited errors.

    :param message_type: The message type identifier.
    :type message_type: ScribeRateLimitedErrorPayloadMessageType
    :param error: Rate limited error details.
    :type error: str
    """

    message_type: ScribeRateLimitedErrorPayloadMessageType = Field(
        default="rate_limited", description="The message type identifier."
    )
    error: str = Field(description="Rate limited error details.")
