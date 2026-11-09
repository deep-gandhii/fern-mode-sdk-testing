from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .upsert_order_item_request import UpsertOrderItemRequest


class BodyUpsertOrderItemV1ProductionsOrdersOrderIdItemsPost(BaseModel):
    """BodyUpsertOrderItemV1ProductionsOrdersOrderIdItemsPost

    :param request: request
    :type request: UpsertOrderItemRequest
    """

    request: UpsertOrderItemRequest
