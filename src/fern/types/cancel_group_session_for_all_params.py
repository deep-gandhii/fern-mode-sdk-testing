from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CancelGroupSessionForAllParamsSmbToolType = typing.Union[
    typing.Literal["cancel_group_session_for_all"], typing.Any
]


class CancelGroupSessionForAllParams(BaseModel):
    """Cancel an entire group session and notify every registered participant. Destructive -- prefer ``cancel_group_session_registration`` for cancelling a single attendee.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: CancelGroupSessionForAllParamsSmbToolType, optional
    """

    smb_tool_type: Optional[CancelGroupSessionForAllParamsSmbToolType] = Field(
        default=None
    )
