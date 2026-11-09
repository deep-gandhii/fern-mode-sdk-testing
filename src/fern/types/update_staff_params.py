from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateStaffParamsSmbToolType = typing.Union[typing.Literal["update_staff"], typing.Any]


class UpdateStaffParams(BaseModel):
    """Update an existing staff member's information.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateStaffParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateStaffParamsSmbToolType] = Field(default=None)
