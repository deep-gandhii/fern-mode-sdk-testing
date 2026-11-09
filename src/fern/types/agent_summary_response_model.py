from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .resource_access_info import ResourceAccessInfo


class AgentSummaryResponseModel(BaseModel):
    """AgentSummaryResponseModel

    :param agent_id: The ID of the agent
    :type agent_id: str
    :param name: The name of the agent
    :type name: str
    :param tags: Agent tags used to categorize the agent
    :type tags: List[str]
    :param created_at_unix_secs: The creation time of the agent in unix seconds
    :type created_at_unix_secs: int
    :param access_info: access_info
    :type access_info: ResourceAccessInfo
    :param last_call_time_unix_secs: The time of the most recent call in unix seconds, null if no calls have been made, defaults to None
    :type last_call_time_unix_secs: int, optional
    :param archived: Whether the agent is archived, defaults to None
    :type archived: bool, optional
    """

    agent_id: str = Field(description="The ID of the agent")
    name: str = Field(description="The name of the agent")
    tags: List[str] = Field(description="Agent tags used to categorize the agent")
    created_at_unix_secs: int = Field(
        description="The creation time of the agent in unix seconds"
    )
    access_info: ResourceAccessInfo
    last_call_time_unix_secs: Optional[int] = Field(
        default=None,
        description="The time of the most recent call in unix seconds, null if no calls have been made",
    )
    archived: Optional[bool] = Field(
        default=None, description="Whether the agent is archived"
    )
