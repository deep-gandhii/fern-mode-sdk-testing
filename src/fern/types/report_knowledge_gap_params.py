from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ReportKnowledgeGapParamsSmbToolType = typing.Union[
    typing.Literal["report_knowledge_gap"], typing.Any
]


class ReportKnowledgeGapParams(BaseModel):
    """ReportKnowledgeGapParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: ReportKnowledgeGapParamsSmbToolType, optional
    """

    smb_tool_type: Optional[ReportKnowledgeGapParamsSmbToolType] = Field(default=None)
