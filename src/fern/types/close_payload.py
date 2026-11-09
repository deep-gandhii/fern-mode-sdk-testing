from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ClosePayloadType = typing.Union[typing.Literal["close"], typing.Any]


class ClosePayload(BaseModel):
    """Payload indicating a clean end-of-conversation signal from ElevenLabs.

    :param type: The message type identifier.
    :type type: ClosePayloadType
    """

    type: ClosePayloadType = Field(
        default="close", description="The message type identifier."
    )
