from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .llm import Llm
from .llm_reasoning_effort import LlmReasoningEffort
from .built_in_tools_output import BuiltInToolsOutput
from .knowledge_base_locator import KnowledgeBaseLocator
from .custom_llm import CustomLlm
from .rag_config_output import RagConfigOutput
from .backup_llm_default import BackupLlmDefault
from .backup_llm_disabled import BackupLlmDisabled
from .backup_llm_override import BackupLlmOverride
from .webhook_tool_config_output import WebhookToolConfigOutput
from .client_tool_config_output import ClientToolConfigOutput
from .system_tool_config_output import SystemToolConfigOutput
from .mcp_tool_config_output import McpToolConfigOutput
from .api_integration_webhook_tool_config_output import (
    ApiIntegrationWebhookToolConfigOutput,
)
from .smb_tool_config import SmbToolConfig


# fernMode variant type for a shared-component member of PromptAgentApiModelOutputBackupLlmConfig
class PromptAgentApiModelOutputBackupLlmConfig_Default(BackupLlmDefault):
    pass


# fernMode variant type for a shared-component member of PromptAgentApiModelOutputBackupLlmConfig
class PromptAgentApiModelOutputBackupLlmConfig_Disabled(BackupLlmDisabled):
    pass


# fernMode variant type for a shared-component member of PromptAgentApiModelOutputBackupLlmConfig
class PromptAgentApiModelOutputBackupLlmConfig_Override(BackupLlmOverride):
    pass


# Union type for PromptAgentApiModelOutputBackupLlmConfig
# Pydantic will attempt to validate against each type in order
PromptAgentApiModelOutputBackupLlmConfig = Union[
    BackupLlmDefault, BackupLlmDisabled, BackupLlmOverride
]
# TypeAdapter for runtime validation of PromptAgentApiModelOutputBackupLlmConfig
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

PromptAgentApiModelOutputBackupLlmConfig_adapter = TypeAdapter(
    PromptAgentApiModelOutputBackupLlmConfig
)


# fernMode variant type for a shared-component member of PromptAgentApiModelOutputToolsItem
class PromptAgentApiModelOutputToolsItem_Webhook(WebhookToolConfigOutput):
    pass


# fernMode variant type for a shared-component member of PromptAgentApiModelOutputToolsItem
class PromptAgentApiModelOutputToolsItem_Client(ClientToolConfigOutput):
    pass


# fernMode variant type for a shared-component member of PromptAgentApiModelOutputToolsItem
class PromptAgentApiModelOutputToolsItem_System(SystemToolConfigOutput):
    pass


# fernMode variant type for a shared-component member of PromptAgentApiModelOutputToolsItem
class PromptAgentApiModelOutputToolsItem_Mcp(McpToolConfigOutput):
    pass


# fernMode variant type for a shared-component member of PromptAgentApiModelOutputToolsItem
class PromptAgentApiModelOutputToolsItem_ApiIntegrationWebhook(
    ApiIntegrationWebhookToolConfigOutput
):
    pass


# fernMode variant type for a shared-component member of PromptAgentApiModelOutputToolsItem
class PromptAgentApiModelOutputToolsItem_Smb(SmbToolConfig):
    pass


# Union type for PromptAgentApiModelOutputToolsItem
# Pydantic will attempt to validate against each type in order
PromptAgentApiModelOutputToolsItem = Union[
    WebhookToolConfigOutput,
    ClientToolConfigOutput,
    SystemToolConfigOutput,
    McpToolConfigOutput,
    ApiIntegrationWebhookToolConfigOutput,
    SmbToolConfig,
]
# TypeAdapter for runtime validation of PromptAgentApiModelOutputToolsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

PromptAgentApiModelOutputToolsItem_adapter = TypeAdapter(
    PromptAgentApiModelOutputToolsItem
)


