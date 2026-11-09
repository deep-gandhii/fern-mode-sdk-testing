from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateBookingPageAppearanceParamsSmbToolType = typing.Union[
    typing.Literal["update_booking_page_appearance"], typing.Any
]


class UpdateBookingPageAppearanceParams(BaseModel):
    """UpdateBookingPageAppearanceParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateBookingPageAppearanceParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateBookingPageAppearanceParamsSmbToolType] = Field(
        default=None
    )
