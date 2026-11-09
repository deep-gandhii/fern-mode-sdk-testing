from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ScribeQuotaExceededErrorPayloadMessageType = typing.Union[
    typing.Literal["quota_exceeded"], typing.Any
]


class ScribeQuotaExceededErrorPayload(BaseModel):
    """Payload for quota exceeded errors.

    :param message_type: The message type identifier.
    :type message_type: ScribeQuotaExceededErrorPayloadMessageType
    :param error: Quota exceeded error details.
    :type error: str
    """

    message_type: ScribeQuotaExceededErrorPayloadMessageType = Field(
        default="quota_exceeded", description="The message type identifier."
    )
    error: str = Field(description="Quota exceeded error details.")
