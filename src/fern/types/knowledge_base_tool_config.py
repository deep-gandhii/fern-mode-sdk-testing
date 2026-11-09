from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .search_strategy import SearchStrategy

KnowledgeBaseToolConfigSystemToolType = typing.Union[
    typing.Literal["knowledge_base"], typing.Any
]


class KnowledgeBaseToolConfig(BaseModel):
    """KnowledgeBaseToolConfig

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: KnowledgeBaseToolConfigSystemToolType, optional
    :param enabled_strategies: enabled_strategies, defaults to None
    :type enabled_strategies: List[SearchStrategy], optional
    """

    system_tool_type: Optional[KnowledgeBaseToolConfigSystemToolType] = Field(
        default=None
    )
    enabled_strategies: Optional[List[SearchStrategy]] = Field(default=None)
