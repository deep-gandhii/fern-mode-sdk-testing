from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

RegisterForGroupSessionParamsSmbToolType = typing.Union[
    typing.Literal["register_for_group_session"], typing.Any
]


class RegisterForGroupSessionParams(BaseModel):
    """Register a client for a scheduled group session.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: RegisterForGroupSessionParamsSmbToolType, optional
    """

    smb_tool_type: Optional[RegisterForGroupSessionParamsSmbToolType] = Field(
        default=None
    )
