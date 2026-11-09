from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class DiscountResponseModel(BaseModel):
    """DiscountResponseModel

    :param discount_percent_off: The discount applied to the invoice. E.g. [20.0f] for 20% off., defaults to None
    :type discount_percent_off: float, optional
    :param discount_amount_off: The discount applied to the invoice. E.g. [20.0f] for 20 cents off., defaults to None
    :type discount_amount_off: float, optional
    """

    discount_percent_off: Optional[float] = Field(
        default=None,
        description="The discount applied to the invoice. E.g. [20.0f] for 20% off.",
    )
    discount_amount_off: Optional[float] = Field(
        default=None,
        description="The discount applied to the invoice. E.g. [20.0f] for 20 cents off.",
    )
