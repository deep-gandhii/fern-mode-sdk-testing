from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .tool_response_model import ToolResponseModel


class ToolsResponseModel(BaseModel):
    """ToolsResponseModel

    :param tools: tools
    :type tools: List[ToolResponseModel]
    :param next_cursor: next_cursor, defaults to None
    :type next_cursor: str, optional
    :param has_more: has_more
    :type has_more: bool
    """

    tools: List[ToolResponseModel]
    next_cursor: Optional[str] = Field(default=None)
    has_more: bool
