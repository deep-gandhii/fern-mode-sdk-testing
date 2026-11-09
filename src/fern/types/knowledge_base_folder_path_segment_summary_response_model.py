from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class KnowledgeBaseFolderPathSegmentSummaryResponseModel(BaseModel):
    """KnowledgeBaseFolderPathSegmentSummaryResponseModel

    :param id: id
    :type id: str
    """

    id: str
