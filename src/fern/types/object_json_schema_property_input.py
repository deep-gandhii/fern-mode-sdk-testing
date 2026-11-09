from __future__ import annotations
import typing
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import TYPE_CHECKING
from typing import Dict
from .utils.base_model import BaseModel
from .required_constraints import RequiredConstraints
from .literal_json_schema_property import LiteralJsonSchemaProperty

if TYPE_CHECKING:
    from .array_json_schema_property_input import ArrayJsonSchemaPropertyInput


class ObjectJsonSchemaPropertyInput(BaseModel):
    """ObjectJsonSchemaPropertyInput

    :param property_kind: property_kind, defaults to None
    :type property_kind: ObjectJsonSchemaPropertyInputPropertyKind, optional
    :param description: description, defaults to None
    :type description: str, optional
    :param dynamic_variable: When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted., defaults to None
    :type dynamic_variable: str, optional
    :param constant_value: When set, the entire object uses this constant JSON value at runtime. Mutually exclusive with description (LLM-provided object), dynamic_variable, and is_omitted., defaults to None
    :type constant_value: Dict[str, Any], optional
    :param is_omitted: If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value., defaults to None
    :type is_omitted: bool, optional
    :param type: type, defaults to None
    :type type: ObjectJsonSchemaPropertyInputType, optional
    :param required: required, defaults to None
    :type required: List[str], optional
    :param properties: properties, defaults to None
    :type properties: Dict[str, ObjectJsonSchemaPropertyInputPropertiesValue], optional
    :param required_constraints: required_constraints, defaults to None
    :type required_constraints: RequiredConstraints, optional
    """

    property_kind: Optional[ObjectJsonSchemaPropertyInputPropertyKind] = Field(
        default=None
    )
    description: Optional[str] = Field(default=None)
    dynamic_variable: Optional[str] = Field(
        default=None,
        description="When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.",
    )
    constant_value: Optional[Dict[str, Any]] = Field(
        default=None,
        description="When set, the entire object uses this constant JSON value at runtime. Mutually exclusive with description (LLM-provided object), dynamic_variable, and is_omitted.",
    )
    is_omitted: Optional[bool] = Field(
        default=None,
        description="If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.",
    )
    type: Optional[ObjectJsonSchemaPropertyInputType] = Field(default=None)
    required: Optional[List[str]] = Field(default=None)
    properties: Optional[Dict[str, ObjectJsonSchemaPropertyInputPropertiesValue]] = (
        Field(default=None)
    )
    required_constraints: Optional[RequiredConstraints] = Field(default=None)


ObjectJsonSchemaPropertyInputPropertyKind = typing.Union[
    typing.Literal["array", "object"], typing.Any
]

ObjectJsonSchemaPropertyInputType = typing.Union[typing.Literal["object"], typing.Any]

# Union type for ObjectJsonSchemaPropertyInputPropertiesValue
# Pydantic will attempt to validate against each type in order
ObjectJsonSchemaPropertyInputPropertiesValue = Union[
    LiteralJsonSchemaProperty,
    ObjectJsonSchemaPropertyInput,
    "ArrayJsonSchemaPropertyInput",
]
# TypeAdapter for runtime validation of ObjectJsonSchemaPropertyInputPropertiesValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter


class _ObjectJsonSchemaPropertyInputPropertiesValueAdapterProxy:
    _adapter = None

    def __getattr__(self, attr):
        if _ObjectJsonSchemaPropertyInputPropertiesValueAdapterProxy._adapter is None:
            from . import ArrayJsonSchemaPropertyInput

            _ObjectJsonSchemaPropertyInputPropertiesValueAdapterProxy._adapter = (
                TypeAdapter(ObjectJsonSchemaPropertyInputPropertiesValue)
            )
        return getattr(
            _ObjectJsonSchemaPropertyInputPropertiesValueAdapterProxy._adapter, attr
        )


ObjectJsonSchemaPropertyInputPropertiesValue_adapter = (
    _ObjectJsonSchemaPropertyInputPropertiesValueAdapterProxy()
)


# Rebuild model to resolve forward references from submodels
try:
    ObjectJsonSchemaPropertyInput.model_rebuild()
except NameError:
    # A member of an import cycle is only imported under TYPE_CHECKING, so some forward refs
    # cannot resolve this early. The batched model_rebuild(_types_namespace=...) in
    # models/__init__.py resolves them once every model is loaded.
    #
    # NameError, not Exception: pydantic raises PydanticUndefinedAnnotation for an unresolved
    # forward reference and that subclasses NameError, so this catches exactly the expected case
    # and leaves a genuine error (a bad field type, a missing import) loud.
    pass


# Note: This model has circular dependencies with: object_json_schema_property_input, array_json_schema_property_input
# Forward references will be resolved when model_rebuild() is called from models/__init__.py
