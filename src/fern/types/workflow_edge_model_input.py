from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .workflow_unconditional_model_input import WorkflowUnconditionalModelInput
from .workflow_llm_condition_model_input import WorkflowLlmConditionModelInput
from .workflow_result_condition_model_input import WorkflowResultConditionModelInput
from .workflow_expression_condition_model_input import (
    WorkflowExpressionConditionModelInput,
)


# fernMode variant type for a shared-component member of WorkflowEdgeModelInputForwardCondition
class WorkflowEdgeModelInputForwardCondition_Unconditional(
    WorkflowUnconditionalModelInput
):
    pass


# fernMode variant type for a shared-component member of WorkflowEdgeModelInputForwardCondition
class WorkflowEdgeModelInputForwardCondition_Llm(WorkflowLlmConditionModelInput):
    pass


# fernMode variant type for a shared-component member of WorkflowEdgeModelInputForwardCondition
class WorkflowEdgeModelInputForwardCondition_Result(WorkflowResultConditionModelInput):
    pass


# fernMode variant type for a shared-component member of WorkflowEdgeModelInputForwardCondition
class WorkflowEdgeModelInputForwardCondition_Expression(
    WorkflowExpressionConditionModelInput
):
    pass


# Union type for WorkflowEdgeModelInputForwardCondition
# Pydantic will attempt to validate against each type in order
WorkflowEdgeModelInputForwardCondition = Union[
    WorkflowUnconditionalModelInput,
    WorkflowLlmConditionModelInput,
    WorkflowResultConditionModelInput,
    WorkflowExpressionConditionModelInput,
]
# TypeAdapter for runtime validation of WorkflowEdgeModelInputForwardCondition
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkflowEdgeModelInputForwardCondition_adapter = TypeAdapter(
    WorkflowEdgeModelInputForwardCondition
)


# fernMode variant type for a shared-component member of WorkflowEdgeModelInputBackwardCondition
class WorkflowEdgeModelInputBackwardCondition_Unconditional(
    WorkflowUnconditionalModelInput
):
    pass


# fernMode variant type for a shared-component member of WorkflowEdgeModelInputBackwardCondition
class WorkflowEdgeModelInputBackwardCondition_Llm(WorkflowLlmConditionModelInput):
    pass


# fernMode variant type for a shared-component member of WorkflowEdgeModelInputBackwardCondition
class WorkflowEdgeModelInputBackwardCondition_Result(WorkflowResultConditionModelInput):
    pass


# fernMode variant type for a shared-component member of WorkflowEdgeModelInputBackwardCondition
class WorkflowEdgeModelInputBackwardCondition_Expression(
    WorkflowExpressionConditionModelInput
):
    pass


# Union type for WorkflowEdgeModelInputBackwardCondition
# Pydantic will attempt to validate against each type in order
WorkflowEdgeModelInputBackwardCondition = Union[
    WorkflowUnconditionalModelInput,
    WorkflowLlmConditionModelInput,
    WorkflowResultConditionModelInput,
    WorkflowExpressionConditionModelInput,
]
# TypeAdapter for runtime validation of WorkflowEdgeModelInputBackwardCondition
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkflowEdgeModelInputBackwardCondition_adapter = TypeAdapter(
    WorkflowEdgeModelInputBackwardCondition
)


class WorkflowEdgeModelInput(BaseModel):
    """WorkflowEdgeModelInput

    :param source: ID of the source node.
    :type source: str
    :param target: ID of the target node.
    :type target: str
    :param forward_condition: Condition that must be met for the edge to be traversed in the forward direction (source to target)., defaults to None
    :type forward_condition: WorkflowEdgeModelInputForwardCondition, optional
    :param backward_condition: Condition that must be met for the edge to be traversed in the backward direction (target to source)., defaults to None
    :type backward_condition: WorkflowEdgeModelInputBackwardCondition, optional
    """

    source: str = Field(description="ID of the source node.")
    target: str = Field(description="ID of the target node.")
    forward_condition: Optional[WorkflowEdgeModelInputForwardCondition] = Field(
        default=None,
        description="Condition that must be met for the edge to be traversed in the forward direction (source to target).",
    )
    backward_condition: Optional[WorkflowEdgeModelInputBackwardCondition] = Field(
        default=None,
        description="Condition that must be met for the edge to be traversed in the backward direction (target to source).",
    )
