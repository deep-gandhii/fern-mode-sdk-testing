from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .update_order_request import UpdateOrderRequest


class BodyUpdateOrderV1ProductionsOrdersOrderIdPatch(BaseModel):
    """BodyUpdateOrderV1ProductionsOrdersOrderIdPatch

    :param request: request
    :type request: UpdateOrderRequest
    """

    request: UpdateOrderRequest
