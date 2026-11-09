from __future__ import annotations
import typing
from typing import Any

BranchProtectionStatus = typing.Union[
    typing.Literal["writer_perms_required", "admin_perms_required"], typing.Any
]
