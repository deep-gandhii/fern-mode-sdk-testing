from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from typing import List
from .utils.base_model import BaseModel
from .conversation_config_client_override_output import (
    ConversationConfigClientOverrideOutput,
)
from .conversation_initiation_source_info import ConversationInitiationSourceInfo
from .orchestrator_tool_mock_behavior_config import OrchestratorToolMockBehaviorConfig
from .tool_response_mock_config_output import ToolResponseMockConfigOutput


class ConversationInitiationClientDataInternal(BaseModel):
    """ConversationInitiationClientDataInternal

    :param conversation_config_override: conversation_config_override, defaults to None
    :type conversation_config_override: ConversationConfigClientOverrideOutput, optional
    :param custom_llm_extra_body: custom_llm_extra_body, defaults to None
    :type custom_llm_extra_body: Dict[str, Any], optional
    :param user_id: ID of the end user participating in this conversation (for agent owner's user identification), defaults to None
    :type user_id: str, optional
    :param source_info: Information about the source of conversation initiation, defaults to None
    :type source_info: ConversationInitiationSourceInfo, optional
    :param branch_id: ID of the agent branch to use for this conversation, defaults to None
    :type branch_id: str, optional
    :param environment: Environment to use for resolving environment variables, defaults to None
    :type environment: str, optional
    :param starting_workflow_node_id: If set, start the workflow at this node id instead of the default entry, defaults to None
    :type starting_workflow_node_id: str, optional
    :param dynamic_variables: dynamic_variables, defaults to None
    :type dynamic_variables: Dict[str, Any], optional
    :param tool_mock_config: Orchestrator-side config: tools are identified by resolved names., defaults to None
    :type tool_mock_config: OrchestratorToolMockBehaviorConfig, optional
    :param tool_mock_overrides: Per-tool response mock overrides keyed by resolved tool name, applied ahead of the tool's shared mocks. Used for test-specific mocks., defaults to None
    :type tool_mock_overrides: Dict[str, List[ToolResponseMockConfigOutput]], optional
    """

    conversation_config_override: Optional[ConversationConfigClientOverrideOutput] = (
        Field(default=None)
    )
    custom_llm_extra_body: Optional[Dict[str, Any]] = Field(default=None)
    user_id: Optional[str] = Field(
        default=None,
        description="ID of the end user participating in this conversation (for agent owner's user identification)",
    )
    source_info: Optional[ConversationInitiationSourceInfo] = Field(
        default=None,
        description="Information about the source of conversation initiation",
    )
    branch_id: Optional[str] = Field(
        default=None, description="ID of the agent branch to use for this conversation"
    )
    environment: Optional[str] = Field(
        default=None,
        description="Environment to use for resolving environment variables",
    )
    starting_workflow_node_id: Optional[str] = Field(
        default=None,
        description="If set, start the workflow at this node id instead of the default entry",
    )
    dynamic_variables: Optional[Dict[str, Any]] = Field(default=None)
    tool_mock_config: Optional[OrchestratorToolMockBehaviorConfig] = Field(
        default=None,
        description="Orchestrator-side config: tools are identified by resolved names.",
    )
    tool_mock_overrides: Optional[Dict[str, List[ToolResponseMockConfigOutput]]] = (
        Field(
            default=None,
            description="Per-tool response mock overrides keyed by resolved tool name, applied ahead of the tool's shared mocks. Used for test-specific mocks.",
        )
    )
