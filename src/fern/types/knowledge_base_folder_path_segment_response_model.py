from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class KnowledgeBaseFolderPathSegmentResponseModel(BaseModel):
    """KnowledgeBaseFolderPathSegmentResponseModel

    :param id: id
    :type id: str
    :param name: name
    :type name: str
    """

    id: str
    name: Optional[str]
