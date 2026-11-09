from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .safety_rule import SafetyRule


class SafetyEvaluation(BaseModel):
    """Safety evaluation of the agent. Prompt and first message is taken into account. The unsafe reason is provided from the evaluation

    :param is_unsafe: is_unsafe, defaults to None
    :type is_unsafe: bool, optional
    :param llm_reason: llm_reason, defaults to None
    :type llm_reason: str, optional
    :param safety_prompt_version: safety_prompt_version, defaults to None
    :type safety_prompt_version: int, optional
    :param matched_rule_id: matched_rule_id, defaults to None
    :type matched_rule_id: List[SafetyRule], optional
    """

    is_unsafe: Optional[bool] = Field(default=None)
    llm_reason: Optional[str] = Field(default=None)
    safety_prompt_version: Optional[int] = Field(default=None)
    matched_rule_id: Optional[List[SafetyRule]] = Field(default=None)
