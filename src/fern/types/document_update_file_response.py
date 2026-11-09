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


# fernMode variant type for a shared-component member of DocumentUpdateFileResponse
class DocumentUpdateFileResponse_Url(GetKnowledgeBaseUrlResponseModel):
    pass


# fernMode variant type for a shared-component member of DocumentUpdateFileResponse
class DocumentUpdateFileResponse_File(GetKnowledgeBaseFileResponseModel):
    pass


# fernMode variant type for a shared-component member of DocumentUpdateFileResponse
class DocumentUpdateFileResponse_Text(GetKnowledgeBaseTextResponseModel):
    pass


# fernMode variant type for a shared-component member of DocumentUpdateFileResponse
class DocumentUpdateFileResponse_Folder(GetKnowledgeBaseFolderResponseModel):
    pass


# Union type for DocumentUpdateFileResponse
# Pydantic will attempt to validate against each type in order
DocumentUpdateFileResponse = Union[
    GetKnowledgeBaseUrlResponseModel,
    GetKnowledgeBaseFileResponseModel,
    GetKnowledgeBaseTextResponseModel,
    GetKnowledgeBaseFolderResponseModel,
]
# TypeAdapter for runtime validation of DocumentUpdateFileResponse
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

DocumentUpdateFileResponse_adapter = TypeAdapter(DocumentUpdateFileResponse)
