from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .ast_node_input import AstNodeInput, AstNodeInput_adapter
from .ast_string_node_input import AstStringNodeInput
from .ast_number_node_input import AstNumberNodeInput
from .ast_boolean_node_input import AstBooleanNodeInput
from .ast_null_node_input import AstNullNodeInput
from .astllm_node_input import AstllmNodeInput1
from .astllm_node_input import AstllmNodeInput2
from .ast_dynamic_variable_node_input import AstDynamicVariableNodeInput
from .ast_or_operator_node_input import AstOrOperatorNodeInput
from .ast_and_operator_node_input import AstAndOperatorNodeInput
from .ast_equals_operator_node_input import AstEqualsOperatorNodeInput
from .ast_not_equals_operator_node_input import AstNotEqualsOperatorNodeInput
from .ast_greater_than_operator_node_input import AstGreaterThanOperatorNodeInput
from .ast_less_than_operator_node_input import AstLessThanOperatorNodeInput
from .ast_greater_than_or_equals_operator_node_input import (
    AstGreaterThanOrEqualsOperatorNodeInput,
)
from .ast_less_than_or_equals_operator_node_input import (
    AstLessThanOrEqualsOperatorNodeInput,
)
from .ast_addition_operator_node_input import AstAdditionOperatorNodeInput
from .ast_subtraction_operator_node_input import AstSubtractionOperatorNodeInput
from .ast_multiplication_operator_node_input import AstMultiplicationOperatorNodeInput
from .ast_division_operator_node_input import AstDivisionOperatorNodeInput
from .ast_conditional_operator_node_input import AstConditionalOperatorNodeInput

WorkflowExpressionConditionModelInputType = typing.Union[
    typing.Literal["expression"], typing.Any
]


class WorkflowExpressionConditionModelInput(BaseModel):
    """WorkflowExpressionConditionModelInput

    :param label: Optional human-readable label for the condition used throughout the UI., defaults to None
    :type label: str, optional
    :param type: type, defaults to None
    :type type: WorkflowExpressionConditionModelInputType, optional
    :param expression: expression
    :type expression: AstNodeInput
    """

    label: Optional[str] = Field(
        default=None,
        description="Optional human-readable label for the condition used throughout the UI.",
    )
    type: Optional[WorkflowExpressionConditionModelInputType] = Field(default=None)
    expression: AstNodeInput
