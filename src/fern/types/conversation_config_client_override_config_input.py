from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .asr_conversational_config_override_config import (
    AsrConversationalConfigOverrideConfig,
)
from .turn_config_override_config import TurnConfigOverrideConfig
from .tts_conversational_config_override_config import (
    TtsConversationalConfigOverrideConfig,
)
from .conversation_config_override_config import ConversationConfigOverrideConfig
from .agent_config_override_config import AgentConfigOverrideConfig


class ConversationConfigClientOverrideConfigInput(BaseModel):
    """ConversationConfigClientOverrideConfigInput

    :param asr: asr, defaults to None
    :type asr: AsrConversationalConfigOverrideConfig, optional
    :param turn: turn, defaults to None
    :type turn: TurnConfigOverrideConfig, optional
    :param tts: tts, defaults to None
    :type tts: TtsConversationalConfigOverrideConfig, optional
    :param conversation: conversation, defaults to None
    :type conversation: ConversationConfigOverrideConfig, optional
    :param agent: agent, defaults to None
    :type agent: AgentConfigOverrideConfig, optional
    """

    asr: Optional[AsrConversationalConfigOverrideConfig] = Field(default=None)
    turn: Optional[TurnConfigOverrideConfig] = Field(default=None)
    tts: Optional[TtsConversationalConfigOverrideConfig] = Field(default=None)
    conversation: Optional[ConversationConfigOverrideConfig] = Field(default=None)
    agent: Optional[AgentConfigOverrideConfig] = Field(default=None)
