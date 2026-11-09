from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .speech_engine_config import SpeechEngineConfig
from .asr_conversational_config import AsrConversationalConfig
from .tts_conversational_config_input import TtsConversationalConfigInput
from .base_turn_config import BaseTurnConfig
from .vad_config import VadConfig
from .conversation_config_input import ConversationConfigInput
from .privacy_config_input import PrivacyConfigInput
from .agent_call_limits import AgentCallLimits
from .speech_engine_conversation_initiation_client_data_config import (
    SpeechEngineConversationInitiationClientDataConfig,
)


class CreateSpeechEngineRequest(BaseModel):
    """CreateSpeechEngineRequest

    :param name: Name of the speech engine, defaults to None
    :type name: str, optional
    :param speech_engine: speech_engine
    :type speech_engine: SpeechEngineConfig
    :param asr: asr, defaults to None
    :type asr: AsrConversationalConfig, optional
    :param tts: tts, defaults to None
    :type tts: TtsConversationalConfigInput, optional
    :param turn: turn, defaults to None
    :type turn: BaseTurnConfig, optional
    :param vad: vad, defaults to None
    :type vad: VadConfig, optional
    :param conversation: conversation, defaults to None
    :type conversation: ConversationConfigInput, optional
    :param privacy: privacy, defaults to None
    :type privacy: PrivacyConfigInput, optional
    :param call_limits: call_limits, defaults to None
    :type call_limits: AgentCallLimits, optional
    :param language: Language for the speech engine, defaults to None
    :type language: str, optional
    :param tags: Tags for categorization, defaults to None
    :type tags: List[str], optional
    :param overrides: overrides, defaults to None
    :type overrides: SpeechEngineConversationInitiationClientDataConfig, optional
    """

    name: Optional[str] = Field(default=None, description="Name of the speech engine")
    speech_engine: SpeechEngineConfig
    asr: Optional[AsrConversationalConfig] = Field(default=None)
    tts: Optional[TtsConversationalConfigInput] = Field(default=None)
    turn: Optional[BaseTurnConfig] = Field(default=None)
    vad: Optional[VadConfig] = Field(default=None)
    conversation: Optional[ConversationConfigInput] = Field(default=None)
    privacy: Optional[PrivacyConfigInput] = Field(default=None)
    call_limits: Optional[AgentCallLimits] = Field(default=None)
    language: Optional[str] = Field(
        default=None, description="Language for the speech engine"
    )
    tags: Optional[List[str]] = Field(
        default=None, description="Tags for categorization"
    )
    overrides: Optional[SpeechEngineConversationInitiationClientDataConfig] = Field(
        default=None
    )
