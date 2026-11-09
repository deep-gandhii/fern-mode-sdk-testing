from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .custom_guardrails_config_output import CustomGuardrailsConfigOutput


class CustomGuardrailOutput(BaseModel):
    """Container for custom guardrails, matching ModerationGuardrail pattern

    :param config: Config container for custom guardrails list, defaults to None
    :type config: CustomGuardrailsConfigOutput, optional
    """

    config: Optional[CustomGuardrailsConfigOutput] = Field(
        default=None, description="Config container for custom guardrails list"
    )
