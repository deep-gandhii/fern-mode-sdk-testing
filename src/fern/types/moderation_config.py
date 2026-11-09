from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .threshold_guardrail import ThresholdGuardrail


class ModerationConfig(BaseModel):
    """ModerationConfig

    :param sexual: sexual, defaults to None
    :type sexual: ThresholdGuardrail, optional
    :param violence: violence, defaults to None
    :type violence: ThresholdGuardrail, optional
    :param violence_graphic: violence_graphic, defaults to None
    :type violence_graphic: ThresholdGuardrail, optional
    :param harassment: harassment, defaults to None
    :type harassment: ThresholdGuardrail, optional
    :param harassment_threatening: harassment_threatening, defaults to None
    :type harassment_threatening: ThresholdGuardrail, optional
    :param hate: hate, defaults to None
    :type hate: ThresholdGuardrail, optional
    :param hate_threatening: hate_threatening, defaults to None
    :type hate_threatening: ThresholdGuardrail, optional
    :param self_harm_instructions: self_harm_instructions, defaults to None
    :type self_harm_instructions: ThresholdGuardrail, optional
    :param self_harm: self_harm, defaults to None
    :type self_harm: ThresholdGuardrail, optional
    :param self_harm_intent: self_harm_intent, defaults to None
    :type self_harm_intent: ThresholdGuardrail, optional
    :param sexual_minors: sexual_minors, defaults to None
    :type sexual_minors: ThresholdGuardrail, optional
    """

    sexual: Optional[ThresholdGuardrail] = Field(default=None)
    violence: Optional[ThresholdGuardrail] = Field(default=None)
    violence_graphic: Optional[ThresholdGuardrail] = Field(default=None)
    harassment: Optional[ThresholdGuardrail] = Field(default=None)
    harassment_threatening: Optional[ThresholdGuardrail] = Field(default=None)
    hate: Optional[ThresholdGuardrail] = Field(default=None)
    hate_threatening: Optional[ThresholdGuardrail] = Field(default=None)
    self_harm_instructions: Optional[ThresholdGuardrail] = Field(default=None)
    self_harm: Optional[ThresholdGuardrail] = Field(default=None)
    self_harm_intent: Optional[ThresholdGuardrail] = Field(default=None)
    sexual_minors: Optional[ThresholdGuardrail] = Field(default=None)
