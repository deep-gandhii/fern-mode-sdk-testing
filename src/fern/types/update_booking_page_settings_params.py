from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateBookingPageSettingsParamsSmbToolType = typing.Union[
    typing.Literal["update_booking_page_settings"], typing.Any
]


class UpdateBookingPageSettingsParams(BaseModel):
    """UpdateBookingPageSettingsParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateBookingPageSettingsParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateBookingPageSettingsParamsSmbToolType] = Field(
        default=None
    )
