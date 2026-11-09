from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .seat_type import SeatType


class UpdateMemberRequest(BaseModel):
    """UpdateMemberRequest

    :param email: Email of the target user.
    :type email: str
    :param is_locked: Whether to lock or unlock the user account., defaults to None
    :type is_locked: bool, optional
    :param workspace_role: The workspace role of the user. This is deprecated, use `workspace_seat_type` instead., defaults to None
    :type workspace_role: SeatType, optional
    :param workspace_seat_type: The workspace seat type, defaults to None
    :type workspace_seat_type: SeatType, optional
    """

    email: str = Field(description="Email of the target user.")
    is_locked: Optional[bool] = Field(
        default=None, description="Whether to lock or unlock the user account."
    )
    workspace_role: Optional[SeatType] = Field(
        default=None,
        description="The workspace role of the user. This is deprecated, use `workspace_seat_type` instead.",
    )
    workspace_seat_type: Optional[SeatType] = Field(
        default=None, description="The workspace seat type"
    )
