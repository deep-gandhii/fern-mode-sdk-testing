from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import TYPE_CHECKING
from .utils.base_model import BaseModel
from .ast_string_node_output import AstStringNodeOutput
from .ast_number_node_output import AstNumberNodeOutput
from .ast_boolean_node_output import AstBooleanNodeOutput
from .ast_null_node_output import AstNullNodeOutput
from .astllm_node_output import AstllmNodeOutput
from .ast_dynamic_variable_node_output import AstDynamicVariableNodeOutput

if TYPE_CHECKING:
    from .ast_node_output import AstNodeOutput, AstNodeOutput_adapter
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
    from .ast_subtraction_operator_node_output import AstSubtractionOperatorNodeOutput
    from .ast_multiplication_operator_node_output import (
        AstMultiplicationOperatorNodeOutput,
    )
    from .ast_division_operator_node_output import AstDivisionOperatorNodeOutput
    from .ast_conditional_operator_node_output import AstConditionalOperatorNodeOutput

AstAdditionOperatorNodeOutputType = typing.Union[
    typing.Literal["add_operator"], typing.Any
]


class AstAdditionOperatorNodeOutput(BaseModel):
    """AstAdditionOperatorNodeOutput

    :param type: type
    :type type: AstAdditionOperatorNodeOutputType
    :param left: left
    :type left: AstNodeOutput
    :param right: right
    :type right: AstNodeOutput
    """

    type: AstAdditionOperatorNodeOutputType = Field(default="add_operator")
    left: AstNodeOutput
    right: AstNodeOutput


# Note: This model has circular dependencies with: ast_node_output
# Forward references will be resolved when model_rebuild() is called from models/__init__.py
