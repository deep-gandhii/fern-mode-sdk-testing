from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

OptInSmsReminderParamsSmbToolType = typing.Union[
    typing.Literal["opt_in_sms_reminder"], typing.Any
]


class OptInSmsReminderParams(BaseModel):
    """OptInSmsReminderParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: OptInSmsReminderParamsSmbToolType, optional
    """

    smb_tool_type: Optional[OptInSmsReminderParamsSmbToolType] = Field(default=None)
