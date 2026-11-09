from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

InitPayloadType = typing.Union[typing.Literal["init"], typing.Any]


class InitPayload(BaseModel):
    """Payload for the session initialisation message sent by ElevenLabs.

    :param type: The message type identifier.
    :type type: InitPayloadType
    :param conversation_id: Unique identifier for this conversation session.
    :type conversation_id: str
    """

    type: InitPayloadType = Field(
        default="init", description="The message type identifier."
    )
    conversation_id: str = Field(
        description="Unique identifier for this conversation session."
    )
