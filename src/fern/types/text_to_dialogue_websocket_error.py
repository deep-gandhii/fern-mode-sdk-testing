from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class TextToDialogueWebsocketError(BaseModel):
    """TextToDialogueWebsocketError

    :param message: Human-readable error description.
    :type message: str
    :param error: Machine-readable error identifier (for example `authentication_required`).
    :type error: str
    :param code: WebSocket close code that will follow this payload.
    :type code: int
    :param param: Field name related to the error, when applicable., defaults to None
    :type param: str, optional
    """

    message: str = Field(description="Human-readable error description.")
    error: str = Field(
        description="Machine-readable error identifier (for example `authentication_required`)."
    )
    code: int = Field(description="WebSocket close code that will follow this payload.")
    param: Optional[str] = Field(
        default=None, description="Field name related to the error, when applicable."
    )
