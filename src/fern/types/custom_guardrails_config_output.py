from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .custom_guardrail_config import CustomGuardrailConfig


class CustomGuardrailsConfigOutput(BaseModel):
    """Config container for custom guardrails list

    :param configs: configs, defaults to None
    :type configs: List[CustomGuardrailConfig], optional
    """

    configs: Optional[List[CustomGuardrailConfig]] = Field(default=None)
