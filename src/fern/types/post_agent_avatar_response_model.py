from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class PostAgentAvatarResponseModel(BaseModel):
    """PostAgentAvatarResponseModel

    :param agent_id: agent_id
    :type agent_id: str
    :param avatar_url: avatar_url, defaults to None
    :type avatar_url: str, optional
    """

    agent_id: str
    avatar_url: Optional[str] = Field(default=None)
