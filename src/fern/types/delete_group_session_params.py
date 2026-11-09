from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DeleteGroupSessionParamsSmbToolType = typing.Union[
    typing.Literal["delete_group_session"], typing.Any
]


class DeleteGroupSessionParams(BaseModel):
    """Permanently remove a previously-cancelled group session. Group analogue of ``delete_calendar_event``: cancel (``cancel_group_session_for_all``) is the soft, history-preserving step; this tool is the irreversible follow-up that drops the row from Mongo and the staff Google Calendar entirely. The backend rejects the call (422) if the session hasn't been cancelled yet, so the only safe path is cancel-then-delete.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: DeleteGroupSessionParamsSmbToolType, optional
    """

    smb_tool_type: Optional[DeleteGroupSessionParamsSmbToolType] = Field(default=None)
