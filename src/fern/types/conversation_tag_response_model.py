from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ConversationTagResponseModel(BaseModel):
    """ConversationTagResponseModel

    :param tag_id: tag_id
    :type tag_id: str
    :param workspace_id: workspace_id
    :type workspace_id: str
    :param owner_user_id: owner_user_id
    :type owner_user_id: str
    :param title: title
    :type title: str
    :param description: description
    :type description: str
    :param created_at_unix_secs: created_at_unix_secs
    :type created_at_unix_secs: int
    """

    tag_id: str
    workspace_id: str
    owner_user_id: str
    title: str
    description: Optional[str]
    created_at_unix_secs: int
