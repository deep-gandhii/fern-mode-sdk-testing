from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import TYPE_CHECKING
from .ast_string_node_input import AstStringNodeInput
from .ast_number_node_input import AstNumberNodeInput
from .ast_boolean_node_input import AstBooleanNodeInput
from .ast_null_node_input import AstNullNodeInput
from .astllm_node_input import AstllmNodeInput, AstllmNodeInput_adapter
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


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_StringLiteral(AstStringNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_NumberLiteral(AstNumberNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_BooleanLiteral(AstBooleanNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_NullLiteral(AstNullNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_DynamicVariable(AstDynamicVariableNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_OrOperator(AstOrOperatorNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_AndOperator(AstAndOperatorNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_EqOperator(AstEqualsOperatorNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_NeqOperator(AstNotEqualsOperatorNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_GtOperator(AstGreaterThanOperatorNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_LtOperator(AstLessThanOperatorNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_GteOperator(AstGreaterThanOrEqualsOperatorNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_LteOperator(AstLessThanOrEqualsOperatorNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_AddOperator(AstAdditionOperatorNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_SubOperator(AstSubtractionOperatorNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_MulOperator(AstMultiplicationOperatorNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_DivOperator(AstDivisionOperatorNodeInput):
    pass


# fernMode variant type for a shared-component member of AstNodeInput
class AstNodeInput_ConditionalOperator(AstConditionalOperatorNodeInput):
    pass


# Union type for AstNodeInput
# Pydantic will attempt to validate against each type in order
AstNodeInput = Union[
    AstStringNodeInput,
    AstNumberNodeInput,
    AstBooleanNodeInput,
    AstNullNodeInput,
    AstllmNodeInput1,
    AstllmNodeInput2,
    AstDynamicVariableNodeInput,
    AstOrOperatorNodeInput,
    AstAndOperatorNodeInput,
    AstEqualsOperatorNodeInput,
    AstNotEqualsOperatorNodeInput,
    AstGreaterThanOperatorNodeInput,
    AstLessThanOperatorNodeInput,
    AstGreaterThanOrEqualsOperatorNodeInput,
    AstLessThanOrEqualsOperatorNodeInput,
    AstAdditionOperatorNodeInput,
    AstSubtractionOperatorNodeInput,
    AstMultiplicationOperatorNodeInput,
    AstDivisionOperatorNodeInput,
    AstConditionalOperatorNodeInput,
]
# TypeAdapter for runtime validation of AstNodeInput
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AstNodeInput_adapter = TypeAdapter(AstNodeInput)
