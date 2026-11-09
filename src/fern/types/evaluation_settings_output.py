from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .prompt_evaluation_criteria import PromptEvaluationCriteria


class EvaluationSettingsOutput(BaseModel):
    """Settings to evaluate an agent's performance. Agents are evaluated against a set of criteria, with success being defined as meeting some combination of those criteria.

    :param criteria: Individual criteria that the agent should be evaluated against, defaults to None
    :type criteria: List[PromptEvaluationCriteria], optional
    """

    criteria: Optional[List[PromptEvaluationCriteria]] = Field(
        default=None,
        description="Individual criteria that the agent should be evaluated against",
    )
