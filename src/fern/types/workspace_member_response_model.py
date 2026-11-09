from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .seat_type import SeatType


class WorkspaceMemberResponseModel(BaseModel):
    """Public workspace member fields exposed via GET /v1/workspace/members.

    :param user_id: The user ID of the workspace member.
    :type user_id: str
    :param email: The email address of the workspace member.
    :type email: str
    :param first_name: The first name of the workspace member, if available.
    :type first_name: str
    :param seat_type: The seat type (role) of the workspace member.
    :type seat_type: SeatType
    :param is_owner: Whether the member is the workspace owner.
    :type is_owner: bool
    :param is_locked: Whether the member's account is locked in this workspace.
    :type is_locked: bool
    """

    user_id: str = Field(description="The user ID of the workspace member.")
    email: str = Field(description="The email address of the workspace member.")
    first_name: Optional[str] = Field(
        description="The first name of the workspace member, if available."
    )
    seat_type: SeatType = Field(
        description="The seat type (role) of the workspace member."
    )
    is_owner: bool = Field(description="Whether the member is the workspace owner.")
    is_locked: bool = Field(
        description="Whether the member's account is locked in this workspace."
    )
