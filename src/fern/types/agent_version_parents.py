from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class AgentVersionParents(BaseModel):
    """AgentVersionParents

    :param in_branch_parent_id: in_branch_parent_id, defaults to None
    :type in_branch_parent_id: str, optional
    :param out_of_branch_parent_id: out_of_branch_parent_id, defaults to None
    :type out_of_branch_parent_id: str, optional
    :param merged_into_branch_id: merged_into_branch_id, defaults to None
    :type merged_into_branch_id: str, optional
    :param merged_from_branch_id: merged_from_branch_id, defaults to None
    :type merged_from_branch_id: str, optional
    :param merged_from_version_id: merged_from_version_id, defaults to None
    :type merged_from_version_id: str, optional
    :param rebased_from_version_id: rebased_from_version_id, defaults to None
    :type rebased_from_version_id: str, optional
    """

    in_branch_parent_id: Optional[str] = Field(default=None)
    out_of_branch_parent_id: Optional[str] = Field(default=None)
    merged_into_branch_id: Optional[str] = Field(default=None)
    merged_from_branch_id: Optional[str] = Field(default=None)
    merged_from_version_id: Optional[str] = Field(default=None)
    rebased_from_version_id: Optional[str] = Field(default=None)
