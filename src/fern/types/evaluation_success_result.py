from __future__ import annotations
import typing
from typing import Any

EvaluationSuccessResult = typing.Union[
    typing.Literal["success", "failure", "unknown"], typing.Any
]
