from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TransferBranchInfoDefaultingToMainBranchReason = typing.Union[
    typing.Literal["defaulting_to_main"], typing.Any
]


class TransferBranchInfoDefaultingToMain(BaseModel):
    """TransferBranchInfoDefaultingToMain

    :param branch_reason: branch_reason
    :type branch_reason: TransferBranchInfoDefaultingToMainBranchReason
    :param branch_id: branch_id
    :type branch_id: str
    """

    branch_reason: TransferBranchInfoDefaultingToMainBranchReason = Field(
        default="defaulting_to_main"
    )
    branch_id: str
