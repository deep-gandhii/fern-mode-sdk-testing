from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .list_response_meta import ListResponseMeta
from .agent_branch_summary import AgentBranchSummary


class ListResponseAgentBranchSummary(BaseModel):
    """ListResponseAgentBranchSummary

    :param meta: meta, defaults to None
    :type meta: ListResponseMeta, optional
    :param results: results
    :type results: List[AgentBranchSummary]
    """

    meta: Optional[ListResponseMeta] = Field(default=None)
    results: List[AgentBranchSummary]
