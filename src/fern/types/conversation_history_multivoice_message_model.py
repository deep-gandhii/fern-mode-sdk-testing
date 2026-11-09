from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_history_multivoice_message_part_model import (
    ConversationHistoryMultivoiceMessagePartModel,
)


class ConversationHistoryMultivoiceMessageModel(BaseModel):
    """Represents a message from a multi-voice agent.

    :param parts: parts
    :type parts: List[ConversationHistoryMultivoiceMessagePartModel]
    """

    parts: List[ConversationHistoryMultivoiceMessagePartModel]
