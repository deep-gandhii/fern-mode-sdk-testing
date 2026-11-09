from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

LeaveMessageParamsSmbToolType = typing.Union[
    typing.Literal["leave_message"], typing.Any
]


class LeaveMessageParams(BaseModel):
    """LeaveMessageParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: LeaveMessageParamsSmbToolType, optional
    """

    smb_tool_type: Optional[LeaveMessageParamsSmbToolType] = Field(default=None)
