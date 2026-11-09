from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class RemoveOrderItemResponse(BaseModel):
    """RemoveOrderItemResponse

    :param success: Whether the item was successfully removed.
    :type success: bool
    """

    success: bool = Field(description="Whether the item was successfully removed.")
