from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .branch_protection_status import BranchProtectionStatus
from .resource_access_info import ResourceAccessInfo


class AgentBranchSummary(BaseModel):
    """AgentBranchSummary

    :param id: id
    :type id: str
    :param name: name
    :type name: str
    :param agent_id: agent_id
    :type agent_id: str
    :param description: description
    :type description: str
    :param created_at: created_at
    :type created_at: int
    :param last_committed_at: last_committed_at
    :type last_committed_at: int
    :param is_archived: is_archived
    :type is_archived: bool
    :param protection_status: protection_status, defaults to None
    :type protection_status: BranchProtectionStatus, optional
    :param access_info: Access information for the branch, defaults to None
    :type access_info: ResourceAccessInfo, optional
    :param current_live_percentage: Percentage of traffic live on the branch, defaults to None
    :type current_live_percentage: float, optional
    :param parent_branch_id: ID of the parent branch, defaults to None
    :type parent_branch_id: str, optional
    :param draft_exists: Whether a draft exists for the branch, defaults to None
    :type draft_exists: bool, optional
    :param calls_7_d: Number of calls in the last 7 days, defaults to None
    :type calls_7_d: int, optional
    """

    id: str
    name: str
    agent_id: str
    description: str
    created_at: int
    last_committed_at: int
    is_archived: bool
    protection_status: Optional[BranchProtectionStatus] = Field(default=None)
    access_info: Optional[ResourceAccessInfo] = Field(
        default=None, description="Access information for the branch"
    )
    current_live_percentage: Optional[float] = Field(
        default=None, description="Percentage of traffic live on the branch"
    )
    parent_branch_id: Optional[str] = Field(
        default=None, description="ID of the parent branch"
    )
    draft_exists: Optional[bool] = Field(
        default=None, description="Whether a draft exists for the branch"
    )
    calls_7_d: Optional[int] = Field(
        alias="calls_7d",
        serialization_alias="calls_7d",
        default=None,
        description="Number of calls in the last 7 days",
    )
