from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .rag_index_batch_successful_response_model import (
    RagIndexBatchSuccessfulResponseModel,
)
from .batch_failure_response_model import BatchFailureResponseModel


# fernMode variant type for a shared-component member of KnowledgeBaseGetOrCreateRagIndexesResponse
class KnowledgeBaseGetOrCreateRagIndexesResponse_Success(
    RagIndexBatchSuccessfulResponseModel
):
    pass


# fernMode variant type for a shared-component member of KnowledgeBaseGetOrCreateRagIndexesResponse
class KnowledgeBaseGetOrCreateRagIndexesResponse_Failure(BatchFailureResponseModel):
    pass


# Union type for KnowledgeBaseGetOrCreateRagIndexesResponse
# Pydantic will attempt to validate against each type in order
KnowledgeBaseGetOrCreateRagIndexesResponse = Union[
    RagIndexBatchSuccessfulResponseModel, BatchFailureResponseModel
]
# TypeAdapter for runtime validation of KnowledgeBaseGetOrCreateRagIndexesResponse
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

KnowledgeBaseGetOrCreateRagIndexesResponse_adapter = TypeAdapter(
    KnowledgeBaseGetOrCreateRagIndexesResponse
)
