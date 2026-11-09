from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AssignConversationTagsRequestModel(BaseModel):
    """AssignConversationTagsRequestModel

    :param tag_ids: Tag IDs to add to the conversation. Re-assigning an existing tag is a no-op.
    :type tag_ids: List[str]
    """

    tag_ids: List[str] = Field(
        description="Tag IDs to add to the conversation. Re-assigning an existing tag is a no-op."
    )
