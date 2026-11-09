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
from .utils.base_model import BaseModel
from .literal_json_schema_property import LiteralJsonSchemaProperty

if TYPE_CHECKING:
    from .object_json_schema_property_output import ObjectJsonSchemaPropertyOutput


class ArrayJsonSchemaPropertyOutput(BaseModel):
    """ArrayJsonSchemaPropertyOutput

    :param description: description, defaults to None
    :type description: str, optional
    :param dynamic_variable: When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted., defaults to None
    :type dynamic_variable: str, optional
    :param constant_value: When set, the entire array uses this constant value at runtime. Mutually exclusive with description (LLM-provided array), dynamic_variable, and is_omitted., defaults to None
    :type constant_value: List[Any], optional
    :param is_omitted: If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value., defaults to None
    :type is_omitted: bool, optional
    :param type: type, defaults to None
    :type type: ArrayJsonSchemaPropertyOutputType, optional
    :param items: Schema for array elements., defaults to None
    :type items: ArrayJsonSchemaPropertyOutputItems, optional
    """

    description: Optional[str] = Field(default=None)
    dynamic_variable: Optional[str] = Field(
        default=None,
        description="When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.",
    )
    constant_value: Optional[List[Any]] = Field(
        default=None,
        description="When set, the entire array uses this constant value at runtime. Mutually exclusive with description (LLM-provided array), dynamic_variable, and is_omitted.",
    )
    is_omitted: Optional[bool] = Field(
        default=None,
        description="If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.",
    )
    type: Optional[ArrayJsonSchemaPropertyOutputType] = Field(default=None)
    items: Optional[ArrayJsonSchemaPropertyOutputItems] = Field(
        default=None, description="Schema for array elements."
    )


ArrayJsonSchemaPropertyOutputType = typing.Union[typing.Literal["array"], typing.Any]

# Union type for ArrayJsonSchemaPropertyOutputItems
# Pydantic will attempt to validate against each type in order
ArrayJsonSchemaPropertyOutputItems = Union[
    LiteralJsonSchemaProperty,
    "ObjectJsonSchemaPropertyOutput",
    ArrayJsonSchemaPropertyOutput,
]
# TypeAdapter for runtime validation of ArrayJsonSchemaPropertyOutputItems
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter


class _ArrayJsonSchemaPropertyOutputItemsAdapterProxy:
    _adapter = None

    def __getattr__(self, attr):
        if _ArrayJsonSchemaPropertyOutputItemsAdapterProxy._adapter is None:
            from . import ObjectJsonSchemaPropertyOutput

            _ArrayJsonSchemaPropertyOutputItemsAdapterProxy._adapter = TypeAdapter(
                ArrayJsonSchemaPropertyOutputItems
            )
        return getattr(_ArrayJsonSchemaPropertyOutputItemsAdapterProxy._adapter, attr)


ArrayJsonSchemaPropertyOutputItems_adapter = (
    _ArrayJsonSchemaPropertyOutputItemsAdapterProxy()
)


# Rebuild model to resolve forward references from submodels
try:
    ArrayJsonSchemaPropertyOutput.model_rebuild()
except NameError:
    # A member of an import cycle is only imported under TYPE_CHECKING, so some forward refs
    # cannot resolve this early. The batched model_rebuild(_types_namespace=...) in
    # models/__init__.py resolves them once every model is loaded.
    #
    # NameError, not Exception: pydantic raises PydanticUndefinedAnnotation for an unresolved
    # forward reference and that subclasses NameError, so this catches exactly the expected case
    # and leaves a genuine error (a bad field type, a missing import) loud.
    pass


# Note: This model has circular dependencies with: object_json_schema_property_output, array_json_schema_property_output
# Forward references will be resolved when model_rebuild() is called from models/__init__.py
