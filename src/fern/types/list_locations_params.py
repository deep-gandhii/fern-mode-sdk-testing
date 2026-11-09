from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ListLocationsParamsSmbToolType = typing.Union[
    typing.Literal["list_locations"], typing.Any
]


class ListLocationsParams(BaseModel):
    """ListLocationsParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: ListLocationsParamsSmbToolType, optional
    """

    smb_tool_type: Optional[ListLocationsParamsSmbToolType] = Field(default=None)
