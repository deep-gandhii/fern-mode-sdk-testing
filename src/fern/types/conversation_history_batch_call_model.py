from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ConversationHistoryBatchCallModel(BaseModel):
    """ConversationHistoryBatchCallModel

    :param batch_call_id: batch_call_id
    :type batch_call_id: str
    :param batch_call_recipient_id: batch_call_recipient_id
    :type batch_call_recipient_id: str
    """

    batch_call_id: str
    batch_call_recipient_id: str
