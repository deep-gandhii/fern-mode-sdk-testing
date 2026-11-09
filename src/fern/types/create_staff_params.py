from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CreateStaffParamsSmbToolType = typing.Union[typing.Literal["create_staff"], typing.Any]


class CreateStaffParams(BaseModel):
    """Create a new staff member in the system.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: CreateStaffParamsSmbToolType, optional
    """

    smb_tool_type: Optional[CreateStaffParamsSmbToolType] = Field(default=None)
