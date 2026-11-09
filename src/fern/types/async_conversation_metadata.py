from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

AsyncConversationMetadataDeliveryStatus = typing.Union[
    typing.Literal["pending", "success", "failed"], typing.Any
]


class AsyncConversationMetadata(BaseModel):
    """Metadata for async conversation delivery (Zendesk, Slack, etc.).

    :param delivery_status: delivery_status
    :type delivery_status: AsyncConversationMetadataDeliveryStatus
    :param delivery_timestamp: delivery_timestamp
    :type delivery_timestamp: int
    :param delivery_error: delivery_error, defaults to None
    :type delivery_error: str, optional
    :param external_system: external_system
    :type external_system: str
    :param external_id: external_id
    :type external_id: str
    :param external_link: external_link, defaults to None
    :type external_link: str, optional
    :param retry_count: retry_count, defaults to None
    :type retry_count: int, optional
    :param last_retry_timestamp: last_retry_timestamp, defaults to None
    :type last_retry_timestamp: int, optional
    :param last_processed_external_message_id: last_processed_external_message_id, defaults to None
    :type last_processed_external_message_id: str, optional
    """

    delivery_status: AsyncConversationMetadataDeliveryStatus
    delivery_timestamp: int
    delivery_error: Optional[str] = Field(default=None)
    external_system: str
    external_id: str
    external_link: Optional[str] = Field(default=None)
    retry_count: Optional[int] = Field(default=None)
    last_retry_timestamp: Optional[int] = Field(default=None)
    last_processed_external_message_id: Optional[str] = Field(default=None)
