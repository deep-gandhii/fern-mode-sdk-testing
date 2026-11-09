from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class TestConditionRationaleCommonModel(BaseModel):
    """Structured rationale for test condition results containing individual failure/success reasons.

    :param messages: List of individual parameter evaluation messages or reasons, defaults to None
    :type messages: List[str], optional
    :param summary: High-level summary of the evaluation result, defaults to None
    :type summary: str, optional
    """

    messages: Optional[List[str]] = Field(
        default=None,
        description="List of individual parameter evaluation messages or reasons",
    )
    summary: Optional[str] = Field(
        default=None, description="High-level summary of the evaluation result"
    )
