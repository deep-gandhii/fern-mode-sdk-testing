from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .outbound_call_recipient import OutboundCallRecipient
from .batch_call_whats_app_params import BatchCallWhatsAppParams
from .telephony_call_config import TelephonyCallConfig


class BodySubmitABatchCallRequestV1ConvaiBatchCallingSubmitPost(BaseModel):
    """BodySubmitABatchCallRequestV1ConvaiBatchCallingSubmitPost

    :param call_name: call_name
    :type call_name: str
    :param agent_id: agent_id
    :type agent_id: str
    :param recipients: recipients
    :type recipients: List[OutboundCallRecipient]
    :param scheduled_time_unix: scheduled_time_unix, defaults to None
    :type scheduled_time_unix: int, optional
    :param agent_phone_number_id: agent_phone_number_id, defaults to None
    :type agent_phone_number_id: str, optional
    :param whatsapp_params: whatsapp_params, defaults to None
    :type whatsapp_params: BatchCallWhatsAppParams, optional
    :param timezone: timezone, defaults to None
    :type timezone: str, optional
    :param branch_id: branch_id, defaults to None
    :type branch_id: str, optional
    :param environment: environment, defaults to None
    :type environment: str, optional
    :param telephony_call_config: telephony_call_config, defaults to None
    :type telephony_call_config: TelephonyCallConfig, optional
    :param target_concurrency_limit: Maximum number of simultaneous calls for this batch. When set, dispatch is governed by this limit rather than workspace/agent capacity percentages., defaults to None
    :type target_concurrency_limit: int, optional
    """

    call_name: str
    agent_id: str
    recipients: List[OutboundCallRecipient]
    scheduled_time_unix: Optional[int] = Field(default=None)
    agent_phone_number_id: Optional[str] = Field(default=None)
    whatsapp_params: Optional[BatchCallWhatsAppParams] = Field(default=None)
    timezone: Optional[str] = Field(default=None)
    branch_id: Optional[str] = Field(default=None)
    environment: Optional[str] = Field(default=None)
    telephony_call_config: Optional[TelephonyCallConfig] = Field(default=None)
    target_concurrency_limit: Optional[int] = Field(
        default=None,
        description="Maximum number of simultaneous calls for this batch. When set, dispatch is governed by this limit rather than workspace/agent capacity percentages.",
    )
