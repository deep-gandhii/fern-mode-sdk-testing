from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import TYPE_CHECKING
from .utils.base_model import BaseModel
from .ast_string_node_input import AstStringNodeInput
from .ast_number_node_input import AstNumberNodeInput
from .ast_boolean_node_input import AstBooleanNodeInput
from .ast_null_node_input import AstNullNodeInput
from .astllm_node_input import AstllmNodeInput1
from .astllm_node_input import AstllmNodeInput2
from .ast_dynamic_variable_node_input import AstDynamicVariableNodeInput

if TYPE_CHECKING:
    from .ast_node_input import AstNodeInput, AstNodeInput_adapter
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
    from .ast_multiplication_operator_node_input import (
        AstMultiplicationOperatorNodeInput,
    )
    from .ast_division_operator_node_input import AstDivisionOperatorNodeInput

AstConditionalOperatorNodeInputType = typing.Union[
    typing.Literal["conditional_operator"], typing.Any
]


class AstConditionalOperatorNodeInput(BaseModel):
    """AstConditionalOperatorNodeInput

    :param type: type, defaults to None
    :type type: AstConditionalOperatorNodeInputType, optional
    :param condition: condition
    :type condition: AstNodeInput
    :param true_expression: true_expression
    :type true_expression: AstNodeInput
    :param false_expression: false_expression
    :type false_expression: AstNodeInput
    """

    type: Optional[AstConditionalOperatorNodeInputType] = Field(default=None)
    condition: AstNodeInput
    true_expression: AstNodeInput = Field(
        alias="trueExpression", serialization_alias="trueExpression"
    )
    false_expression: AstNodeInput = Field(
        alias="falseExpression", serialization_alias="falseExpression"
    )


# Note: This model has circular dependencies with: ast_node_input
# Forward references will be resolved when model_rebuild() is called from models/__init__.py
