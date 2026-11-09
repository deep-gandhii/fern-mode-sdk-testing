from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

GetBookingPageSettingsParamsSmbToolType = typing.Union[
    typing.Literal["get_booking_page_settings"], typing.Any
]


class GetBookingPageSettingsParams(BaseModel):
    """GetBookingPageSettingsParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: GetBookingPageSettingsParamsSmbToolType, optional
    """

    smb_tool_type: Optional[GetBookingPageSettingsParamsSmbToolType] = Field(
        default=None
    )
