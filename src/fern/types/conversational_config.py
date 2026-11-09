from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .asr_conversational_config import AsrConversationalConfig
from .turn_config import TurnConfig
from .tts_conversational_config_output import TtsConversationalConfigOutput
from .conversation_config_output import ConversationConfigOutput
from .language_preset_output import LanguagePresetOutput
from .vad_config import VadConfig
from .agent_config import AgentConfig


class ConversationalConfig(BaseModel):
    """ConversationalConfig

    :param asr: asr, defaults to None
    :type asr: AsrConversationalConfig, optional
    :param turn: turn, defaults to None
    :type turn: TurnConfig, optional
    :param tts: tts, defaults to None
    :type tts: TtsConversationalConfigOutput, optional
    :param conversation: conversation, defaults to None
    :type conversation: ConversationConfigOutput, optional
    :param language_presets: Language presets for conversations, defaults to None
    :type language_presets: Dict[str, LanguagePresetOutput], optional
    :param vad: vad, defaults to None
    :type vad: VadConfig, optional
    :param agent: agent, defaults to None
    :type agent: AgentConfig, optional
    """

    asr: Optional[AsrConversationalConfig] = Field(default=None)
    turn: Optional[TurnConfig] = Field(default=None)
    tts: Optional[TtsConversationalConfigOutput] = Field(default=None)
    conversation: Optional[ConversationConfigOutput] = Field(default=None)
    language_presets: Optional[Dict[str, LanguagePresetOutput]] = Field(
        default=None, description="Language presets for conversations"
    )
    vad: Optional[VadConfig] = Field(default=None)
    agent: Optional[AgentConfig] = Field(default=None)
