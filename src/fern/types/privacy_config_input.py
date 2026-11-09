from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .conversation_history_redaction_config import ConversationHistoryRedactionConfig


class PrivacyConfigInput(BaseModel):
    """PrivacyConfigInput

    :param record_voice: Whether to record the conversation, defaults to None
    :type record_voice: bool, optional
    :param retention_days: The number of days to retain the conversation. -1 indicates there is no retention limit, defaults to None
    :type retention_days: int, optional
    :param delete_transcript_and_pii: Whether to delete the transcript and PII, defaults to None
    :type delete_transcript_and_pii: bool, optional
    :param delete_audio: Whether to delete the audio, defaults to None
    :type delete_audio: bool, optional
    :param apply_to_existing_conversations: Whether to apply the privacy settings to existing conversations, defaults to None
    :type apply_to_existing_conversations: bool, optional
    :param zero_retention_mode: Whether to enable zero retention mode - no PII data is stored, defaults to None
    :type zero_retention_mode: bool, optional
    :param conversation_history_redaction: conversation_history_redaction, defaults to None
    :type conversation_history_redaction: ConversationHistoryRedactionConfig, optional
    """

    record_voice: Optional[bool] = Field(
        default=None, description="Whether to record the conversation"
    )
    retention_days: Optional[int] = Field(
        default=None,
        description="The number of days to retain the conversation. -1 indicates there is no retention limit",
    )
    delete_transcript_and_pii: Optional[bool] = Field(
        default=None, description="Whether to delete the transcript and PII"
    )
    delete_audio: Optional[bool] = Field(
        default=None, description="Whether to delete the audio"
    )
    apply_to_existing_conversations: Optional[bool] = Field(
        default=None,
        description="Whether to apply the privacy settings to existing conversations",
    )
    zero_retention_mode: Optional[bool] = Field(
        default=None,
        description="Whether to enable zero retention mode - no PII data is stored",
    )
    conversation_history_redaction: Optional[ConversationHistoryRedactionConfig] = (
        Field(default=None)
    )
