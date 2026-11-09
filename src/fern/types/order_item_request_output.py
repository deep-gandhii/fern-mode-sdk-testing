from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .dub_order_item_request import DubOrderItemRequest
from .subtitle_order_item_request import SubtitleOrderItemRequest
from .transcription_order_item_request import TranscriptionOrderItemRequest


# fernMode variant type for a shared-component member of OrderItemRequestOutput
class OrderItemRequestOutput_Dub(DubOrderItemRequest):
    pass


# fernMode variant type for a shared-component member of OrderItemRequestOutput
class OrderItemRequestOutput_Subtitles(SubtitleOrderItemRequest):
    pass


# fernMode variant type for a shared-component member of OrderItemRequestOutput
class OrderItemRequestOutput_Transcription(TranscriptionOrderItemRequest):
    pass


# Union type for OrderItemRequestOutput
# Pydantic will attempt to validate against each type in order
OrderItemRequestOutput = Union[
    DubOrderItemRequest, SubtitleOrderItemRequest, TranscriptionOrderItemRequest
]
# TypeAdapter for runtime validation of OrderItemRequestOutput
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

OrderItemRequestOutput_adapter = TypeAdapter(OrderItemRequestOutput)
