from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

GetScheduleParamsSmbToolType = typing.Union[typing.Literal["get_schedule"], typing.Any]


class GetScheduleParams(BaseModel):
    """GetScheduleParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: GetScheduleParamsSmbToolType, optional
    :param include_location_filter: include_location_filter, defaults to None
    :type include_location_filter: bool, optional
    """

    smb_tool_type: Optional[GetScheduleParamsSmbToolType] = Field(default=None)
    include_location_filter: Optional[bool] = Field(default=None)
