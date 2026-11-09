from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AllowlistItem(BaseModel):
    """AllowlistItem

    :param hostname: The hostname of the allowed origin
    :type hostname: str
    """

    hostname: str = Field(description="The hostname of the allowed origin")
