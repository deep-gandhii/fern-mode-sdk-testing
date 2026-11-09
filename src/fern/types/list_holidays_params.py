from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ListHolidaysParamsSmbToolType = typing.Union[
    typing.Literal["list_holidays"], typing.Any
]


class ListHolidaysParams(BaseModel):
    """ListHolidaysParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: ListHolidaysParamsSmbToolType, optional
    """

    smb_tool_type: Optional[ListHolidaysParamsSmbToolType] = Field(default=None)
