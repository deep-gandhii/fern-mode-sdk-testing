from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .telephony_direction import TelephonyDirection

ConversationHistorySipTrunkingPhoneCallModelType = typing.Union[
    typing.Literal["sip_trunking"], typing.Any
]


class ConversationHistorySipTrunkingPhoneCallModel(BaseModel):
    """ConversationHistorySipTrunkingPhoneCallModel

    :param direction: direction
    :type direction: TelephonyDirection
    :param phone_number_id: phone_number_id
    :type phone_number_id: str
    :param agent_number: agent_number
    :type agent_number: str
    :param external_number: external_number
    :type external_number: str
    :param type: type
    :type type: ConversationHistorySipTrunkingPhoneCallModelType
    :param call_id: call_id, defaults to None
    :type call_id: str, optional
    :param call_sid: call_sid
    :type call_sid: str
    :param sip_header_dynamic_variables: sip_header_dynamic_variables, defaults to None
    :type sip_header_dynamic_variables: Dict[str, str], optional
    """

    direction: TelephonyDirection
    phone_number_id: str
    agent_number: str
    external_number: str
    type: ConversationHistorySipTrunkingPhoneCallModelType = Field(
        default="sip_trunking"
    )
    call_id: Optional[str] = Field(default=None)
    call_sid: str
    sip_header_dynamic_variables: Optional[Dict[str, str]] = Field(default=None)
