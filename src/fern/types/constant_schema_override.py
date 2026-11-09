from __future__ import annotations
import typing
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel

ConstantSchemaOverrideSource = typing.Union[typing.Literal["constant"], typing.Any]

# Union type for ConstantSchemaOverrideConstantValue
# Pydantic will attempt to validate against each type in order
ConstantSchemaOverrideConstantValue = Union[
    str, int, float, bool, List[Any], Dict[str, Any]
]
# TypeAdapter for runtime validation of ConstantSchemaOverrideConstantValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ConstantSchemaOverrideConstantValue_adapter = TypeAdapter(
    ConstantSchemaOverrideConstantValue
)


class ConstantSchemaOverride(BaseModel):
    """ConstantSchemaOverride

    :param source: source, defaults to None
    :type source: ConstantSchemaOverrideSource, optional
    :param constant_value: The constant value to use
    :type constant_value: ConstantSchemaOverrideConstantValue
    """

    source: Optional[ConstantSchemaOverrideSource] = Field(default=None)
    constant_value: ConstantSchemaOverrideConstantValue = Field(
        description="The constant value to use"
    )
