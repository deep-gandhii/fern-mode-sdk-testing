from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .asr_conversational_config_override import AsrConversationalConfigOverride
from .turn_config_override import TurnConfigOverride
from .tts_conversational_config_override import TtsConversationalConfigOverride
from .conversation_config_override import ConversationConfigOverride
from .agent_config_override_input import AgentConfigOverrideInput


class ConversationConfigClientOverrideInput(BaseModel):
    """ConversationConfigClientOverrideInput

    :param asr: Configuration for conversational transcription, defaults to None
    :type asr: AsrConversationalConfigOverride, optional
    :param turn: Configuration for turn detection, defaults to None
    :type turn: TurnConfigOverride, optional
    :param tts: Configuration for conversational text to speech, defaults to None
    :type tts: TtsConversationalConfigOverride, optional
    :param conversation: Configuration for conversational events, defaults to None
    :type conversation: ConversationConfigOverride, optional
    :param agent: Agent specific configuration, defaults to None
    :type agent: AgentConfigOverrideInput, optional
    """

    asr: Optional[AsrConversationalConfigOverride] = Field(
        default=None, description="Configuration for conversational transcription"
    )
    turn: Optional[TurnConfigOverride] = Field(
        default=None, description="Configuration for turn detection"
    )
    tts: Optional[TtsConversationalConfigOverride] = Field(
        default=None, description="Configuration for conversational text to speech"
    )
    conversation: Optional[ConversationConfigOverride] = Field(
        default=None, description="Configuration for conversational events"
    )
    agent: Optional[AgentConfigOverrideInput] = Field(
        default=None, description="Agent specific configuration"
    )
