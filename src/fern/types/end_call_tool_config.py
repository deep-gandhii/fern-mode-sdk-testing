from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

EndCallToolConfigSystemToolType = typing.Union[typing.Literal["end_call"], typing.Any]


class EndCallToolConfig(BaseModel):
    """EndCallToolConfig

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: EndCallToolConfigSystemToolType, optional
    """

    system_tool_type: Optional[EndCallToolConfigSystemToolType] = Field(default=None)
