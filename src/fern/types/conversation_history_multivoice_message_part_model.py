from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ConversationHistoryMultivoiceMessagePartModel(BaseModel):
    """Represents a single voice part of a multi-voice message.

    :param text: text
    :type text: str
    :param voice_label: voice_label
    :type voice_label: str
    :param time_in_call_secs: time_in_call_secs
    :type time_in_call_secs: int
    """

    text: str
    voice_label: Optional[str]
    time_in_call_secs: Optional[int]
