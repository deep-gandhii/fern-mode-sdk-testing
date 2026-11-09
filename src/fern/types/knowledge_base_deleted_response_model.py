from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class KnowledgeBaseDeletedResponseModel(BaseModel):
    """KnowledgeBaseDeletedResponseModel

    :param id: id
    :type id: str
    """

    id: str
