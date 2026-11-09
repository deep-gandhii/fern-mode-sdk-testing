from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .safety_evaluation import SafetyEvaluation


class SafetyCommonModelOutput(BaseModel):
    """Safety object that has the information of safety evaluations based on used voice.

    :param ivc: Safety evaluation of the agent. Prompt and first message is taken into account. The unsafe reason is provided from the evaluation, defaults to None
    :type ivc: SafetyEvaluation, optional
    :param non_ivc: Safety evaluation of the agent. Prompt and first message is taken into account. The unsafe reason is provided from the evaluation, defaults to None
    :type non_ivc: SafetyEvaluation, optional
    """

    ivc: Optional[SafetyEvaluation] = Field(
        default=None,
        description="Safety evaluation of the agent. Prompt and first message is taken into account. The unsafe reason is provided from the evaluation",
    )
    non_ivc: Optional[SafetyEvaluation] = Field(
        default=None,
        description="Safety evaluation of the agent. Prompt and first message is taken into account. The unsafe reason is provided from the evaluation",
    )
