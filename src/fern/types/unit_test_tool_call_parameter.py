from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .llm_parameter_evaluation_strategy import LlmParameterEvaluationStrategy
from .regex_parameter_evaluation_strategy import RegexParameterEvaluationStrategy
from .exact_parameter_evaluation_strategy import ExactParameterEvaluationStrategy
from .match_anything_parameter_evaluation_strategy import (
    MatchAnythingParameterEvaluationStrategy,
)


# fernMode variant type for a shared-component member of UnitTestToolCallParameterEval
class UnitTestToolCallParameterEval_Llm(LlmParameterEvaluationStrategy):
    pass


# fernMode variant type for a shared-component member of UnitTestToolCallParameterEval
class UnitTestToolCallParameterEval_Regex(RegexParameterEvaluationStrategy):
    pass


# fernMode variant type for a shared-component member of UnitTestToolCallParameterEval
class UnitTestToolCallParameterEval_Exact(ExactParameterEvaluationStrategy):
    pass


# fernMode variant type for a shared-component member of UnitTestToolCallParameterEval
class UnitTestToolCallParameterEval_Anything(MatchAnythingParameterEvaluationStrategy):
    pass


# Union type for UnitTestToolCallParameterEval
# Pydantic will attempt to validate against each type in order
UnitTestToolCallParameterEval = Union[
    LlmParameterEvaluationStrategy,
    RegexParameterEvaluationStrategy,
    ExactParameterEvaluationStrategy,
    MatchAnythingParameterEvaluationStrategy,
]
# TypeAdapter for runtime validation of UnitTestToolCallParameterEval
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

UnitTestToolCallParameterEval_adapter = TypeAdapter(UnitTestToolCallParameterEval)


class UnitTestToolCallParameter(BaseModel):
    """UnitTestToolCallParameter

    :param eval: eval
    :type eval: UnitTestToolCallParameterEval
    :param path: path
    :type path: str
    """

    eval: UnitTestToolCallParameterEval
    path: str
