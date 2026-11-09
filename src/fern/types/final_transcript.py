from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class FinalTranscript(BaseModel):
    """FinalTranscript

    :param message_type: message_type, defaults to None
    :type message_type: str, optional
    :param text: text
    :type text: str
    """

    message_type: Optional[str] = Field(default=None)
    text: str
