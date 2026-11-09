from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PongPayloadType = typing.Union[typing.Literal["pong"], typing.Any]


class PongPayload(BaseModel):
    """Reply to a `ping` message.

    :param type: The message type identifier.
    :type type: PongPayloadType
    """

    type: PongPayloadType = Field(
        default="pong", description="The message type identifier."
    )
