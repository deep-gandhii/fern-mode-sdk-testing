from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CreateClientAppointmentParamsSmbToolType = typing.Union[
    typing.Literal["create_client_appointment"], typing.Any
]


class CreateClientAppointmentParams(BaseModel):
    """CreateClientAppointmentParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: CreateClientAppointmentParamsSmbToolType, optional
    """

    smb_tool_type: Optional[CreateClientAppointmentParamsSmbToolType] = Field(
        default=None
    )
