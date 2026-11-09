from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class QuoteInfo(BaseModel):
    """QuoteInfo

    :param amount_usd: The quoted price for this item in USD. Use the order's total_amount_usd for the combined order total.
    :type amount_usd: float
    """

    amount_usd: float = Field(
        description="The quoted price for this item in USD. Use the order's total_amount_usd for the combined order total."
    )
