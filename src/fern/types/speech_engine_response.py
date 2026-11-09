from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .speech_engine_config import SpeechEngineConfig
from .asr_conversational_config import AsrConversationalConfig
from .tts_conversational_config_output import TtsConversationalConfigOutput
from .base_turn_config import BaseTurnConfig
from .vad_config import VadConfig
from .conversation_config_output import ConversationConfigOutput
from .privacy_config_output import PrivacyConfigOutput
from .agent_call_limits import AgentCallLimits
from .speech_engine_conversation_initiation_client_data_config import (
    SpeechEngineConversationInitiationClientDataConfig,
)
from .agent_metadata_db_model import AgentMetadataDbModel
from .resource_access_info import ResourceAccessInfo


class SpeechEngineResponse(BaseModel):
    """SpeechEngineResponse

    :param speech_engine_id: The speech engine resource ID
    :type speech_engine_id: str
    :param name: Human-readable name for the speech engine
    :type name: str
    :param speech_engine: speech_engine
    :type speech_engine: SpeechEngineConfig
    :param asr: asr
    :type asr: AsrConversationalConfig
    :param tts: tts
    :type tts: TtsConversationalConfigOutput
    :param turn: turn
    :type turn: BaseTurnConfig
    :param vad: vad
    :type vad: VadConfig
    :param conversation: conversation
    :type conversation: ConversationConfigOutput
    :param privacy: privacy
    :type privacy: PrivacyConfigOutput
    :param call_limits: call_limits
    :type call_limits: AgentCallLimits
    :param language: ISO language code used by the speech engine (e.g. 'en')
    :type language: str
    :param tags: Arbitrary tags for categorization and filtering
    :type tags: List[str]
    :param overrides: overrides
    :type overrides: SpeechEngineConversationInitiationClientDataConfig
    :param metadata: metadata
    :type metadata: AgentMetadataDbModel
    :param access_info: The access information of the speech engine for the user, defaults to None
    :type access_info: ResourceAccessInfo, optional
    """

    speech_engine_id: str = Field(description="The speech engine resource ID")
    name: str = Field(description="Human-readable name for the speech engine")
    speech_engine: SpeechEngineConfig
    asr: AsrConversationalConfig
    tts: TtsConversationalConfigOutput
    turn: BaseTurnConfig
    vad: VadConfig
    conversation: ConversationConfigOutput
    privacy: PrivacyConfigOutput
    call_limits: AgentCallLimits
    language: str = Field(
        description="ISO language code used by the speech engine (e.g. 'en')"
    )
    tags: List[str] = Field(
        description="Arbitrary tags for categorization and filtering"
    )
    overrides: SpeechEngineConversationInitiationClientDataConfig
    metadata: AgentMetadataDbModel
    access_info: Optional[ResourceAccessInfo] = Field(
        default=None,
        description="The access information of the speech engine for the user",
    )
