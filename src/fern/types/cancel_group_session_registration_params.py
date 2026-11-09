from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CancelGroupSessionRegistrationParamsSmbToolType = typing.Union[
    typing.Literal["cancel_group_session_registration"], typing.Any
]


class CancelGroupSessionRegistrationParams(BaseModel):
    """Cancel a single client's registration for a group session.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: CancelGroupSessionRegistrationParamsSmbToolType, optional
    """

    smb_tool_type: Optional[CancelGroupSessionRegistrationParamsSmbToolType] = Field(
        default=None
    )
