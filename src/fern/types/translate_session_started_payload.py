from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

TranslateSessionStartedPayloadMessageType = typing.Union[
    typing.Literal["session_started"], typing.Any
]


class TranslateSessionStartedPayload(BaseModel):
    """Confirms the session has been initialized.

    :param message_type: The message type identifier.
    :type message_type: TranslateSessionStartedPayloadMessageType
    :param session_id: Unique identifier for this session.
    :type session_id: str
    :param client_session_id: Client-defined session identifier, if provided during connection., defaults to None
    :type client_session_id: str, optional
    """

    message_type: TranslateSessionStartedPayloadMessageType = Field(
        default="session_started", description="The message type identifier."
    )
    session_id: str = Field(description="Unique identifier for this session.")
    client_session_id: Optional[str] = Field(
        default=None,
        description="Client-defined session identifier, if provided during connection.",
    )
