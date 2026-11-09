from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .analysis_scope import AnalysisScope

AttachedSystemEvaluationRefSource = typing.Union[typing.Literal["system"], typing.Any]

AttachedSystemEvaluationRefAnalysisItemId = typing.Union[
    typing.Literal[
        "__system_eval_criteria_sentiment", "__system_eval_criteria_frustration"
    ],
    typing.Any,
]


class AttachedSystemEvaluationRef(BaseModel):
    """AttachedSystemEvaluationRef

    :param source: source
    :type source: AttachedSystemEvaluationRefSource
    :param analysis_item_id: Id of the referenced built-in system evaluation.
    :type analysis_item_id: AttachedSystemEvaluationRefAnalysisItemId
    :param scope: scope, defaults to None
    :type scope: AnalysisScope, optional
    :param weight: Optional relative weight for aggregate scoring., defaults to None
    :type weight: float, optional
    """

    source: AttachedSystemEvaluationRefSource = Field(default="system")
    analysis_item_id: AttachedSystemEvaluationRefAnalysisItemId = Field(
        description="Id of the referenced built-in system evaluation."
    )
    scope: Optional[AnalysisScope] = Field(default=None)
    weight: Optional[float] = Field(
        default=None, description="Optional relative weight for aggregate scoring."
    )
