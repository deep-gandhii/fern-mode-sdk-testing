from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .order_state import OrderState


class SubmitOrderResponse(BaseModel):
    """SubmitOrderResponse

    :param order_id: order_id
    :type order_id: str
    :param state: state
    :type state: OrderState
    :param submitted_at: The timestamp when the order was submitted.
    :type submitted_at: str
    """

    order_id: str
    state: OrderState
    submitted_at: str = Field(description="The timestamp when the order was submitted.")
