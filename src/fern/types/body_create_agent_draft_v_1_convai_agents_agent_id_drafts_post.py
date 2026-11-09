from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .agent_workflow_request_model import AgentWorkflowRequestModel


class BodyCreateAgentDraftV1ConvaiAgentsAgentIdDraftsPost(BaseModel):
    """BodyCreateAgentDraftV1ConvaiAgentsAgentIdDraftsPost

    :param conversation_config: Conversation config for the draft
    :type conversation_config: Dict[str, Any]
    :param platform_settings: Platform settings for the draft
    :type platform_settings: Dict[str, Any]
    :param workflow: workflow
    :type workflow: AgentWorkflowRequestModel
    :param name: Name for the draft
    :type name: str
    :param tags: Tags to help classify and filter the agent, defaults to None
    :type tags: List[str], optional
    """

    conversation_config: Dict[str, Any] = Field(
        description="Conversation config for the draft"
    )
    platform_settings: Dict[str, Any] = Field(
        description="Platform settings for the draft"
    )
    workflow: AgentWorkflowRequestModel
    name: str = Field(description="Name for the draft")
    tags: Optional[List[str]] = Field(
        default=None, description="Tags to help classify and filter the agent"
    )
