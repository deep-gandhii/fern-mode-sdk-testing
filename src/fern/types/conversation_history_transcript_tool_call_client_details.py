from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ConversationHistoryTranscriptToolCallClientDetailsType = typing.Union[
    typing.Literal["client"], typing.Any
]


class ConversationHistoryTranscriptToolCallClientDetails(BaseModel):
    """ConversationHistoryTranscriptToolCallClientDetails

    :param type: type, defaults to None
    :type type: ConversationHistoryTranscriptToolCallClientDetailsType, optional
    :param parameters: parameters
    :type parameters: str
    """

    type: Optional[ConversationHistoryTranscriptToolCallClientDetailsType] = Field(
        default=None
    )
    parameters: str
