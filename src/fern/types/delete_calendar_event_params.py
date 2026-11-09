from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DeleteCalendarEventParamsSmbToolType = typing.Union[
    typing.Literal["delete_calendar_event"], typing.Any
]


class DeleteCalendarEventParams(BaseModel):
    """Permanently remove a previously-cancelled calendar event. This delete tool is the irreversible follow-up to cancel_calendar_event. The backend rejects the call (422) if the event hasn't been cancelled yet, so the only safe path is cancel-then-delete.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: DeleteCalendarEventParamsSmbToolType, optional
    """

    smb_tool_type: Optional[DeleteCalendarEventParamsSmbToolType] = Field(default=None)
