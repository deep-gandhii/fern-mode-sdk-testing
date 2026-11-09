from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .crawl_type import CrawlType
from .knowledge_base_folder_path_segment_summary_response_model import (
    KnowledgeBaseFolderPathSegmentSummaryResponseModel,
)


class CreateCrawlJobResponseModel(BaseModel):
    """CreateCrawlJobResponseModel

    :param id: id
    :type id: str
    :param type: type
    :type type: CrawlType
    :param root_folder_id: root_folder_id
    :type root_folder_id: str
    :param status: status
    :type status: str
    :param created_at: created_at
    :type created_at: int
    :param folder_path: The folder path segments leading to the root folder, from root to parent folder., defaults to None
    :type folder_path: List[KnowledgeBaseFolderPathSegmentSummaryResponseModel], optional
    """

    id: str
    type: CrawlType
    root_folder_id: str
    status: str
    created_at: int
    folder_path: Optional[List[KnowledgeBaseFolderPathSegmentSummaryResponseModel]] = (
        Field(
            default=None,
            description="The folder path segments leading to the root folder, from root to parent folder.",
        )
    )
