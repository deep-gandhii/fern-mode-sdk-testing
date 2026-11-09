from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .order_summary import OrderSummary


class ListOrdersResponse(BaseModel):
    """ListOrdersResponse

    :param orders: The list of orders matching the query.
    :type orders: List[OrderSummary]
    """

    orders: List[OrderSummary] = Field(
        description="The list of orders matching the query."
    )
