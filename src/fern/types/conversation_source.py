from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ConversationSourceType = typing.Union[typing.Literal["conversation"], typing.Any]


class ConversationSource(BaseModel):
    """ConversationSource

    :param type: type, defaults to None
    :type type: ConversationSourceType, optional
    :param conversation_id: conversation_id
    :type conversation_id: str
    """

    type: Optional[ConversationSourceType] = Field(default=None)
    conversation_id: str
