from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CheckServiceAvailabilityParamsSmbToolType = typing.Union[
    typing.Literal["check_service_availability"], typing.Any
]


class CheckServiceAvailabilityParams(BaseModel):
    """CheckServiceAvailabilityParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: CheckServiceAvailabilityParamsSmbToolType, optional
    """

    smb_tool_type: Optional[CheckServiceAvailabilityParamsSmbToolType] = Field(
        default=None
    )
