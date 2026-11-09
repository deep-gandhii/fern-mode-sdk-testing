from __future__ import annotations
import typing
from typing import List
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
    from .ast_conditional_operator_node_input import AstConditionalOperatorNodeInput

AstOrOperatorNodeInputType = typing.Union[typing.Literal["or_operator"], typing.Any]


class AstOrOperatorNodeInput(BaseModel):
    """AstOrOperatorNodeInput

    :param type: type, defaults to None
    :type type: AstOrOperatorNodeInputType, optional
    :param children: Child nodes of the logical operator.
    :type children: List[AstNodeInput]
    """

    type: Optional[AstOrOperatorNodeInputType] = Field(default=None)
    children: List[AstNodeInput] = Field(
        description="Child nodes of the logical operator."
    )


# Note: This model has circular dependencies with: ast_node_input
# Forward references will be resolved when model_rebuild() is called from models/__init__.py
