from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateCalendarEventParamsSmbToolType = typing.Union[
    typing.Literal["update_calendar_event"], typing.Any
]


class UpdateCalendarEventParams(BaseModel):
    """UpdateCalendarEventParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateCalendarEventParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateCalendarEventParamsSmbToolType] = Field(default=None)
