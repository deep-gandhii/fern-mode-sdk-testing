from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ListGroupSessionsParamsSmbToolType = typing.Union[
    typing.Literal["list_group_sessions"], typing.Any
]


class ListGroupSessionsParams(BaseModel):
    """List scheduled group sessions for a group service in a date range. Group services are scheduled in advance (e.g. yoga classes, workshops) and callers register against an existing session. Use this for group services; use ``check_service_availability`` for appointment / rental services.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: ListGroupSessionsParamsSmbToolType, optional
    """

    smb_tool_type: Optional[ListGroupSessionsParamsSmbToolType] = Field(default=None)
