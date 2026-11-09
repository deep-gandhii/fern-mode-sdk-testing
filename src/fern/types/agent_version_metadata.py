from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .agent_version_parents import AgentVersionParents
from .resource_access_info import ResourceAccessInfo


class AgentVersionMetadata(BaseModel):
    """AgentVersionMetadata

    :param id: id
    :type id: str
    :param agent_id: agent_id
    :type agent_id: str
    :param branch_id: branch_id
    :type branch_id: str
    :param version_description: version_description
    :type version_description: str
    :param seq_no_in_branch: seq_no_in_branch
    :type seq_no_in_branch: int
    :param time_committed_secs: time_committed_secs
    :type time_committed_secs: int
    :param parents: parents
    :type parents: AgentVersionParents
    :param access_info: access_info, defaults to None
    :type access_info: ResourceAccessInfo, optional
    """

    id: str
    agent_id: str
    branch_id: str
    version_description: str
    seq_no_in_branch: int
    time_committed_secs: int
    parents: AgentVersionParents
    access_info: Optional[ResourceAccessInfo] = Field(default=None)
