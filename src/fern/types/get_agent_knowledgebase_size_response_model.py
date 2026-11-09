from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class GetAgentKnowledgebaseSizeResponseModel(BaseModel):
    """GetAgentKnowledgebaseSizeResponseModel

    :param number_of_pages: number_of_pages
    :type number_of_pages: float
    """

    number_of_pages: float
