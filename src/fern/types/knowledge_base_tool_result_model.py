from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .knowledge_base_tool_status import KnowledgeBaseToolStatus

KnowledgeBaseToolResultModelResultType = typing.Union[
    typing.Literal["knowledge_base_success"], typing.Any
]


class KnowledgeBaseToolResultModel(BaseModel):
    """KnowledgeBaseToolResultModel

    :param result_type: result_type, defaults to None
    :type result_type: KnowledgeBaseToolResultModelResultType, optional
    :param status: status, defaults to None
    :type status: KnowledgeBaseToolStatus, optional
    :param chunk_count: chunk_count, defaults to None
    :type chunk_count: int, optional
    :param message: message, defaults to None
    :type message: str, optional
    """

    result_type: Optional[KnowledgeBaseToolResultModelResultType] = Field(default=None)
    status: Optional[KnowledgeBaseToolStatus] = Field(default=None)
    chunk_count: Optional[int] = Field(default=None)
    message: Optional[str] = Field(default=None)
