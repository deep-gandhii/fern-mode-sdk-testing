from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class VisitedAgentRef(BaseModel):
    """An agent (and optional branch) that participated in the call, in first-seen transcript order.

    :param agent_id: agent_id
    :type agent_id: str
    :param branch_id: branch_id, defaults to None
    :type branch_id: str, optional
    """

    agent_id: str
    branch_id: Optional[str] = Field(default=None)
