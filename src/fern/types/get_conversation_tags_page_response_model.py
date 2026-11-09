from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_tag_response_model import ConversationTagResponseModel


class GetConversationTagsPageResponseModel(BaseModel):
    """GetConversationTagsPageResponseModel

    :param conversation_tags: conversation_tags
    :type conversation_tags: List[ConversationTagResponseModel]
    :param next_cursor: next_cursor, defaults to None
    :type next_cursor: str, optional
    :param has_more: has_more
    :type has_more: bool
    """

    conversation_tags: List[ConversationTagResponseModel]
    next_cursor: Optional[str] = Field(default=None)
    has_more: bool
