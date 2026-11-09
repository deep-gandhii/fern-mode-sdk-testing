from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import TYPE_CHECKING
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


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_StringLiteral(AstStringNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_NumberLiteral(AstNumberNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_BooleanLiteral(AstBooleanNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_NullLiteral(AstNullNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_Llm(AstllmNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_DynamicVariable(AstDynamicVariableNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_OrOperator(AstOrOperatorNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_AndOperator(AstAndOperatorNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_EqOperator(AstEqualsOperatorNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_NeqOperator(AstNotEqualsOperatorNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_GtOperator(AstGreaterThanOperatorNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_LtOperator(AstLessThanOperatorNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_GteOperator(AstGreaterThanOrEqualsOperatorNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_LteOperator(AstLessThanOrEqualsOperatorNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_AddOperator(AstAdditionOperatorNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_SubOperator(AstSubtractionOperatorNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_MulOperator(AstMultiplicationOperatorNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_DivOperator(AstDivisionOperatorNodeOutput):
    pass


# fernMode variant type for a shared-component member of AstNodeOutput
class AstNodeOutput_ConditionalOperator(AstConditionalOperatorNodeOutput):
    pass


# Union type for AstNodeOutput
# Pydantic will attempt to validate against each type in order
AstNodeOutput = Union[
    AstStringNodeOutput,
    AstNumberNodeOutput,
    AstBooleanNodeOutput,
    AstNullNodeOutput,
    AstllmNodeOutput,
    AstDynamicVariableNodeOutput,
    AstOrOperatorNodeOutput,
    AstAndOperatorNodeOutput,
    AstEqualsOperatorNodeOutput,
    AstNotEqualsOperatorNodeOutput,
    AstGreaterThanOperatorNodeOutput,
    AstLessThanOperatorNodeOutput,
    AstGreaterThanOrEqualsOperatorNodeOutput,
    AstLessThanOrEqualsOperatorNodeOutput,
    AstAdditionOperatorNodeOutput,
    AstSubtractionOperatorNodeOutput,
    AstMultiplicationOperatorNodeOutput,
    AstDivisionOperatorNodeOutput,
    AstConditionalOperatorNodeOutput,
]
# TypeAdapter for runtime validation of AstNodeOutput
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AstNodeOutput_adapter = TypeAdapter(AstNodeOutput)
