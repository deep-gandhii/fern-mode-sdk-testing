from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .get_knowledge_base_url_response_model import GetKnowledgeBaseUrlResponseModel
from .get_knowledge_base_file_response_model import GetKnowledgeBaseFileResponseModel
from .get_knowledge_base_text_response_model import GetKnowledgeBaseTextResponseModel
from .get_knowledge_base_folder_response_model import (
    GetKnowledgeBaseFolderResponseModel,
)


# fernMode variant type for a shared-component member of DocumentRefreshResponse
class DocumentRefreshResponse_Url(GetKnowledgeBaseUrlResponseModel):
    pass


# fernMode variant type for a shared-component member of DocumentRefreshResponse
class DocumentRefreshResponse_File(GetKnowledgeBaseFileResponseModel):
    pass


# fernMode variant type for a shared-component member of DocumentRefreshResponse
class DocumentRefreshResponse_Text(GetKnowledgeBaseTextResponseModel):
    pass


# fernMode variant type for a shared-component member of DocumentRefreshResponse
class DocumentRefreshResponse_Folder(GetKnowledgeBaseFolderResponseModel):
    pass


# Union type for DocumentRefreshResponse
# Pydantic will attempt to validate against each type in order
DocumentRefreshResponse = Union[
    GetKnowledgeBaseUrlResponseModel,
    GetKnowledgeBaseFileResponseModel,
    GetKnowledgeBaseTextResponseModel,
    GetKnowledgeBaseFolderResponseModel,
]
# TypeAdapter for runtime validation of DocumentRefreshResponse
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

DocumentRefreshResponse_adapter = TypeAdapter(DocumentRefreshResponse)
