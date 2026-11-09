from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CustomSipHeaderWithDynamicVariableType = typing.Union[
    typing.Literal["dynamic"], typing.Any
]


class CustomSipHeaderWithDynamicVariable(BaseModel):
    """Custom SIP header for phone transfers with a dynamic variable reference. The value is a variable name that will be resolved at runtime. Value is not validated here since it will be substituted with actual value later.

    :param type: type
    :type type: CustomSipHeaderWithDynamicVariableType
    :param key: The SIP header name (e.g., 'X-Customer-ID')
    :type key: str
    :param value: The dynamic variable name to resolve
    :type value: str
    """

    type: CustomSipHeaderWithDynamicVariableType = Field(default="dynamic")
    key: str = Field(description="The SIP header name (e.g., 'X-Customer-ID')")
    value: str = Field(description="The dynamic variable name to resolve")
