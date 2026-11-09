from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ConversationReasoningModel(BaseModel):
    """ConversationReasoningModel

    :param summary: summary, defaults to None
    :type summary: str, optional
    :param provider_redact: provider_redact, defaults to None
    :type provider_redact: bool, optional
    """

    summary: Optional[str] = Field(default=None)
    provider_redact: Optional[bool] = Field(default=None)
