from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CancelCalendarEventParamsSmbToolType = typing.Union[
    typing.Literal["cancel_calendar_event"], typing.Any
]


class CancelCalendarEventParams(BaseModel):
    """CancelCalendarEventParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: CancelCalendarEventParamsSmbToolType, optional
    """

    smb_tool_type: Optional[CancelCalendarEventParamsSmbToolType] = Field(default=None)
