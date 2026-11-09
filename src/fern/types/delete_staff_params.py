from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DeleteStaffParamsSmbToolType = typing.Union[typing.Literal["delete_staff"], typing.Any]


class DeleteStaffParams(BaseModel):
    """Delete an existing staff member from the system.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: DeleteStaffParamsSmbToolType, optional
    """

    smb_tool_type: Optional[DeleteStaffParamsSmbToolType] = Field(default=None)
