from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ListCalendarEventsParamsSmbToolType = typing.Union[
    typing.Literal["list_calendar_events"], typing.Any
]


class ListCalendarEventsParams(BaseModel):
    """ListCalendarEventsParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: ListCalendarEventsParamsSmbToolType, optional
    :param include_cancelled: include_cancelled, defaults to None
    :type include_cancelled: bool, optional
    """

    smb_tool_type: Optional[ListCalendarEventsParamsSmbToolType] = Field(default=None)
    include_cancelled: Optional[bool] = Field(default=None)
