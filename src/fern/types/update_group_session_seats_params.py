from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateGroupSessionSeatsParamsSmbToolType = typing.Union[
    typing.Literal["update_group_session_seats"], typing.Any
]


class UpdateGroupSessionSeatsParams(BaseModel):
    """Change the seat count of an existing group session registration.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateGroupSessionSeatsParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateGroupSessionSeatsParamsSmbToolType] = Field(
        default=None
    )
