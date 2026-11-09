from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .telephony_direction import TelephonyDirection
from .conversation_initiation_client_data_request_input import (
    ConversationInitiationClientDataRequestInput,
)


class BodyRegisterATwilioCallAndReturnTwiMlV1ConvaiTwilioRegisterCallPost(BaseModel):
    """BodyRegisterATwilioCallAndReturnTwiMlV1ConvaiTwilioRegisterCallPost

    :param agent_id: agent_id
    :type agent_id: str
    :param from_number: from_number
    :type from_number: str
    :param to_number: to_number
    :type to_number: str
    :param direction: direction, defaults to None
    :type direction: TelephonyDirection, optional
    :param conversation_initiation_client_data: conversation_initiation_client_data, defaults to None
    :type conversation_initiation_client_data: ConversationInitiationClientDataRequestInput, optional
    """

    agent_id: str
    from_number: str
    to_number: str
    direction: Optional[TelephonyDirection] = Field(default=None)
    conversation_initiation_client_data: Optional[
        ConversationInitiationClientDataRequestInput
    ] = Field(default=None)
