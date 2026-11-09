from __future__ import annotations
import typing
from typing import Any

SecretDependencyResourceType = typing.Union[
    typing.Literal["tools", "agents", "phone_numbers"], typing.Any
]
