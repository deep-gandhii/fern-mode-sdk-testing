from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .order_item_request_output import (
    OrderItemRequestOutput,
    OrderItemRequestOutput_adapter,
)
from .dub_order_item_request import DubOrderItemRequest
from .subtitle_order_item_request import SubtitleOrderItemRequest
from .transcription_order_item_request import TranscriptionOrderItemRequest
from .quote_info import QuoteInfo


class OrderItemInfo(BaseModel):
    """OrderItemInfo

    :param item_id: item_id
    :type item_id: str
    :param item: item
    :type item: OrderItemRequestOutput
    :param quote: The quoted price for this item., defaults to None
    :type quote: QuoteInfo, optional
    """

    item_id: str
    item: OrderItemRequestOutput
    quote: Optional[QuoteInfo] = Field(
        default=None, description="The quoted price for this item."
    )
