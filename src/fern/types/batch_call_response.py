from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .telephony_provider import TelephonyProvider
from .batch_call_whats_app_params import BatchCallWhatsAppParams
from .batch_call_status import BatchCallStatus
from .telephony_call_config import TelephonyCallConfig


class BatchCallResponse(BaseModel):
    """BatchCallResponse

    :param id: id
    :type id: str
    :param phone_number_id: phone_number_id
    :type phone_number_id: str
    :param phone_provider: phone_provider
    :type phone_provider: TelephonyProvider
    :param whatsapp_params: whatsapp_params
    :type whatsapp_params: BatchCallWhatsAppParams
    :param name: name
    :type name: str
    :param agent_id: agent_id
    :type agent_id: str
    :param branch_id: branch_id
    :type branch_id: str
    :param environment: environment
    :type environment: str
    :param created_at_unix: created_at_unix
    :type created_at_unix: int
    :param scheduled_time_unix: scheduled_time_unix
    :type scheduled_time_unix: int
    :param timezone: timezone
    :type timezone: str
    :param total_calls_dispatched: total_calls_dispatched
    :type total_calls_dispatched: int
    :param total_calls_scheduled: total_calls_scheduled
    :type total_calls_scheduled: int
    :param total_calls_finished: total_calls_finished
    :type total_calls_finished: int
    :param last_updated_at_unix: last_updated_at_unix
    :type last_updated_at_unix: int
    :param status: status
    :type status: BatchCallStatus
    :param retry_count: retry_count
    :type retry_count: int
    :param telephony_call_config: telephony_call_config
    :type telephony_call_config: TelephonyCallConfig
    :param target_concurrency_limit: Maximum number of simultaneous calls for this batch. When set, dispatch is governed by this limit rather than workspace/agent capacity percentages.
    :type target_concurrency_limit: int
    :param agent_name: agent_name
    :type agent_name: str
    :param branch_name: branch_name
    :type branch_name: str
    """

    id: str
    phone_number_id: Optional[str]
    phone_provider: TelephonyProvider
    whatsapp_params: BatchCallWhatsAppParams
    name: str
    agent_id: str
    branch_id: Optional[str]
    environment: Optional[str]
    created_at_unix: int
    scheduled_time_unix: int
    timezone: Optional[str]
    total_calls_dispatched: int
    total_calls_scheduled: int
    total_calls_finished: int
    last_updated_at_unix: int
    status: BatchCallStatus
    retry_count: int
    telephony_call_config: TelephonyCallConfig
    target_concurrency_limit: Optional[int] = Field(
        description="Maximum number of simultaneous calls for this batch. When set, dispatch is governed by this limit rather than workspace/agent capacity percentages."
    )
    agent_name: str
    branch_name: Optional[str]
