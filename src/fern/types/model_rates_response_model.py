from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ModelRatesResponseModel(BaseModel):
    """ModelRatesResponseModel

    :param character_cost_multiplier: The cost multiplier for characters.
    :type character_cost_multiplier: float
    :param cost_discount_multiplier: Discount multiplier applied to cost estimates. Defaults to 1.0 (no discount)., defaults to None
    :type cost_discount_multiplier: float, optional
    """

    character_cost_multiplier: float = Field(
        description="The cost multiplier for characters."
    )
    cost_discount_multiplier: Optional[float] = Field(
        default=None,
        description="Discount multiplier applied to cost estimates. Defaults to 1.0 (no discount).",
    )
