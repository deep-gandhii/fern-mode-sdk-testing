from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PingPayloadType = typing.Union[typing.Literal["ping"], typing.Any]


class PingPayload(BaseModel):
    """Keep-alive ping sent periodically by ElevenLabs.

    :param type: The message type identifier.
    :type type: PingPayloadType
    """

    type: PingPayloadType = Field(
        default="ping", description="The message type identifier."
    )
