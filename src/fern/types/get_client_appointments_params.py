from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

GetClientAppointmentsParamsSmbToolType = typing.Union[
    typing.Literal["get_client_appointments"], typing.Any
]


class GetClientAppointmentsParams(BaseModel):
    """GetClientAppointmentsParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: GetClientAppointmentsParamsSmbToolType, optional
    :param include_cancelled: include_cancelled, defaults to None
    :type include_cancelled: bool, optional
    """

    smb_tool_type: Optional[GetClientAppointmentsParamsSmbToolType] = Field(
        default=None
    )
    include_cancelled: Optional[bool] = Field(default=None)
