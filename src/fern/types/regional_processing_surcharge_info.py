from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class RegionalProcessingSurchargeInfo(BaseModel):
    """RegionalProcessingSurchargeInfo

    :param multiplier: The surcharge multiplier applied to this model's pricing (e.g. 1.1 for a 10% surcharge).
    :type multiplier: float
    """

    multiplier: float = Field(
        description="The surcharge multiplier applied to this model's pricing (e.g. 1.1 for a 10% surcharge)."
    )
