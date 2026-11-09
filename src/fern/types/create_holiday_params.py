from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CreateHolidayParamsSmbToolType = typing.Union[
    typing.Literal["create_holiday"], typing.Any
]


class CreateHolidayParams(BaseModel):
    """CreateHolidayParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: CreateHolidayParamsSmbToolType, optional
    """

    smb_tool_type: Optional[CreateHolidayParamsSmbToolType] = Field(default=None)
