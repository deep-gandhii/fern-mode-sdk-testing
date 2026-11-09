from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .conversation_deletion_settings import ConversationDeletionSettings
from .conversation_history_feedback_common_model import (
    ConversationHistoryFeedbackCommonModel,
)
from .authorization_method import AuthorizationMethod
from .conversation_charging_common_model import ConversationChargingCommonModel
from .conversation_history_batch_call_model import ConversationHistoryBatchCallModel
from .conversation_history_error_common_model import ConversationHistoryErrorCommonModel
from .conversation_history_rag_usage_common_model import (
    ConversationHistoryRagUsageCommonModel,
)
from .features_usage_common_model import FeaturesUsageCommonModel
from .conversation_history_eleven_assistant_common_model import (
    ConversationHistoryElevenAssistantCommonModel,
)
from .conversation_initiation_source import ConversationInitiationSource
from .async_conversation_metadata import AsyncConversationMetadata
from .whats_app_conversation_info import WhatsAppConversationInfo
from .sms_conversation_info import SmsConversationInfo
from .agent_definition_source import AgentDefinitionSource
from .conversation_voice_reward_model import ConversationVoiceRewardModel
from .conversation_history_twilio_phone_call_model import (
    ConversationHistoryTwilioPhoneCallModel,
)
from .conversation_history_exotel_phone_call_model import (
    ConversationHistoryExotelPhoneCallModel,
)
from .conversation_history_sip_trunking_phone_call_model import (
    ConversationHistorySipTrunkingPhoneCallModel,
)


