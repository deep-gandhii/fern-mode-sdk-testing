from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .llm_usage_calculator_llm_response_model import LlmUsageCalculatorLlmResponseModel


class LlmUsageCalculatorResponseModel(BaseModel):
    """LlmUsageCalculatorResponseModel

    :param llm_prices: llm_prices
    :type llm_prices: List[LlmUsageCalculatorLlmResponseModel]
    """

    llm_prices: List[LlmUsageCalculatorLlmResponseModel]
