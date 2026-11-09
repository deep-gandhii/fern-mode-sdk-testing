from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .dub_order_item_request import DubOrderItemRequest
from .subtitle_order_item_request import SubtitleOrderItemRequest
from .transcription_order_item_request import TranscriptionOrderItemRequest


# fernMode variant type for a shared-component member of OrderItemRequestInput
class OrderItemRequestInput_Dub(DubOrderItemRequest):
    pass


# fernMode variant type for a shared-component member of OrderItemRequestInput
class OrderItemRequestInput_Subtitles(SubtitleOrderItemRequest):
    pass


# fernMode variant type for a shared-component member of OrderItemRequestInput
class OrderItemRequestInput_Transcription(TranscriptionOrderItemRequest):
    pass


# Union type for OrderItemRequestInput
# Pydantic will attempt to validate against each type in order
OrderItemRequestInput = Union[
    DubOrderItemRequest, SubtitleOrderItemRequest, TranscriptionOrderItemRequest
]
# TypeAdapter for runtime validation of OrderItemRequestInput
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

OrderItemRequestInput_adapter = TypeAdapter(OrderItemRequestInput)
