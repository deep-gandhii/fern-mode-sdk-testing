from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ConversationHistoryErrorCommonModel(BaseModel):
    """ConversationHistoryErrorCommonModel

    :param code: code
    :type code: int
    :param reason: reason, defaults to None
    :type reason: str, optional
    """

    code: int
    reason: Optional[str] = Field(default=None)
