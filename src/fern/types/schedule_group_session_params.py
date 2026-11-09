from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ScheduleGroupSessionParamsSmbToolType = typing.Union[
    typing.Literal["schedule_group_session"], typing.Any
]


class ScheduleGroupSessionParams(BaseModel):
    """Schedule a single instance of a group service. The session's duration is derived from the parent service so the assistant only has to pin start time, the (optional) instructor / room, and the location. Participants register separately via ``register_for_group_session``.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: ScheduleGroupSessionParamsSmbToolType, optional
    """

    smb_tool_type: Optional[ScheduleGroupSessionParamsSmbToolType] = Field(default=None)
