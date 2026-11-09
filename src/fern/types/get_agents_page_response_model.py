from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .agent_summary_response_model import AgentSummaryResponseModel


class GetAgentsPageResponseModel(BaseModel):
    """GetAgentsPageResponseModel

    :param agents: A list of agents and their metadata
    :type agents: List[AgentSummaryResponseModel]
    :param next_cursor: The next cursor to paginate through the agents, defaults to None
    :type next_cursor: str, optional
    :param has_more: Whether there are more agents to paginate through
    :type has_more: bool
    """

    agents: List[AgentSummaryResponseModel] = Field(
        description="A list of agents and their metadata"
    )
    next_cursor: Optional[str] = Field(
        default=None, description="The next cursor to paginate through the agents"
    )
    has_more: bool = Field(
        description="Whether there are more agents to paginate through"
    )
