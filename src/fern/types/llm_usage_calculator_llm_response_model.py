from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .llm import Llm


class LlmUsageCalculatorLlmResponseModel(BaseModel):
    """LlmUsageCalculatorLlmResponseModel

    :param llm: llm
    :type llm: Llm
    :param price_per_minute: price_per_minute
    :type price_per_minute: float
    """

    llm: Llm
    price_per_minute: float
