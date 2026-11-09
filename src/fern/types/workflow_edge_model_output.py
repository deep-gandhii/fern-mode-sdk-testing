from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .workflow_unconditional_model_output import WorkflowUnconditionalModelOutput
from .workflow_llm_condition_model_output import WorkflowLlmConditionModelOutput
from .workflow_result_condition_model_output import WorkflowResultConditionModelOutput
from .workflow_expression_condition_model_output import (
    WorkflowExpressionConditionModelOutput,
)


# fernMode variant type for a shared-component member of WorkflowEdgeModelOutputForwardCondition
class WorkflowEdgeModelOutputForwardCondition_Unconditional(
    WorkflowUnconditionalModelOutput
):
    pass


# fernMode variant type for a shared-component member of WorkflowEdgeModelOutputForwardCondition
class WorkflowEdgeModelOutputForwardCondition_Llm(WorkflowLlmConditionModelOutput):
    pass


# fernMode variant type for a shared-component member of WorkflowEdgeModelOutputForwardCondition
class WorkflowEdgeModelOutputForwardCondition_Result(
    WorkflowResultConditionModelOutput
):
    pass


# fernMode variant type for a shared-component member of WorkflowEdgeModelOutputForwardCondition
class WorkflowEdgeModelOutputForwardCondition_Expression(
    WorkflowExpressionConditionModelOutput
):
    pass


# Union type for WorkflowEdgeModelOutputForwardCondition
# Pydantic will attempt to validate against each type in order
WorkflowEdgeModelOutputForwardCondition = Union[
    WorkflowUnconditionalModelOutput,
    WorkflowLlmConditionModelOutput,
    WorkflowResultConditionModelOutput,
    WorkflowExpressionConditionModelOutput,
]
# TypeAdapter for runtime validation of WorkflowEdgeModelOutputForwardCondition
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkflowEdgeModelOutputForwardCondition_adapter = TypeAdapter(
    WorkflowEdgeModelOutputForwardCondition
)


# fernMode variant type for a shared-component member of WorkflowEdgeModelOutputBackwardCondition
class WorkflowEdgeModelOutputBackwardCondition_Unconditional(
    WorkflowUnconditionalModelOutput
):
    pass


# fernMode variant type for a shared-component member of WorkflowEdgeModelOutputBackwardCondition
class WorkflowEdgeModelOutputBackwardCondition_Llm(WorkflowLlmConditionModelOutput):
    pass


# fernMode variant type for a shared-component member of WorkflowEdgeModelOutputBackwardCondition
class WorkflowEdgeModelOutputBackwardCondition_Result(
    WorkflowResultConditionModelOutput
):
    pass


# fernMode variant type for a shared-component member of WorkflowEdgeModelOutputBackwardCondition
class WorkflowEdgeModelOutputBackwardCondition_Expression(
    WorkflowExpressionConditionModelOutput
):
    pass


# Union type for WorkflowEdgeModelOutputBackwardCondition
# Pydantic will attempt to validate against each type in order
WorkflowEdgeModelOutputBackwardCondition = Union[
    WorkflowUnconditionalModelOutput,
    WorkflowLlmConditionModelOutput,
    WorkflowResultConditionModelOutput,
    WorkflowExpressionConditionModelOutput,
]
# TypeAdapter for runtime validation of WorkflowEdgeModelOutputBackwardCondition
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkflowEdgeModelOutputBackwardCondition_adapter = TypeAdapter(
    WorkflowEdgeModelOutputBackwardCondition
)


class WorkflowEdgeModelOutput(BaseModel):
    """WorkflowEdgeModelOutput

    :param source: ID of the source node.
    :type source: str
    :param target: ID of the target node.
    :type target: str
    :param forward_condition: Condition that must be met for the edge to be traversed in the forward direction (source to target).
    :type forward_condition: WorkflowEdgeModelOutputForwardCondition
    :param backward_condition: Condition that must be met for the edge to be traversed in the backward direction (target to source).
    :type backward_condition: WorkflowEdgeModelOutputBackwardCondition
    """

    source: str = Field(description="ID of the source node.")
    target: str = Field(description="ID of the target node.")
    forward_condition: Optional[WorkflowEdgeModelOutputForwardCondition] = Field(
        description="Condition that must be met for the edge to be traversed in the forward direction (source to target)."
    )
    backward_condition: Optional[WorkflowEdgeModelOutputBackwardCondition] = Field(
        description="Condition that must be met for the edge to be traversed in the backward direction (target to source)."
    )
