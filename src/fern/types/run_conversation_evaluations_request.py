from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .analysis_scope import AnalysisScope


class RunConversationEvaluationsRequest(BaseModel):
    """RunConversationEvaluationsRequest

    :param evaluation_id: ID of the single evaluation criterion to rerun.
    :type evaluation_id: str
    :param scope: scope, defaults to None
    :type scope: AnalysisScope, optional
    """

    evaluation_id: str = Field(
        description="ID of the single evaluation criterion to rerun."
    )
    scope: Optional[AnalysisScope] = Field(default=None)
