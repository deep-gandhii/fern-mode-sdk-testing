from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CustomSipHeaderType = typing.Union[typing.Literal["static"], typing.Any]


class CustomSipHeader(BaseModel):
    """Custom SIP header for phone transfers with a static (validated) value.

    :param type: type, defaults to None
    :type type: CustomSipHeaderType, optional
    :param key: The SIP header name (e.g., 'X-Customer-ID')
    :type key: str
    :param value: The header value
    :type value: str
    """

    type: Optional[CustomSipHeaderType] = Field(default=None)
    key: str = Field(description="The SIP header name (e.g., 'X-Customer-ID')")
    value: str = Field(description="The header value")
