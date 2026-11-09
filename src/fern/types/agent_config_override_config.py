from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .prompt_agent_api_model_override_config import PromptAgentApiModelOverrideConfig


class AgentConfigOverrideConfig(BaseModel):
    """AgentConfigOverrideConfig

    :param first_message: Whether to allow overriding the first_message field., defaults to None
    :type first_message: bool, optional
    :param language: Whether to allow overriding the language field., defaults to None
    :type language: bool, optional
    :param max_conversation_duration_message: Whether to allow overriding the max_conversation_duration_message field., defaults to None
    :type max_conversation_duration_message: bool, optional
    :param prompt: prompt, defaults to None
    :type prompt: PromptAgentApiModelOverrideConfig, optional
    """

    first_message: Optional[bool] = Field(
        default=None, description="Whether to allow overriding the first_message field."
    )
    language: Optional[bool] = Field(
        default=None, description="Whether to allow overriding the language field."
    )
    max_conversation_duration_message: Optional[bool] = Field(
        default=None,
        description="Whether to allow overriding the max_conversation_duration_message field.",
    )
    prompt: Optional[PromptAgentApiModelOverrideConfig] = Field(default=None)
