from __future__ import annotations
import typing
from typing import Any

AuthConnectionStatus = typing.Union[
    typing.Literal["active", "refresh_failed", "revoked", "credential_invalid"],
    typing.Any,
]
