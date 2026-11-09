from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversational_config import ConversationalConfig
from .agent_platform_settings_request_model import AgentPlatformSettingsRequestModel
from .agent_workflow_request_model import AgentWorkflowRequestModel


class UpdateAgentRequest(BaseModel):
    """UpdateAgentRequest

    :param conversation_config: conversation_config, defaults to None
    :type conversation_config: ConversationalConfig, optional
    :param platform_settings: platform_settings, defaults to None
    :type platform_settings: AgentPlatformSettingsRequestModel, optional
    :param workflow: workflow, defaults to None
    :type workflow: AgentWorkflowRequestModel, optional
    :param name: A name to make the agent easier to find, defaults to None
    :type name: str, optional
    :param tags: Tags to help classify and filter the agent, defaults to None
    :type tags: List[str], optional
    :param version_description: Description for this version when publishing changes (only applicable for versioned agents), defaults to None
    :type version_description: str, optional
    """

    conversation_config: Optional[ConversationalConfig] = Field(default=None)
    platform_settings: Optional[AgentPlatformSettingsRequestModel] = Field(default=None)
    workflow: Optional[AgentWorkflowRequestModel] = Field(default=None)
    name: Optional[str] = Field(
        default=None, description="A name to make the agent easier to find"
    )
    tags: Optional[List[str]] = Field(
        default=None, description="Tags to help classify and filter the agent"
    )
    version_description: Optional[str] = Field(
        default=None,
        description="Description for this version when publishing changes (only applicable for versioned agents)",
    )
