from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DependentBranchInfo(BaseModel):
    """DependentBranchInfo

    :param agent_id: agent_id
    :type agent_id: str
    :param agent_name: agent_name
    :type agent_name: str
    :param branch_id: branch_id
    :type branch_id: str
    :param branch_name: branch_name
    :type branch_name: str
    :param is_main: is_main
    :type is_main: bool
    """

    agent_id: str
    agent_name: str
    branch_id: str
    branch_name: str
    is_main: bool
