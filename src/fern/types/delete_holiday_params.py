from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DeleteHolidayParamsSmbToolType = typing.Union[
    typing.Literal["delete_holiday"], typing.Any
]


class DeleteHolidayParams(BaseModel):
    """DeleteHolidayParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: DeleteHolidayParamsSmbToolType, optional
    """

    smb_tool_type: Optional[DeleteHolidayParamsSmbToolType] = Field(default=None)
