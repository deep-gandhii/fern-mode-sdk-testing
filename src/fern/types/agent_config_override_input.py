from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .prompt_agent_api_model_override_input import PromptAgentApiModelOverrideInput


class AgentConfigOverrideInput(BaseModel):
    """AgentConfigOverrideInput

    :param first_message: If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion., defaults to None
    :type first_message: str, optional
    :param language: Language of the agent - used for ASR and TTS, defaults to None
    :type language: str, optional
    :param max_conversation_duration_message: If non-empty, the message the agent will send when max conversation duration is reached., defaults to None
    :type max_conversation_duration_message: str, optional
    :param prompt: The prompt for the agent, defaults to None
    :type prompt: PromptAgentApiModelOverrideInput, optional
    """

    first_message: Optional[str] = Field(
        default=None,
        description="If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.",
    )
    language: Optional[str] = Field(
        default=None, description="Language of the agent - used for ASR and TTS"
    )
    max_conversation_duration_message: Optional[str] = Field(
        default=None,
        description="If non-empty, the message the agent will send when max conversation duration is reached.",
    )
    prompt: Optional[PromptAgentApiModelOverrideInput] = Field(
        default=None, description="The prompt for the agent"
    )
