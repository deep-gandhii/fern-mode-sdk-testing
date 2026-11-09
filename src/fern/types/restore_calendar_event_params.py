from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

RestoreCalendarEventParamsSmbToolType = typing.Union[
    typing.Literal["restore_calendar_event"], typing.Any
]


class RestoreCalendarEventParams(BaseModel):
    """RestoreCalendarEventParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: RestoreCalendarEventParamsSmbToolType, optional
    """

    smb_tool_type: Optional[RestoreCalendarEventParamsSmbToolType] = Field(default=None)
