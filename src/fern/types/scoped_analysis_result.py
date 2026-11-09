from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .analysis_scope import AnalysisScope
from .conversation_history_evaluation_criteria_result_common_model import (
    ConversationHistoryEvaluationCriteriaResultCommonModel,
)
from .data_collection_result_common_model import DataCollectionResultCommonModel
from .evaluation_success_result import EvaluationSuccessResult


class ScopedAnalysisResult(BaseModel):
    """ScopedAnalysisResult

    :param scope: scope
    :type scope: AnalysisScope
    :param source_agent_id: source_agent_id
    :type source_agent_id: str
    :param source_branch_id: Branch of the agent for this scoped block; disambiguates repeated agent_id., defaults to None
    :type source_branch_id: str, optional
    :param evaluation_criteria_results: evaluation_criteria_results, defaults to None
    :type evaluation_criteria_results: Dict[str, ConversationHistoryEvaluationCriteriaResultCommonModel], optional
    :param data_collection_results: data_collection_results, defaults to None
    :type data_collection_results: Dict[str, DataCollectionResultCommonModel], optional
    :param successful: successful
    :type successful: EvaluationSuccessResult
    :param success_score: success_score, defaults to None
    :type success_score: float, optional
    """

    scope: AnalysisScope
    source_agent_id: str
    source_branch_id: Optional[str] = Field(
        default=None,
        description="Branch of the agent for this scoped block; disambiguates repeated agent_id.",
    )
    evaluation_criteria_results: Optional[
        Dict[str, ConversationHistoryEvaluationCriteriaResultCommonModel]
    ] = Field(default=None)
    data_collection_results: Optional[Dict[str, DataCollectionResultCommonModel]] = (
        Field(default=None)
    )
    successful: EvaluationSuccessResult
    success_score: Optional[float] = Field(default=None)
