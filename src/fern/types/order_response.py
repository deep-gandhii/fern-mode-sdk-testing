from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .order_state import OrderState
from .order_item_info import OrderItemInfo


class OrderResponse(BaseModel):
    """OrderResponse

    :param order_id: order_id
    :type order_id: str
    :param name: The display name of the order.
    :type name: str
    :param state: state
    :type state: OrderState
    :param items: The list of items in this order with their quotes.
    :type items: List[OrderItemInfo]
    :param total_amount_usd: The total price for all items in USD. Excluded from response until quotes are available., defaults to None
    :type total_amount_usd: float, optional
    :param sandbox: Whether this is a sandbox order that auto-progresses without producer intervention., defaults to None
    :type sandbox: bool, optional
    :param created_at: The timestamp when the order was created.
    :type created_at: str
    :param submitted_at: The timestamp when the order was submitted, if applicable., defaults to None
    :type submitted_at: str, optional
    :param paid_at: The timestamp when payment was received, if applicable., defaults to None
    :type paid_at: str, optional
    :param accepted_at: The timestamp when the order was accepted for production, if applicable., defaults to None
    :type accepted_at: str, optional
    :param completed_at: The timestamp when the order was completed, if applicable., defaults to None
    :type completed_at: str, optional
    """

    order_id: str
    name: str = Field(description="The display name of the order.")
    state: OrderState
    items: List[OrderItemInfo] = Field(
        description="The list of items in this order with their quotes."
    )
    total_amount_usd: Optional[float] = Field(
        default=None,
        description="The total price for all items in USD. Excluded from response until quotes are available.",
    )
    sandbox: Optional[bool] = Field(
        default=None,
        description="Whether this is a sandbox order that auto-progresses without producer intervention.",
    )
    created_at: str = Field(description="The timestamp when the order was created.")
    submitted_at: Optional[str] = Field(
        default=None,
        description="The timestamp when the order was submitted, if applicable.",
    )
    paid_at: Optional[str] = Field(
        default=None,
        description="The timestamp when payment was received, if applicable.",
    )
    accepted_at: Optional[str] = Field(
        default=None,
        description="The timestamp when the order was accepted for production, if applicable.",
    )
    completed_at: Optional[str] = Field(
        default=None,
        description="The timestamp when the order was completed, if applicable.",
    )
