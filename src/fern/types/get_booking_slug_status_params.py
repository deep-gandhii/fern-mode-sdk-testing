from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

GetBookingSlugStatusParamsSmbToolType = typing.Union[
    typing.Literal["get_booking_slug_status"], typing.Any
]


class GetBookingSlugStatusParams(BaseModel):
    """GetBookingSlugStatusParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: GetBookingSlugStatusParamsSmbToolType, optional
    """

    smb_tool_type: Optional[GetBookingSlugStatusParamsSmbToolType] = Field(default=None)
