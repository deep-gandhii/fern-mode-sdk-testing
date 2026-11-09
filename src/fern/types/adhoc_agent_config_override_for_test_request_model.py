from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversational_config import ConversationalConfig
from .agent_platform_settings_request_model import AgentPlatformSettingsRequestModel
from .agent_workflow_request_model import AgentWorkflowRequestModel


class AdhocAgentConfigOverrideForTestRequestModel(BaseModel):
    """AdhocAgentConfigOverrideForTestRequestModel

    :param conversation_config: conversation_config
    :type conversation_config: ConversationalConfig
    :param platform_settings: platform_settings
    :type platform_settings: AgentPlatformSettingsRequestModel
    :param workflow: workflow, defaults to None
    :type workflow: AgentWorkflowRequestModel, optional
    """

    conversation_config: ConversationalConfig
    platform_settings: AgentPlatformSettingsRequestModel
    workflow: Optional[AgentWorkflowRequestModel] = Field(default=None)
