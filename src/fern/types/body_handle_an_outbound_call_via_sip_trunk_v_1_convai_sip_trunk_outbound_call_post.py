from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_initiation_client_data_request_input import (
    ConversationInitiationClientDataRequestInput,
)
from .telephony_call_config import TelephonyCallConfig


class BodyHandleAnOutboundCallViaSipTrunkV1ConvaiSipTrunkOutboundCallPost(BaseModel):
    """BodyHandleAnOutboundCallViaSipTrunkV1ConvaiSipTrunkOutboundCallPost

    :param agent_id: agent_id
    :type agent_id: str
    :param agent_phone_number_id: agent_phone_number_id
    :type agent_phone_number_id: str
    :param to_number: to_number
    :type to_number: str
    :param conversation_initiation_client_data: conversation_initiation_client_data, defaults to None
    :type conversation_initiation_client_data: ConversationInitiationClientDataRequestInput, optional
    :param telephony_call_config: telephony_call_config, defaults to None
    :type telephony_call_config: TelephonyCallConfig, optional
    """

    agent_id: str
    agent_phone_number_id: str
    to_number: str
    conversation_initiation_client_data: Optional[
        ConversationInitiationClientDataRequestInput
    ] = Field(default=None)
    telephony_call_config: Optional[TelephonyCallConfig] = Field(default=None)
