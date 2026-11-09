from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ConversationConfigOverride(BaseModel):
    """ConversationConfigOverride

    :param text_only: If enabled audio will not be processed and only text will be used, use to avoid audio pricing., defaults to None
    :type text_only: bool, optional
    """

    text_only: Optional[bool] = Field(
        default=None,
        description="If enabled audio will not be processed and only text will be used, use to avoid audio pricing.",
    )
