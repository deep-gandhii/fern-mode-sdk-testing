from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .guardrail_execution_mode import GuardrailExecutionMode
from .moderation_config import ModerationConfig


class ModerationGuardrailInput(BaseModel):
    """ModerationGuardrailInput

    :param execution_mode: execution_mode, defaults to None
    :type execution_mode: GuardrailExecutionMode, optional
    :param config: config, defaults to None
    :type config: ModerationConfig, optional
    """

    execution_mode: Optional[GuardrailExecutionMode] = Field(default=None)
    config: Optional[ModerationConfig] = Field(default=None)
