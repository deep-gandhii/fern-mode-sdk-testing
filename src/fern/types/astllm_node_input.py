from __future__ import annotations
import typing
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .llm_literal_json_schema_property import LlmLiteralJsonSchemaProperty

AstllmNodeInput1Type = typing.Union[typing.Literal["llm"], typing.Any]


class AstllmNodeInput1(BaseModel):
    """AstllmNodeInput1

    :param type: type, defaults to None
    :type type: AstllmNodeInput1Type, optional
    :param value_schema: value_schema
    :type value_schema: LlmLiteralJsonSchemaProperty
    """

    type: Optional[AstllmNodeInput1Type] = Field(default=None)
    value_schema: LlmLiteralJsonSchemaProperty


AstllmNodeInput2Type = typing.Union[typing.Literal["llm"], typing.Any]


class AstllmNodeInput2(BaseModel):
    """AstllmNodeInput2

    :param type: type, defaults to None
    :type type: AstllmNodeInput2Type, optional
    :param prompt: The prompt to evaluate to a boolean value. Deprecated. Use a boolean schema instead.
    :type prompt: str
    """

    type: Optional[AstllmNodeInput2Type] = Field(default=None)
    prompt: str = Field(
        description="The prompt to evaluate to a boolean value. Deprecated. Use a boolean schema instead."
    )


# Union type for AstllmNodeInput
# Pydantic will attempt to validate against each type in order
AstllmNodeInput = Union[AstllmNodeInput1, AstllmNodeInput2]
# TypeAdapter for runtime validation of AstllmNodeInput
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AstllmNodeInput_adapter = TypeAdapter(AstllmNodeInput)
