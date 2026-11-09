from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class CreateOrderRequest(BaseModel):
    """CreateOrderRequest

    :param sandbox: When true, creates a sandbox order that auto-progresses without producer intervention., defaults to None
    :type sandbox: bool, optional
    """

    sandbox: Optional[bool] = Field(
        default=None,
        description="When true, creates a sandbox order that auto-progresses without producer intervention.",
    )
