from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class UpdateOrderRequest(BaseModel):
    """UpdateOrderRequest

    :param name: The new name for the order.
    :type name: str
    """

    name: str = Field(description="The new name for the order.")
