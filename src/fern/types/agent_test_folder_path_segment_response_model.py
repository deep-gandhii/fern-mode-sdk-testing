from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AgentTestFolderPathSegmentResponseModel(BaseModel):
    """AgentTestFolderPathSegmentResponseModel

    :param id: id
    :type id: str
    :param name: name, defaults to None
    :type name: str, optional
    """

    id: str
    name: Optional[str] = Field(default=None)
