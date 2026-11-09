from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .search_strategy import SearchStrategy


class KnowledgeBaseToolInfo(BaseModel):
    """KnowledgeBaseToolInfo

    :param enabled_strategies: Search strategies exposed to the model. Must be non-empty., defaults to None
    :type enabled_strategies: List[SearchStrategy], optional
    """

    enabled_strategies: Optional[List[SearchStrategy]] = Field(
        default=None,
        description="Search strategies exposed to the model. Must be non-empty.",
    )
