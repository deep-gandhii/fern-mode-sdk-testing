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
from .llm import Llm

AnalysisPropertyType = typing.Union[
    typing.Literal["boolean", "string", "integer", "number"], typing.Any
]

# Union type for AnalysisPropertyConstantValue
# Pydantic will attempt to validate against each type in order
AnalysisPropertyConstantValue = Union[str, int, float, bool]
# TypeAdapter for runtime validation of AnalysisPropertyConstantValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AnalysisPropertyConstantValue_adapter = TypeAdapter(AnalysisPropertyConstantValue)


class AnalysisProperty(BaseModel):
    """Data collection property with optional per-item LLM override for post-call analysis. TODO: migrate to composition (value_schema: LiteralJsonSchemaProperty + llm) instead of inheritance, so this generalizes cleanly to object/array schemas in the future.

    :param type: type
    :type type: AnalysisPropertyType
    :param description: The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted., defaults to None
    :type description: str, optional
    :param enum: List of allowed string values for string type parameters, defaults to None
    :type enum: List[str], optional
    :param is_system_provided: If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted., defaults to None
    :type is_system_provided: bool, optional
    :param dynamic_variable: The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted., defaults to None
    :type dynamic_variable: str, optional
    :param allowed_values_dynamic_variable: When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable. Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted., defaults to None
    :type allowed_values_dynamic_variable: str, optional
    :param constant_value: A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted., defaults to None
    :type constant_value: AnalysisPropertyConstantValue, optional
    :param is_omitted: If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value., defaults to None
    :type is_omitted: bool, optional
    :param llm: LLM model to use for this analysis item. If not set, uses agent's analysis_llm default., defaults to None
    :type llm: Llm, optional
    """

    type: AnalysisPropertyType
    description: Optional[str] = Field(
        default=None,
        description="The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.",
    )
    enum: Optional[List[str]] = Field(
        default=None,
        description="List of allowed string values for string type parameters",
    )
    is_system_provided: Optional[bool] = Field(
        default=None,
        description="If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.",
    )
    dynamic_variable: Optional[str] = Field(
        default=None,
        description="The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.",
    )
    allowed_values_dynamic_variable: Optional[str] = Field(
        default=None,
        description="When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable. Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.",
    )
    constant_value: Optional[AnalysisPropertyConstantValue] = Field(
        default=None,
        description="A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.",
    )
    is_omitted: Optional[bool] = Field(
        default=None,
        description="If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.",
    )
    llm: Optional[Llm] = Field(
        default=None,
        description="LLM model to use for this analysis item. If not set, uses agent's analysis_llm default.",
    )
