from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TransferBranchInfoTrafficSplitBranchReason = typing.Union[
    typing.Literal["traffic_split"], typing.Any
]


class TransferBranchInfoTrafficSplit(BaseModel):
    """TransferBranchInfoTrafficSplit

    :param branch_reason: branch_reason
    :type branch_reason: TransferBranchInfoTrafficSplitBranchReason
    :param branch_id: branch_id
    :type branch_id: str
    :param traffic_percentage: traffic_percentage
    :type traffic_percentage: float
    """

    branch_reason: TransferBranchInfoTrafficSplitBranchReason = Field(
        default="traffic_split"
    )
    branch_id: str
    traffic_percentage: float
