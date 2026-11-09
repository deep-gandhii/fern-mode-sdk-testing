from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .search_highlight_segment import SearchHighlightSegment
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


# fernMode variant type for a shared-component member of KnowledgeBaseContentSearchResultDocument
class KnowledgeBaseContentSearchResultDocument_Url(
    GetKnowledgeBaseSummaryUrlResponseModel
):
    pass


# fernMode variant type for a shared-component member of KnowledgeBaseContentSearchResultDocument
class KnowledgeBaseContentSearchResultDocument_File(
    GetKnowledgeBaseSummaryFileResponseModel
):
    pass


# fernMode variant type for a shared-component member of KnowledgeBaseContentSearchResultDocument
class KnowledgeBaseContentSearchResultDocument_Text(
    GetKnowledgeBaseSummaryTextResponseModel
):
    pass


# fernMode variant type for a shared-component member of KnowledgeBaseContentSearchResultDocument
class KnowledgeBaseContentSearchResultDocument_Folder(
    GetKnowledgeBaseSummaryFolderResponseModel
):
    pass


# Union type for KnowledgeBaseContentSearchResultDocument
# Pydantic will attempt to validate against each type in order
KnowledgeBaseContentSearchResultDocument = Union[
    GetKnowledgeBaseSummaryUrlResponseModel,
    GetKnowledgeBaseSummaryFileResponseModel,
    GetKnowledgeBaseSummaryTextResponseModel,
    GetKnowledgeBaseSummaryFolderResponseModel,
]
# TypeAdapter for runtime validation of KnowledgeBaseContentSearchResultDocument
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

KnowledgeBaseContentSearchResultDocument_adapter = TypeAdapter(
    KnowledgeBaseContentSearchResultDocument
)


class KnowledgeBaseContentSearchResult(BaseModel):
    """KnowledgeBaseContentSearchResult

    :param document: document
    :type document: KnowledgeBaseContentSearchResultDocument
    :param search_snippet: search_snippet, defaults to None
    :type search_snippet: List[SearchHighlightSegment], optional
    :param score: score
    :type score: float
    """

    document: KnowledgeBaseContentSearchResultDocument
    search_snippet: Optional[List[SearchHighlightSegment]] = Field(default=None)
    score: float
