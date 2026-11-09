from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .sip_log_message_direction import SipLogMessageDirection


class SipLogMessage(BaseModel):
    """SipLogMessage

    :param call_id: call_id
    :type call_id: str
    :param phone_numbers: phone_numbers
    :type phone_numbers: List[str]
    :param local_address: local_address
    :type local_address: str
    :param remote_address: remote_address
    :type remote_address: str
    :param transport: transport
    :type transport: str
    :param raw_message: raw_message
    :type raw_message: str
    :param error_message: error_message
    :type error_message: str
    :param direction: direction
    :type direction: SipLogMessageDirection
    :param created_at_unix_micro: created_at_unix_micro
    :type created_at_unix_micro: int
    """

    call_id: str
    phone_numbers: List[str]
    local_address: str
    remote_address: str
    transport: str
    raw_message: str
    error_message: str
    direction: SipLogMessageDirection
    created_at_unix_micro: int