class PromptAgentApiModelOutput(BaseModel):
    """PromptAgentApiModelOutput

    :param prompt: The prompt for the agent, defaults to None
    :type prompt: str, optional
    :param llm: llm, defaults to None
    :type llm: Llm, optional
    :param reasoning_effort: Reasoning effort of the model. Only available for some models., defaults to None
    :type reasoning_effort: LlmReasoningEffort, optional
    :param thinking_budget: Max number of tokens used for thinking. Use 0 to turn off if supported by the model., defaults to None
    :type thinking_budget: int, optional
    :param enable_reasoning_summary: Enable model reasoning summaries. When disabled, we do not request summaries from provider if possible for faster TTFB. Not ZRM compatible., defaults to None
    :type enable_reasoning_summary: bool, optional
    :param temperature: The temperature for the LLM. Defaults to 0. Set to null to omit the parameter from the LLM request entirely (useful for custom LLMs that reject the temperature field)., defaults to None
    :type temperature: float, optional
    :param max_tokens: If greater than 0, maximum number of tokens the LLM can predict, defaults to None
    :type max_tokens: int, optional
    :param tool_ids: A list of IDs of tools used by the agent, defaults to None
    :type tool_ids: List[str], optional
    :param built_in_tools: built_in_tools, defaults to None
    :type built_in_tools: BuiltInToolsOutput, optional
    :param mcp_server_ids: A list of MCP server ids to be used by the agent, defaults to None
    :type mcp_server_ids: List[str], optional
    :param native_mcp_server_ids: A list of Native MCP server ids to be used by the agent, defaults to None
    :type native_mcp_server_ids: List[str], optional
    :param knowledge_base: A list of knowledge bases to be used by the agent, defaults to None
    :type knowledge_base: List[KnowledgeBaseLocator], optional
    :param custom_llm: Definition for a custom LLM if LLM field is set to 'CUSTOM_LLM', defaults to None
    :type custom_llm: CustomLlm, optional
    :param ignore_default_personality: Whether to remove the default personality lines from the system prompt, defaults to None
    :type ignore_default_personality: bool, optional
    :param rag: rag, defaults to None
    :type rag: RagConfigOutput, optional
    :param timezone: Timezone for displaying current time in system prompt. If set, the current time will be included in the system prompt using this timezone. Must be a valid timezone name (e.g., 'America/New_York', 'Europe/London', 'UTC'). Recommended for accurate time-aware responses; without this, the agent has no knowledge of the current date/time unless you provide it via dynamic variables or tools, which can lead to incorrect or hallucinated time references., defaults to None
    :type timezone: str, optional
    :param backup_llm_config: Configuration for backup LLM cascading. Can be disabled, use system defaults, or specify custom order., defaults to None
    :type backup_llm_config: PromptAgentApiModelOutputBackupLlmConfig, optional
    :param cascade_timeout_seconds: Time in seconds before cascading to backup LLM. Must be between 2 and 15 seconds., defaults to None
    :type cascade_timeout_seconds: float, optional
    :param tools: A list of tools that the agent can use over the course of the conversation, use tool_ids instead, defaults to None
    :type tools: List[PromptAgentApiModelOutputToolsItem], optional
    """

    prompt: Optional[str] = Field(default=None, description="The prompt for the agent")
    llm: Optional[Llm] = Field(default=None)
    reasoning_effort: Optional[LlmReasoningEffort] = Field(
        default=None,
        description="Reasoning effort of the model. Only available for some models.",
    )
    thinking_budget: Optional[int] = Field(
        default=None,
        description="Max number of tokens used for thinking. Use 0 to turn off if supported by the model.",
    )
    enable_reasoning_summary: Optional[bool] = Field(
        default=None,
        description="Enable model reasoning summaries. When disabled, we do not request summaries from provider if possible for faster TTFB. Not ZRM compatible.",
    )
    temperature: Optional[float] = Field(
        default=None,
        description="The temperature for the LLM. Defaults to 0. Set to null to omit the parameter from the LLM request entirely (useful for custom LLMs that reject the temperature field).",
    )
    max_tokens: Optional[int] = Field(
        default=None,
        description="If greater than 0, maximum number of tokens the LLM can predict",
    )
    tool_ids: Optional[List[str]] = Field(
        default=None, description="A list of IDs of tools used by the agent"
    )
    built_in_tools: Optional[BuiltInToolsOutput] = Field(default=None)
    mcp_server_ids: Optional[List[str]] = Field(
        default=None, description="A list of MCP server ids to be used by the agent"
    )
    native_mcp_server_ids: Optional[List[str]] = Field(
        default=None,
        description="A list of Native MCP server ids to be used by the agent",
    )
    knowledge_base: Optional[List[KnowledgeBaseLocator]] = Field(
        default=None, description="A list of knowledge bases to be used by the agent"
    )
    custom_llm: Optional[CustomLlm] = Field(
        default=None,
        description="Definition for a custom LLM if LLM field is set to 'CUSTOM_LLM'",
    )
    ignore_default_personality: Optional[bool] = Field(
        default=None,
        description="Whether to remove the default personality lines from the system prompt",
    )
    rag: Optional[RagConfigOutput] = Field(default=None)
    timezone: Optional[str] = Field(
        default=None,
        description="Timezone for displaying current time in system prompt. If set, the current time will be included in the system prompt using this timezone. Must be a valid timezone name (e.g., 'America/New_York', 'Europe/London', 'UTC'). Recommended for accurate time-aware responses; without this, the agent has no knowledge of the current date/time unless you provide it via dynamic variables or tools, which can lead to incorrect or hallucinated time references.",
    )
    backup_llm_config: Optional[PromptAgentApiModelOutputBackupLlmConfig] = Field(
        default=None,
        description="Configuration for backup LLM cascading. Can be disabled, use system defaults, or specify custom order.",
    )
    cascade_timeout_seconds: Optional[float] = Field(
        default=None,
        description="Time in seconds before cascading to backup LLM. Must be between 2 and 15 seconds.",
    )
    tools: Optional[List[PromptAgentApiModelOutputToolsItem]] = Field(
        default=None,
        description="A list of tools that the agent can use over the course of the conversation, use tool_ids instead",
    )
