from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .dynamic_variables_config_workflow_override import (
    DynamicVariablesConfigWorkflowOverride,
)
from .behavior_override import BehaviorOverride
from .prompt_agent_api_model_workflow_override_input import (
    PromptAgentApiModelWorkflowOverrideInput,
)


class AgentConfigApiModelWorkflowOverrideInput(BaseModel):
    """AgentConfigApiModelWorkflowOverrideInput

    :param first_message: If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion., defaults to None
    :type first_message: str, optional
    :param language: Language of the agent - used for ASR and TTS, defaults to None
    :type language: str, optional
    :param hinglish_mode: When enabled and language is Hindi, the agent will respond in Hinglish, defaults to None
    :type hinglish_mode: bool, optional
    :param dynamic_variables: Configuration for dynamic variables, defaults to None
    :type dynamic_variables: DynamicVariablesConfigWorkflowOverride, optional
    :param disable_first_message_interruptions: If true, the user will not be able to interrupt the agent while the first message is being delivered., defaults to None
    :type disable_first_message_interruptions: bool, optional
    :param max_conversation_duration_message: If non-empty, the message the agent will send when max conversation duration is reached., defaults to None
    :type max_conversation_duration_message: str, optional
    :param text_behavior_overrides: Per-channel response behavior overrides for text conversations. Built-in channel defaults apply when unset., defaults to None
    :type text_behavior_overrides: Dict[str, BehaviorOverride], optional
    :param prompt: The prompt for the agent, defaults to None
    :type prompt: PromptAgentApiModelWorkflowOverrideInput, optional
    """

    first_message: Optional[str] = Field(
        default=None,
        description="If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.",
    )
    language: Optional[str] = Field(
        default=None, description="Language of the agent - used for ASR and TTS"
    )
    hinglish_mode: Optional[bool] = Field(
        default=None,
        description="When enabled and language is Hindi, the agent will respond in Hinglish",
    )
    dynamic_variables: Optional[DynamicVariablesConfigWorkflowOverride] = Field(
        default=None, description="Configuration for dynamic variables"
    )
    disable_first_message_interruptions: Optional[bool] = Field(
        default=None,
        description="If true, the user will not be able to interrupt the agent while the first message is being delivered.",
    )
    max_conversation_duration_message: Optional[str] = Field(
        default=None,
        description="If non-empty, the message the agent will send when max conversation duration is reached.",
    )
    text_behavior_overrides: Optional[Dict[str, BehaviorOverride]] = Field(
        default=None,
        description="Per-channel response behavior overrides for text conversations. Built-in channel defaults apply when unset.",
    )
    prompt: Optional[PromptAgentApiModelWorkflowOverrideInput] = Field(
        default=None, description="The prompt for the agent"
    )
