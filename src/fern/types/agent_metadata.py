from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class AgentMetadata(BaseModel):
    """AgentMetadata

    :param agent_id: agent_id
    :type agent_id: str
    :param branch_id: branch_id, defaults to None
    :type branch_id: str, optional
    :param workflow_node_id: workflow_node_id, defaults to None
    :type workflow_node_id: str, optional
    :param version_id: version_id, defaults to None
    :type version_id: str, optional
    """

    agent_id: str
    branch_id: Optional[str] = Field(default=None)
    workflow_node_id: Optional[str] = Field(default=None)
    version_id: Optional[str] = Field(default=None)
