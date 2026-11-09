from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .agent_workflow_request_model import AgentWorkflowRequestModel


class BodyCreateANewBranchV1ConvaiAgentsAgentIdBranchesPost(BaseModel):
    """BodyCreateANewBranchV1ConvaiAgentsAgentIdBranchesPost

    :param parent_version_id: ID of the version to branch from
    :type parent_version_id: str
    :param name: Name of the branch. It is unique within the agent.
    :type name: str
    :param description: Description for the branch
    :type description: str
    :param conversation_config: Changes to apply to conversation config, defaults to None
    :type conversation_config: Dict[str, Any], optional
    :param platform_settings: Changes to apply to platform settings, defaults to None
    :type platform_settings: Dict[str, Any], optional
    :param workflow: Updated workflow definition, defaults to None
    :type workflow: AgentWorkflowRequestModel, optional
    """

    parent_version_id: str = Field(description="ID of the version to branch from")
    name: str = Field(description="Name of the branch. It is unique within the agent.")
    description: str = Field(description="Description for the branch")
    conversation_config: Optional[Dict[str, Any]] = Field(
        default=None, description="Changes to apply to conversation config"
    )
    platform_settings: Optional[Dict[str, Any]] = Field(
        default=None, description="Changes to apply to platform settings"
    )
    workflow: Optional[AgentWorkflowRequestModel] = Field(
        default=None, description="Updated workflow definition"
    )
