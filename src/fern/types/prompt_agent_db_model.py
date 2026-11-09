from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class PromptAgentDbModel(BaseModel):
    """PromptAgentDbModel

    :param tools: tools, defaults to None
    :type tools: Any, optional
    """

    tools: Optional[Any] = Field(default=None)
