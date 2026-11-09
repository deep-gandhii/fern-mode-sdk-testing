from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ConversationConfigOverrideConfig(BaseModel):
    """ConversationConfigOverrideConfig

    :param text_only: Whether to allow overriding the text_only field., defaults to None
    :type text_only: bool, optional
    """

    text_only: Optional[bool] = Field(
        default=None, description="Whether to allow overriding the text_only field."
    )
