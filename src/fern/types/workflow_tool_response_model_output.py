from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import TYPE_CHECKING
from .utils.base_model import BaseModel
from .workflow_tool_edge_step_model import WorkflowToolEdgeStepModel
from .workflow_tool_nested_tools_step_model_output import (
    WorkflowToolNestedToolsStepModelOutput,
)
from .workflow_tool_max_iterations_exceeded_step_model import (
    WorkflowToolMaxIterationsExceededStepModel,
)


# fernMode variant type for a shared-component member of WorkflowToolResponseModelOutputStepsItem
class WorkflowToolResponseModelOutputStepsItem_Edge(WorkflowToolEdgeStepModel):
    pass


# fernMode variant type for a shared-component member of WorkflowToolResponseModelOutputStepsItem
class WorkflowToolResponseModelOutputStepsItem_NestedTools(
    WorkflowToolNestedToolsStepModelOutput
):
    pass


# fernMode variant type for a shared-component member of WorkflowToolResponseModelOutputStepsItem
class WorkflowToolResponseModelOutputStepsItem_MaxIterationsExceeded(
    WorkflowToolMaxIterationsExceededStepModel
):
    pass


# Union type for WorkflowToolResponseModelOutputStepsItem
# Pydantic will attempt to validate against each type in order
WorkflowToolResponseModelOutputStepsItem = Union[
    WorkflowToolEdgeStepModel,
    WorkflowToolNestedToolsStepModelOutput,
    WorkflowToolMaxIterationsExceededStepModel,
]
# TypeAdapter for runtime validation of WorkflowToolResponseModelOutputStepsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkflowToolResponseModelOutputStepsItem_adapter = TypeAdapter(
    WorkflowToolResponseModelOutputStepsItem
)


class WorkflowToolResponseModelOutput(BaseModel):
    """A common model for workflow tool responses.

    :param steps: steps, defaults to None
    :type steps: List[WorkflowToolResponseModelOutputStepsItem], optional
    """

    steps: Optional[List[WorkflowToolResponseModelOutputStepsItem]] = Field(
        default=None
    )


# Note: This model has circular dependencies with: workflow_tool_nested_tools_step_model_output
# Forward references will be resolved when model_rebuild() is called from models/__init__.py
