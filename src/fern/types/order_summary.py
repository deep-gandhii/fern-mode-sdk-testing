from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .order_state import OrderState


class OrderSummary(BaseModel):
    """OrderSummary

    :param order_id: order_id
    :type order_id: str
    :param name: The display name of the order.
    :type name: str
    :param state: state
    :type state: OrderState
    :param total_amount_usd: The total price for all items in USD. Excluded from response until quotes are available., defaults to None
    :type total_amount_usd: float, optional
    :param sandbox: Whether this is a sandbox order that auto-progresses without producer intervention., defaults to None
    :type sandbox: bool, optional
    :param submitted_at: The timestamp when the order was submitted, if applicable., defaults to None
    :type submitted_at: str, optional
    :param updated_at: The timestamp when the order was last modified, if applicable., defaults to None
    :type updated_at: str, optional
    """

    order_id: str
    name: str = Field(description="The display name of the order.")
    state: OrderState
    total_amount_usd: Optional[float] = Field(
        default=None,
        description="The total price for all items in USD. Excluded from response until quotes are available.",
    )
    sandbox: Optional[bool] = Field(
        default=None,
        description="Whether this is a sandbox order that auto-progresses without producer intervention.",
    )
    submitted_at: Optional[str] = Field(
        default=None,
        description="The timestamp when the order was submitted, if applicable.",
    )
    updated_at: Optional[str] = Field(
        default=None,
        description="The timestamp when the order was last modified, if applicable.",
    )
