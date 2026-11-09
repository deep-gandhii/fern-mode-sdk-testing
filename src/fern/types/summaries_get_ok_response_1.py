from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .agent_summary_batch_successful_response_model import (
    AgentSummaryBatchSuccessfulResponseModel,
)
from .batch_failure_response_model import BatchFailureResponseModel


# fernMode variant type for a shared-component member of SummariesGetOkResponse1
class SummariesGetOkResponse1_Success(AgentSummaryBatchSuccessfulResponseModel):
    pass


# fernMode variant type for a shared-component member of SummariesGetOkResponse1
class SummariesGetOkResponse1_Failure(BatchFailureResponseModel):
    pass


# Union type for SummariesGetOkResponse1
# Pydantic will attempt to validate against each type in order
SummariesGetOkResponse1 = Union[
    AgentSummaryBatchSuccessfulResponseModel, BatchFailureResponseModel
]
# TypeAdapter for runtime validation of SummariesGetOkResponse1
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

SummariesGetOkResponse1_adapter = TypeAdapter(SummariesGetOkResponse1)
