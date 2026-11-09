from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from .utils.base_model import BaseModel
from .llm_input_output_tokens_usage import LlmInputOutputTokensUsage


class LlmUsageOutput(BaseModel):
    """LlmUsageOutput

    :param model_usage: model_usage, defaults to None
    :type model_usage: Dict[str, LlmInputOutputTokensUsage], optional
    """

    model_usage: Optional[Dict[str, LlmInputOutputTokensUsage]] = Field(default=None)
