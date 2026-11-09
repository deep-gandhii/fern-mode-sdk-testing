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
from .workflow_tool_nested_tools_step_model_input import (
    WorkflowToolNestedToolsStepModelInput,
)
from .workflow_tool_max_iterations_exceeded_step_model import (
    WorkflowToolMaxIterationsExceededStepModel,
)


# fernMode variant type for a shared-component member of WorkflowToolResponseModelInputStepsItem
class WorkflowToolResponseModelInputStepsItem_Edge(WorkflowToolEdgeStepModel):
    pass


# fernMode variant type for a shared-component member of WorkflowToolResponseModelInputStepsItem
class WorkflowToolResponseModelInputStepsItem_NestedTools(
    WorkflowToolNestedToolsStepModelInput
):
    pass


# fernMode variant type for a shared-component member of WorkflowToolResponseModelInputStepsItem
class WorkflowToolResponseModelInputStepsItem_MaxIterationsExceeded(
    WorkflowToolMaxIterationsExceededStepModel
):
    pass


# Union type for WorkflowToolResponseModelInputStepsItem
# Pydantic will attempt to validate against each type in order
WorkflowToolResponseModelInputStepsItem = Union[
    WorkflowToolEdgeStepModel,
    WorkflowToolNestedToolsStepModelInput,
    WorkflowToolMaxIterationsExceededStepModel,
]
# TypeAdapter for runtime validation of WorkflowToolResponseModelInputStepsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkflowToolResponseModelInputStepsItem_adapter = TypeAdapter(
    WorkflowToolResponseModelInputStepsItem
)


class WorkflowToolResponseModelInput(BaseModel):
    """A common model for workflow tool responses.

    :param steps: steps, defaults to None
    :type steps: List[WorkflowToolResponseModelInputStepsItem], optional
    """

    steps: Optional[List[WorkflowToolResponseModelInputStepsItem]] = Field(default=None)


# Note: This model has circular dependencies with: workflow_tool_nested_tools_step_model_input
# Forward references will be resolved when model_rebuild() is called from models/__init__.py
