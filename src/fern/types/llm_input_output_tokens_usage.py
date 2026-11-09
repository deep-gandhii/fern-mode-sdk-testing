from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .llm_tokens_category_usage import LlmTokensCategoryUsage


class LlmInputOutputTokensUsage(BaseModel):
    """LlmInputOutputTokensUsage

    :param input: input, defaults to None
    :type input: LlmTokensCategoryUsage, optional
    :param input_cache_read: input_cache_read, defaults to None
    :type input_cache_read: LlmTokensCategoryUsage, optional
    :param input_cache_write: input_cache_write, defaults to None
    :type input_cache_write: LlmTokensCategoryUsage, optional
    :param output_total: output_total, defaults to None
    :type output_total: LlmTokensCategoryUsage, optional
    """

    input: Optional[LlmTokensCategoryUsage] = Field(default=None)
    input_cache_read: Optional[LlmTokensCategoryUsage] = Field(default=None)
    input_cache_write: Optional[LlmTokensCategoryUsage] = Field(default=None)
    output_total: Optional[LlmTokensCategoryUsage] = Field(default=None)
