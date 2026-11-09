from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .sip_log_message import SipLogMessage


class GetSipLogMessagesResponse(BaseModel):
    """GetSipLogMessagesResponse

    :param sip_messages: sip_messages
    :type sip_messages: List[SipLogMessage]
    :param next_cursor: next_cursor, defaults to None
    :type next_cursor: str, optional
    :param has_more: has_more, defaults to None
    :type has_more: bool, optional
    """

    sip_messages: List[SipLogMessage]
    next_cursor: Optional[str] = Field(default=None)
    has_more: Optional[bool] = Field(default=None)
