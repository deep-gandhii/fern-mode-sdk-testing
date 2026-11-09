from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .order_item_request_input import (
    OrderItemRequestInput,
    OrderItemRequestInput_adapter,
)
from .dub_order_item_request import DubOrderItemRequest
from .subtitle_order_item_request import SubtitleOrderItemRequest
from .transcription_order_item_request import TranscriptionOrderItemRequest


class UpsertOrderItemRequest(BaseModel):
    """UpsertOrderItemRequest

    :param item: item
    :type item: OrderItemRequestInput
    :param item_id: The ID of an existing item to update. Omit to create a new item., defaults to None
    :type item_id: str, optional
    """

    item: OrderItemRequestInput
    item_id: Optional[str] = Field(
        default=None,
        description="The ID of an existing item to update. Omit to create a new item.",
    )
