from __future__ import annotations
import typing
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel

Type12 = typing.Union[
    typing.Literal["boolean", "string", "integer", "number"], typing.Any
]


# Union type for LlmLiteralJsonSchemaPropertyType
# Pydantic will attempt to validate against each type in order
LlmLiteralJsonSchemaPropertyType = Union[str, List[str]]
# TypeAdapter for runtime validation of LlmLiteralJsonSchemaPropertyType
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

LlmLiteralJsonSchemaPropertyType_adapter = TypeAdapter(LlmLiteralJsonSchemaPropertyType)


class LlmLiteralJsonSchemaProperty(BaseModel):
    """LlmLiteralJsonSchemaProperty

    :param type: type
    :type type: LlmLiteralJsonSchemaPropertyType
    :param description: description
    :type description: str
    :param enum: List of allowed string values for string type parameters, defaults to None
    :type enum: List[str], optional
    """

    type: LlmLiteralJsonSchemaPropertyType
    description: str
    enum: Optional[List[str]] = Field(
        default=None,
        description="List of allowed string values for string type parameters",
    )
