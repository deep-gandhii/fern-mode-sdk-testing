from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .knowledge_base_folder_path_segment_summary_response_model import (
    KnowledgeBaseFolderPathSegmentSummaryResponseModel,
)


class AddKnowledgeBaseResponseModel(BaseModel):
    """AddKnowledgeBaseResponseModel

    :param id: id
    :type id: str
    :param name: name
    :type name: str
    :param folder_path: The folder path segments leading to this entity, from root to parent folder., defaults to None
    :type folder_path: List[KnowledgeBaseFolderPathSegmentSummaryResponseModel], optional
    """

    id: str
    name: str
    folder_path: Optional[List[KnowledgeBaseFolderPathSegmentSummaryResponseModel]] = (
        Field(
            default=None,
            description="The folder path segments leading to this entity, from root to parent folder.",
        )
    )
