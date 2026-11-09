from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranscriptMessageRole = typing.Union[typing.Literal["user", "agent"], typing.Any]


class TranscriptMessage(BaseModel):
    """A single turn in the conversation history.

    :param role: The speaker for this turn.
    :type role: TranscriptMessageRole
    :param content: The transcript text for this turn.
    :type content: str
    """

    role: TranscriptMessageRole = Field(description="The speaker for this turn.")
    content: str = Field(description="The transcript text for this turn.")
