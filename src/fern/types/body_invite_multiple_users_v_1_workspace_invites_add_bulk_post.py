from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .seat_type import SeatType


class BodyInviteMultipleUsersV1WorkspaceInvitesAddBulkPost(BaseModel):
    """BodyInviteMultipleUsersV1WorkspaceInvitesAddBulkPost

    :param emails: The email of the customer
    :type emails: List[str]
    :param seat_type: The seat type of the user, defaults to None
    :type seat_type: SeatType, optional
    :param group_ids: The group ids of the user, defaults to None
    :type group_ids: List[str], optional
    :param usage_limit: Monthly credit usage limit for the invitee. Omit or set to null for no custom cap., defaults to None
    :type usage_limit: int, optional
    """

    emails: List[str] = Field(description="The email of the customer")
    seat_type: Optional[SeatType] = Field(
        default=None, description="The seat type of the user"
    )
    group_ids: Optional[List[str]] = Field(
        default=None, description="The group ids of the user"
    )
    usage_limit: Optional[int] = Field(
        default=None,
        description="Monthly credit usage limit for the invitee. Omit or set to null for no custom cap.",
    )
