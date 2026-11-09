from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .conversation_history_evaluation_criteria_result_common_model import (
    ConversationHistoryEvaluationCriteriaResultCommonModel,
)
from .data_collection_result_common_model import DataCollectionResultCommonModel
from .evaluation_success_result import EvaluationSuccessResult
from .scoped_analysis_result import ScopedAnalysisResult


class ConversationHistoryAnalysisCommonModel(BaseModel):
    """ConversationHistoryAnalysisCommonModel

    :param evaluation_criteria_results: evaluation_criteria_results, defaults to None
    :type evaluation_criteria_results: Dict[str, ConversationHistoryEvaluationCriteriaResultCommonModel], optional
    :param data_collection_results: data_collection_results, defaults to None
    :type data_collection_results: Dict[str, DataCollectionResultCommonModel], optional
    :param evaluation_criteria_results_list: evaluation_criteria_results_list, defaults to None
    :type evaluation_criteria_results_list: List[ConversationHistoryEvaluationCriteriaResultCommonModel], optional
    :param data_collection_results_list: data_collection_results_list, defaults to None
    :type data_collection_results_list: List[DataCollectionResultCommonModel], optional
    :param call_successful: call_successful
    :type call_successful: EvaluationSuccessResult
    :param call_success_score: call_success_score, defaults to None
    :type call_success_score: float, optional
    :param transcript_summary: transcript_summary
    :type transcript_summary: str
    :param call_summary_title: call_summary_title, defaults to None
    :type call_summary_title: str, optional
    :param scoped: scoped, defaults to None
    :type scoped: List[ScopedAnalysisResult], optional
    """

    evaluation_criteria_results: Optional[
        Dict[str, ConversationHistoryEvaluationCriteriaResultCommonModel]
    ] = Field(default=None)
    data_collection_results: Optional[Dict[str, DataCollectionResultCommonModel]] = (
        Field(default=None)
    )
    evaluation_criteria_results_list: Optional[
        List[ConversationHistoryEvaluationCriteriaResultCommonModel]
    ] = Field(default=None)
    data_collection_results_list: Optional[List[DataCollectionResultCommonModel]] = (
        Field(default=None)
    )
    call_successful: EvaluationSuccessResult
    call_success_score: Optional[float] = Field(default=None)
    transcript_summary: str
    call_summary_title: Optional[str] = Field(default=None)
    scoped: Optional[List[ScopedAnalysisResult]] = Field(default=None)
