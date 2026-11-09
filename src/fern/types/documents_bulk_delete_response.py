from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .knowledge_base_bulk_delete_successful_response_model import (
    KnowledgeBaseBulkDeleteSuccessfulResponseModel,
)
from .batch_failure_response_model import BatchFailureResponseModel


# fernMode variant type for a shared-component member of DocumentsBulkDeleteResponse
class DocumentsBulkDeleteResponse_Success(
    KnowledgeBaseBulkDeleteSuccessfulResponseModel
):
    pass


# fernMode variant type for a shared-component member of DocumentsBulkDeleteResponse
class DocumentsBulkDeleteResponse_Failure(BatchFailureResponseModel):
    pass


# Union type for DocumentsBulkDeleteResponse
# Pydantic will attempt to validate against each type in order
DocumentsBulkDeleteResponse = Union[
    KnowledgeBaseBulkDeleteSuccessfulResponseModel, BatchFailureResponseModel
]
# TypeAdapter for runtime validation of DocumentsBulkDeleteResponse
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

DocumentsBulkDeleteResponse_adapter = TypeAdapter(DocumentsBulkDeleteResponse)
