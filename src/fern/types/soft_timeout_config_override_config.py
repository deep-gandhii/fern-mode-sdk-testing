from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SoftTimeoutConfigOverrideConfig(BaseModel):
    """SoftTimeoutConfigOverrideConfig

    :param message: Whether to allow overriding the message field., defaults to None
    :type message: bool, optional
    """

    message: Optional[bool] = Field(
        default=None, description="Whether to allow overriding the message field."
    )
