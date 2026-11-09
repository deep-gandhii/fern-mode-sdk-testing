from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class CreateOrderResponse(BaseModel):
    """CreateOrderResponse

    :param order_id: order_id
    :type order_id: str
    :param sandbox: Whether this is a sandbox order., defaults to None
    :type sandbox: bool, optional
    """

    order_id: str
    sandbox: Optional[bool] = Field(
        default=None, description="Whether this is a sandbox order."
    )
