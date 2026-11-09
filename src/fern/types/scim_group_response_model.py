from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .seat_type import SeatType


class ScimGroupResponseModel(BaseModel):
    """ScimGroupResponseModel

    :param scim_external_id: scim_external_id
    :type scim_external_id: str
    :param display_name: display_name
    :type display_name: str
    :param created_at_unix: created_at_unix, defaults to None
    :type created_at_unix: int, optional
    :param updated_at_unix: updated_at_unix, defaults to None
    :type updated_at_unix: int, optional
    :param seat_type: seat_type, defaults to None
    :type seat_type: SeatType, optional
    """

    scim_external_id: Optional[str]
    display_name: str
    created_at_unix: Optional[int] = Field(default=None)
    updated_at_unix: Optional[int] = Field(default=None)
    seat_type: Optional[SeatType] = Field(default=None)