# fernMode variant type for a shared-component member of ConversationHistoryMetadataCommonModelPhoneCall
class ConversationHistoryMetadataCommonModelPhoneCall_Twilio(
    ConversationHistoryTwilioPhoneCallModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryMetadataCommonModelPhoneCall
class ConversationHistoryMetadataCommonModelPhoneCall_Exotel(
    ConversationHistoryExotelPhoneCallModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryMetadataCommonModelPhoneCall
class ConversationHistoryMetadataCommonModelPhoneCall_SipTrunking(
    ConversationHistorySipTrunkingPhoneCallModel
):
    pass


# Union type for ConversationHistoryMetadataCommonModelPhoneCall
# Pydantic will attempt to validate against each type in order
ConversationHistoryMetadataCommonModelPhoneCall = Union[
    ConversationHistoryTwilioPhoneCallModel,
    ConversationHistoryExotelPhoneCallModel,
    ConversationHistorySipTrunkingPhoneCallModel,
]
# TypeAdapter for runtime validation of ConversationHistoryMetadataCommonModelPhoneCall
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ConversationHistoryMetadataCommonModelPhoneCall_adapter = TypeAdapter(
    ConversationHistoryMetadataCommonModelPhoneCall
)


class ConversationHistoryMetadataCommonModel(BaseModel):
    """ConversationHistoryMetadataCommonModel

    :param start_time_unix_secs: start_time_unix_secs
    :type start_time_unix_secs: int
    :param accepted_time_unix_secs: accepted_time_unix_secs, defaults to None
    :type accepted_time_unix_secs: int, optional
    :param call_duration_secs: call_duration_secs
    :type call_duration_secs: int
    :param cost: cost, defaults to None
    :type cost: int, optional
    :param deletion_settings: deletion_settings, defaults to None
    :type deletion_settings: ConversationDeletionSettings, optional
    :param feedback: feedback, defaults to None
    :type feedback: ConversationHistoryFeedbackCommonModel, optional
    :param authorization_method: authorization_method, defaults to None
    :type authorization_method: AuthorizationMethod, optional
    :param charging: charging, defaults to None
    :type charging: ConversationChargingCommonModel, optional
    :param phone_call: phone_call, defaults to None
    :type phone_call: ConversationHistoryMetadataCommonModelPhoneCall, optional
    :param batch_call: batch_call, defaults to None
    :type batch_call: ConversationHistoryBatchCallModel, optional
    :param termination_reason: termination_reason, defaults to None
    :type termination_reason: str, optional
    :param error: error, defaults to None
    :type error: ConversationHistoryErrorCommonModel, optional
    :param warnings: warnings, defaults to None
    :type warnings: List[str], optional
    :param main_language: main_language, defaults to None
    :type main_language: str, optional
    :param rag_usage: rag_usage, defaults to None
    :type rag_usage: ConversationHistoryRagUsageCommonModel, optional
    :param text_only: text_only, defaults to None
    :type text_only: bool, optional
    :param features_usage: features_usage, defaults to None
    :type features_usage: FeaturesUsageCommonModel, optional
    :param eleven_assistant: eleven_assistant, defaults to None
    :type eleven_assistant: ConversationHistoryElevenAssistantCommonModel, optional
    :param initiator_id: initiator_id, defaults to None
    :type initiator_id: str, optional
    :param conversation_initiation_source: Enum representing the possible sources for conversation initiation., defaults to None
    :type conversation_initiation_source: ConversationInitiationSource, optional
    :param conversation_initiation_source_version: conversation_initiation_source_version, defaults to None
    :type conversation_initiation_source_version: str, optional
    :param timezone: timezone, defaults to None
    :type timezone: str, optional
    :param async_metadata: async_metadata, defaults to None
    :type async_metadata: AsyncConversationMetadata, optional
    :param whatsapp: whatsapp, defaults to None
    :type whatsapp: WhatsAppConversationInfo, optional
    :param sms: sms, defaults to None
    :type sms: SmsConversationInfo, optional
    :param agent_created_from: agent_created_from, defaults to None
    :type agent_created_from: AgentDefinitionSource, optional
    :param agent_last_updated_from: agent_last_updated_from, defaults to None
    :type agent_last_updated_from: AgentDefinitionSource, optional
    :param voice_rewards: voice_rewards, defaults to None
    :type voice_rewards: List[ConversationVoiceRewardModel], optional
    :param cost_fiat: Total fiat cost of the conversation in USD, i.e. the sum of the LLM price and the non-LLM platform price (the fiat analogue of ``cost``). ``None`` when neither is set (e.g. conversations that predate fiat cost tracking)., defaults to None
    :type cost_fiat: float, optional
    """

    start_time_unix_secs: int
    accepted_time_unix_secs: Optional[int] = Field(default=None)
    call_duration_secs: int
    cost: Optional[int] = Field(default=None)
    deletion_settings: Optional[ConversationDeletionSettings] = Field(default=None)
    feedback: Optional[ConversationHistoryFeedbackCommonModel] = Field(default=None)
    authorization_method: Optional[AuthorizationMethod] = Field(default=None)
    charging: Optional[ConversationChargingCommonModel] = Field(default=None)
    phone_call: Optional[ConversationHistoryMetadataCommonModelPhoneCall] = Field(
        default=None
    )
    batch_call: Optional[ConversationHistoryBatchCallModel] = Field(default=None)
    termination_reason: Optional[str] = Field(default=None)
    error: Optional[ConversationHistoryErrorCommonModel] = Field(default=None)
    warnings: Optional[List[str]] = Field(default=None)
    main_language: Optional[str] = Field(default=None)
    rag_usage: Optional[ConversationHistoryRagUsageCommonModel] = Field(default=None)
    text_only: Optional[bool] = Field(default=None)
    features_usage: Optional[FeaturesUsageCommonModel] = Field(default=None)
    eleven_assistant: Optional[ConversationHistoryElevenAssistantCommonModel] = Field(
        default=None
    )
    initiator_id: Optional[str] = Field(default=None)
    conversation_initiation_source: Optional[ConversationInitiationSource] = Field(
        default=None,
        description="Enum representing the possible sources for conversation initiation.",
    )
    conversation_initiation_source_version: Optional[str] = Field(default=None)
    timezone: Optional[str] = Field(default=None)
    async_metadata: Optional[AsyncConversationMetadata] = Field(default=None)
    whatsapp: Optional[WhatsAppConversationInfo] = Field(default=None)
    sms: Optional[SmsConversationInfo] = Field(default=None)
    agent_created_from: Optional[AgentDefinitionSource] = Field(default=None)
    agent_last_updated_from: Optional[AgentDefinitionSource] = Field(default=None)
    voice_rewards: Optional[List[ConversationVoiceRewardModel]] = Field(default=None)
    cost_fiat: Optional[float] = Field(
        default=None,
        description="Total fiat cost of the conversation in USD, i.e. the sum of the LLM price and the non-LLM platform price (the fiat analogue of ``cost``). ``None`` when neither is set (e.g. conversations that predate fiat cost tracking).",
    )
