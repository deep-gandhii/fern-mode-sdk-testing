from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class CreateConversationTagRequestModel(BaseModel):
    """CreateConversationTagRequestModel

    :param title: Display title of the tag.
    :type title: str
    :param description: Optional free-text description., defaults to None
    :type description: str, optional
    """

    title: str = Field(description="Display title of the tag.")
    description: Optional[str] = Field(
        default=None, description="Optional free-text description."
    )
