from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .workspace_audit_log_entry_response import WorkspaceAuditLogEntryResponse


class WorkspaceAuditLogsPageResponse(BaseModel):
    """Paginated workspace audit log response.

    :param entries: entries
    :type entries: List[WorkspaceAuditLogEntryResponse]
    :param has_more: has_more
    :type has_more: bool
    :param next_cursor: next_cursor
    :type next_cursor: str
    """

    entries: List[WorkspaceAuditLogEntryResponse]
    has_more: bool
    next_cursor: Optional[str]
