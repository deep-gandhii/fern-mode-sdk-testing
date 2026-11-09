from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .llm_literal_json_schema_property import LlmLiteralJsonSchemaProperty

AstllmNodeOutputType = typing.Union[typing.Literal["llm"], typing.Any]


class AstllmNodeOutput(BaseModel):
    """AstllmNodeOutput

    :param type: type
    :type type: AstllmNodeOutputType
    :param value_schema: value_schema
    :type value_schema: LlmLiteralJsonSchemaProperty
    :param prompt: The prompt to evaluate to a boolean value. Deprecated. Use a boolean schema instead.
    :type prompt: str
    """

    type: AstllmNodeOutputType = Field(default="llm")
    value_schema: LlmLiteralJsonSchemaProperty
    prompt: str = Field(
        description="The prompt to evaluate to a boolean value. Deprecated. Use a boolean schema instead."
    )
