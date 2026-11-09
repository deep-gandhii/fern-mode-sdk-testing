from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateHolidayParamsSmbToolType = typing.Union[
    typing.Literal["update_holiday"], typing.Any
]


class UpdateHolidayParams(BaseModel):
    """UpdateHolidayParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateHolidayParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateHolidayParamsSmbToolType] = Field(default=None)
