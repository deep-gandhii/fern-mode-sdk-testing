from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .branch_protection_status import BranchProtectionStatus
from .resource_access_info import ResourceAccessInfo
from .agent_branch_basic_info import AgentBranchBasicInfo
from .agent_version_metadata import AgentVersionMetadata


class AgentBranchResponse(BaseModel):
    """AgentBranchResponse

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
    :param parent_branch: Parent branch of the branch, defaults to None
    :type parent_branch: AgentBranchBasicInfo, optional
    :param most_recent_versions: Most recent versions on the branch, defaults to None
    :type most_recent_versions: List[AgentVersionMetadata], optional
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
    parent_branch: Optional[AgentBranchBasicInfo] = Field(
        default=None, description="Parent branch of the branch"
    )
    most_recent_versions: Optional[List[AgentVersionMetadata]] = Field(
        default=None, description="Most recent versions on the branch"
    )
