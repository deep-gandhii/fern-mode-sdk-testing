from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyMergeABranchIntoATargetBranchV1ConvaiAgentsAgentIdBranchesSourceBranchIdMergePost(
    BaseModel
):
    """BodyMergeABranchIntoATargetBranchV1ConvaiAgentsAgentIdBranchesSourceBranchIdMergePost

    :param archive_source_branch: Whether to archive the source branch after merging, defaults to None
    :type archive_source_branch: bool, optional
    :param force: Force source branch changes onto the target, overriding timestamp-based conflict resolution, defaults to None
    :type force: bool, optional
    """

    archive_source_branch: Optional[bool] = Field(
        default=None, description="Whether to archive the source branch after merging"
    )
    force: Optional[bool] = Field(
        default=None,
        description="Force source branch changes onto the target, overriding timestamp-based conflict resolution",
    )
