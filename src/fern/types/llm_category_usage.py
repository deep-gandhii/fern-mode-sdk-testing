from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .llm_usage_output import LlmUsageOutput


class LlmCategoryUsage(BaseModel):
    """LlmCategoryUsage

    :param irreversible_generation: irreversible_generation, defaults to None
    :type irreversible_generation: LlmUsageOutput, optional
    :param initiated_generation: initiated_generation, defaults to None
    :type initiated_generation: LlmUsageOutput, optional
    """

    irreversible_generation: Optional[LlmUsageOutput] = Field(default=None)
    initiated_generation: Optional[LlmUsageOutput] = Field(default=None)
