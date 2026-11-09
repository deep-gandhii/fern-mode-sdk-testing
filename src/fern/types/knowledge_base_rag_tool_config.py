from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

KnowledgeBaseRagToolConfigSystemToolType = typing.Union[
    typing.Literal["knowledge_base_rag"], typing.Any
]


class KnowledgeBaseRagToolConfig(BaseModel):
    """KnowledgeBaseRagToolConfig

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: KnowledgeBaseRagToolConfigSystemToolType, optional
    """

    system_tool_type: Optional[KnowledgeBaseRagToolConfigSystemToolType] = Field(
        default=None
    )
