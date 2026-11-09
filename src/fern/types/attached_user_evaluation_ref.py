from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .analysis_scope import AnalysisScope

AttachedUserEvaluationRefSource = typing.Union[typing.Literal["user"], typing.Any]


class AttachedUserEvaluationRef(BaseModel):
    """AttachedUserEvaluationRef

    :param source: source
    :type source: AttachedUserEvaluationRefSource
    :param analysis_item_id: Id of the referenced user evaluation item.
    :type analysis_item_id: str
    :param version_id: Primary item version whose result feeds scoring. None tracks the item's latest published version., defaults to None
    :type version_id: str, optional
    :param additional_version_ids: Extra item versions to also run for comparison (A/B). These are executed and stored but excluded from scoring; the primary version_id is the one that scores., defaults to None
    :type additional_version_ids: List[str], optional
    :param scope: scope, defaults to None
    :type scope: AnalysisScope, optional
    :param weight: Optional relative weight for aggregate scoring., defaults to None
    :type weight: float, optional
    """

    source: AttachedUserEvaluationRefSource = Field(default="user")
    analysis_item_id: str = Field(
        description="Id of the referenced user evaluation item."
    )
    version_id: Optional[str] = Field(
        default=None,
        description="Primary item version whose result feeds scoring. None tracks the item's latest published version.",
    )
    additional_version_ids: Optional[List[str]] = Field(
        default=None,
        description="Extra item versions to also run for comparison (A/B). These are executed and stored but excluded from scoring; the primary version_id is the one that scores.",
    )
    scope: Optional[AnalysisScope] = Field(default=None)
    weight: Optional[float] = Field(
        default=None, description="Optional relative weight for aggregate scoring."
    )
