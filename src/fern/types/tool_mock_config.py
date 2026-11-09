from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ToolMockConfig(BaseModel):
    """ToolMockConfig

    :param default_return_value: default_return_value, defaults to None
    :type default_return_value: str, optional
    :param default_is_error: default_is_error, defaults to None
    :type default_is_error: bool, optional
    """

    default_return_value: Optional[str] = Field(default=None)
    default_is_error: Optional[bool] = Field(default=None)
