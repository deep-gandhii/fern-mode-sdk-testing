from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .get_knowledge_base_summary_url_response_model import (
    GetKnowledgeBaseSummaryUrlResponseModel,
)
from .get_knowledge_base_summary_file_response_model import (
    GetKnowledgeBaseSummaryFileResponseModel,
)
from .get_knowledge_base_summary_text_response_model import (
    GetKnowledgeBaseSummaryTextResponseModel,
)
from .get_knowledge_base_summary_folder_response_model import (
    GetKnowledgeBaseSummaryFolderResponseModel,
)


# fernMode variant type for a shared-component member of GetKnowledgeBaseListResponseModelDocumentsItem
class GetKnowledgeBaseListResponseModelDocumentsItem_Url(
    GetKnowledgeBaseSummaryUrlResponseModel
):
    pass


# fernMode variant type for a shared-component member of GetKnowledgeBaseListResponseModelDocumentsItem
class GetKnowledgeBaseListResponseModelDocumentsItem_File(
    GetKnowledgeBaseSummaryFileResponseModel
):
    pass


# fernMode variant type for a shared-component member of GetKnowledgeBaseListResponseModelDocumentsItem
class GetKnowledgeBaseListResponseModelDocumentsItem_Text(
    GetKnowledgeBaseSummaryTextResponseModel
):
    pass


# fernMode variant type for a shared-component member of GetKnowledgeBaseListResponseModelDocumentsItem
class GetKnowledgeBaseListResponseModelDocumentsItem_Folder(
    GetKnowledgeBaseSummaryFolderResponseModel
):
    pass


# Union type for GetKnowledgeBaseListResponseModelDocumentsItem
# Pydantic will attempt to validate against each type in order
GetKnowledgeBaseListResponseModelDocumentsItem = Union[
    GetKnowledgeBaseSummaryUrlResponseModel,
    GetKnowledgeBaseSummaryFileResponseModel,
    GetKnowledgeBaseSummaryTextResponseModel,
    GetKnowledgeBaseSummaryFolderResponseModel,
]
# TypeAdapter for runtime validation of GetKnowledgeBaseListResponseModelDocumentsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

GetKnowledgeBaseListResponseModelDocumentsItem_adapter = TypeAdapter(
    GetKnowledgeBaseListResponseModelDocumentsItem
)


class GetKnowledgeBaseListResponseModel(BaseModel):
    """GetKnowledgeBaseListResponseModel

    :param documents: documents
    :type documents: List[GetKnowledgeBaseListResponseModelDocumentsItem]
    :param next_cursor: next_cursor, defaults to None
    :type next_cursor: str, optional
    :param has_more: has_more
    :type has_more: bool
    """

    documents: List[GetKnowledgeBaseListResponseModelDocumentsItem]
    next_cursor: Optional[str] = Field(default=None)
    has_more: bool
