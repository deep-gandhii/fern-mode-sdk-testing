from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .custom_guardrails_config_input import CustomGuardrailsConfigInput


class CustomGuardrailInput(BaseModel):
    """Container for custom guardrails, matching ModerationGuardrail pattern

    :param config: Config container for custom guardrails list, defaults to None
    :type config: CustomGuardrailsConfigInput, optional
    """

    config: Optional[CustomGuardrailsConfigInput] = Field(
        default=None, description="Config container for custom guardrails list"
    )
