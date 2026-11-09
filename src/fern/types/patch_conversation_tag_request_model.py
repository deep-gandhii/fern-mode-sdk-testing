from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class PatchConversationTagRequestModel(BaseModel):
    """PatchConversationTagRequestModel

    :param title: If provided, replaces the tag title. Omit to leave unchanged., defaults to None
    :type title: str, optional
    :param description: If provided, replaces the tag description. Omit to leave unchanged., defaults to None
    :type description: str, optional
    """

    title: Optional[str] = Field(
        default=None,
        description="If provided, replaces the tag title. Omit to leave unchanged.",
    )
    description: Optional[str] = Field(
        default=None,
        description="If provided, replaces the tag description. Omit to leave unchanged.",
    )
