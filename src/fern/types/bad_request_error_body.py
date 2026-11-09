from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BadRequestErrorBody(BaseModel):
    """BadRequestErrorBody

    :param error: error, defaults to None
    :type error: str, optional
    :param message: message, defaults to None
    :type message: str, optional
    """

    error: Optional[str] = Field(default=None)
    message: Optional[str] = Field(default=None)
