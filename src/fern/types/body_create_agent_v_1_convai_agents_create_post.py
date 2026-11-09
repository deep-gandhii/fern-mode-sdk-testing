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


class BodyCreateAgentV1ConvaiAgentsCreatePost(BaseModel):
    """BodyCreateAgentV1ConvaiAgentsCreatePost

    :param conversation_config: conversation_config
    :type conversation_config: ConversationalConfig
    :param platform_settings: Platform settings for the agent are all settings that aren't related to the conversation orchestration and content., defaults to None
    :type platform_settings: AgentPlatformSettingsRequestModel, optional
    :param workflow: workflow, defaults to None
    :type workflow: AgentWorkflowRequestModel, optional
    :param name: A name to make the agent easier to find, defaults to None
    :type name: str, optional
    :param tags: Tags to help classify and filter the agent, defaults to None
    :type tags: List[str], optional
    """

    conversation_config: ConversationalConfig
    platform_settings: Optional[AgentPlatformSettingsRequestModel] = Field(
        default=None,
        description="Platform settings for the agent are all settings that aren't related to the conversation orchestration and content.",
    )
    workflow: Optional[AgentWorkflowRequestModel] = Field(default=None)
    name: Optional[str] = Field(
        default=None, description="A name to make the agent easier to find"
    )
    tags: Optional[List[str]] = Field(
        default=None, description="Tags to help classify and filter the agent"
    )
