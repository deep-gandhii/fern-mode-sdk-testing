from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .webhook_event_type import WebhookEventType
from .webhook_transcript_format import WebhookTranscriptFormat


class ConvAiWebhooks(BaseModel):
    """ConvAiWebhooks

    :param post_call_webhook_id: post_call_webhook_id, defaults to None
    :type post_call_webhook_id: str, optional
    :param events: List of event types to send via webhook. Options: transcript, audio, call_initiation_failure, unredacted_transcript, unredacted_audio., defaults to None
    :type events: List[WebhookEventType], optional
    :param transcript_format: transcript_format, defaults to None
    :type transcript_format: WebhookTranscriptFormat, optional
    :param send_audio: DEPRECATED: Use 'events' field instead. Whether to send audio data with post-call webhooks for ConvAI conversations, defaults to None
    :type send_audio: bool, optional
    """

    post_call_webhook_id: Optional[str] = Field(default=None)
    events: Optional[List[WebhookEventType]] = Field(
        default=None,
        description="List of event types to send via webhook. Options: transcript, audio, call_initiation_failure, unredacted_transcript, unredacted_audio.",
    )
    transcript_format: Optional[WebhookTranscriptFormat] = Field(default=None)
    send_audio: Optional[bool] = Field(
        default=None,
        description="DEPRECATED: Use 'events' field instead. Whether to send audio data with post-call webhooks for ConvAI conversations",
    )
