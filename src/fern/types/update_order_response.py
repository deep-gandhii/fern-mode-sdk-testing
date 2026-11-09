from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class UpdateOrderResponse(BaseModel):
    """UpdateOrderResponse

    :param name: The updated order name.
    :type name: str
    """

    name: str = Field(description="The updated order name.")
