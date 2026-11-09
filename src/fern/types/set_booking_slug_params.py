from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

SetBookingSlugParamsSmbToolType = typing.Union[
    typing.Literal["set_booking_slug"], typing.Any
]


class SetBookingSlugParams(BaseModel):
    """SetBookingSlugParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: SetBookingSlugParamsSmbToolType, optional
    """

    smb_tool_type: Optional[SetBookingSlugParamsSmbToolType] = Field(default=None)
