from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .ast_node_output import AstNodeOutput, AstNodeOutput_adapter
from .ast_string_node_output import AstStringNodeOutput
from .ast_number_node_output import AstNumberNodeOutput
from .ast_boolean_node_output import AstBooleanNodeOutput
from .ast_null_node_output import AstNullNodeOutput
from .astllm_node_output import AstllmNodeOutput
from .ast_dynamic_variable_node_output import AstDynamicVariableNodeOutput
from .ast_or_operator_node_output import AstOrOperatorNodeOutput
from .ast_and_operator_node_output import AstAndOperatorNodeOutput
from .ast_equals_operator_node_output import AstEqualsOperatorNodeOutput
from .ast_not_equals_operator_node_output import AstNotEqualsOperatorNodeOutput
from .ast_greater_than_operator_node_output import AstGreaterThanOperatorNodeOutput
from .ast_less_than_operator_node_output import AstLessThanOperatorNodeOutput
from .ast_greater_than_or_equals_operator_node_output import (
    AstGreaterThanOrEqualsOperatorNodeOutput,
)
from .ast_less_than_or_equals_operator_node_output import (
    AstLessThanOrEqualsOperatorNodeOutput,
)
from .ast_addition_operator_node_output import AstAdditionOperatorNodeOutput
from .ast_subtraction_operator_node_output import AstSubtractionOperatorNodeOutput
from .ast_multiplication_operator_node_output import AstMultiplicationOperatorNodeOutput
from .ast_division_operator_node_output import AstDivisionOperatorNodeOutput
from .ast_conditional_operator_node_output import AstConditionalOperatorNodeOutput

WorkflowExpressionConditionModelOutputType = typing.Union[
    typing.Literal["expression"], typing.Any
]


class WorkflowExpressionConditionModelOutput(BaseModel):
    """WorkflowExpressionConditionModelOutput

    :param label: Optional human-readable label for the condition used throughout the UI.
    :type label: str
    :param type: type
    :type type: WorkflowExpressionConditionModelOutputType
    :param expression: expression
    :type expression: AstNodeOutput
    """

    label: Optional[str] = Field(
        description="Optional human-readable label for the condition used throughout the UI."
    )
    type: WorkflowExpressionConditionModelOutputType = Field(default="expression")
    expression: AstNodeOutput
