from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

GetAppointmentByConfirmationNumberParamsSmbToolType = typing.Union[
    typing.Literal["get_appointment_by_confirmation_number"], typing.Any
]


class GetAppointmentByConfirmationNumberParams(BaseModel):
    """Look up an appointment by the booking confirmation number the caller quotes. The confirmation number is the 8-character code shown on the booking confirmation page (e.g. ``#01ABCDEF``). Callers may read it back with or without the leading ``#`` and with varied spacing; the tool normalizes the input and does a prefix match on the stored calendar item id.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: GetAppointmentByConfirmationNumberParamsSmbToolType, optional
    """

    smb_tool_type: Optional[GetAppointmentByConfirmationNumberParamsSmbToolType] = (
        Field(default=None)
    )
