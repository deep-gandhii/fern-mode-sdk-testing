from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .knowledge_base_summary_batch_successful_response_model import (
    KnowledgeBaseSummaryBatchSuccessfulResponseModel,
)
from .batch_failure_response_model import BatchFailureResponseModel


# fernMode variant type for a shared-component member of SummariesGetOkResponse2
class SummariesGetOkResponse2_Success(KnowledgeBaseSummaryBatchSuccessfulResponseModel):
    pass


# fernMode variant type for a shared-component member of SummariesGetOkResponse2
class SummariesGetOkResponse2_Failure(BatchFailureResponseModel):
    pass


# Union type for SummariesGetOkResponse2
# Pydantic will attempt to validate against each type in order
SummariesGetOkResponse2 = Union[
    KnowledgeBaseSummaryBatchSuccessfulResponseModel, BatchFailureResponseModel
]
# TypeAdapter for runtime validation of SummariesGetOkResponse2
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

SummariesGetOkResponse2_adapter = TypeAdapter(SummariesGetOkResponse2)
