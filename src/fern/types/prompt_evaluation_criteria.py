from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .analysis_scope import AnalysisScope
from .llm import Llm
from .criteria_scoring_mode import CriteriaScoringMode

PromptEvaluationCriteriaType = typing.Union[typing.Literal["prompt"], typing.Any]


class PromptEvaluationCriteria(BaseModel):
    """An evaluation using the transcript and a prompt for a yes/no achieved answer

    :param id: The unique identifier for the evaluation criteria
    :type id: str
    :param name: name
    :type name: str
    :param type: The type of evaluation criteria, defaults to None
    :type type: PromptEvaluationCriteriaType, optional
    :param conversation_goal_prompt: The prompt that the agent should use to evaluate the conversation
    :type conversation_goal_prompt: str
    :param use_knowledge_base: When evaluating the prompt, should the agent's knowledge base be used., defaults to None
    :type use_knowledge_base: bool, optional
    :param scope: scope, defaults to None
    :type scope: AnalysisScope, optional
    :param llm: LLM model to use for this evaluation criteria. If not set, uses agent's analysis_llm default., defaults to None
    :type llm: Llm, optional
    :param scoring_mode: scoring_mode, defaults to None
    :type scoring_mode: CriteriaScoringMode, optional
    :param max_score: Maximum value of the numeric score scale (minimum is always 0). Only used when scoring_mode is 'numeric_uniform'., defaults to None
    :type max_score: int, optional
    :param score_instructions: Optional free-text instructions describing how to assign values on the numeric scale. Only used when scoring_mode is 'numeric_uniform'., defaults to None
    :type score_instructions: str, optional
    """

    id: str = Field(description="The unique identifier for the evaluation criteria")
    name: str
    type: Optional[PromptEvaluationCriteriaType] = Field(
        default=None, description="The type of evaluation criteria"
    )
    conversation_goal_prompt: str = Field(
        description="The prompt that the agent should use to evaluate the conversation"
    )
    use_knowledge_base: Optional[bool] = Field(
        default=None,
        description="When evaluating the prompt, should the agent's knowledge base be used.",
    )
    scope: Optional[AnalysisScope] = Field(default=None)
    llm: Optional[Llm] = Field(
        default=None,
        description="LLM model to use for this evaluation criteria. If not set, uses agent's analysis_llm default.",
    )
    scoring_mode: Optional[CriteriaScoringMode] = Field(default=None)
    max_score: Optional[int] = Field(
        default=None,
        description="Maximum value of the numeric score scale (minimum is always 0). Only used when scoring_mode is 'numeric_uniform'.",
    )
    score_instructions: Optional[str] = Field(
        default=None,
        description="Optional free-text instructions describing how to assign values on the numeric scale. Only used when scoring_mode is 'numeric_uniform'.",
    )
