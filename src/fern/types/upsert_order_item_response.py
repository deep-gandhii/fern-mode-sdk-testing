from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .quote_info import QuoteInfo


class UpsertOrderItemResponse(BaseModel):
    """UpsertOrderItemResponse

    :param item_id: item_id
    :type item_id: str
    :param quote: The quoted price for this item., defaults to None
    :type quote: QuoteInfo, optional
    """

    item_id: str
    quote: Optional[QuoteInfo] = Field(
        default=None, description="The quoted price for this item."
    )
