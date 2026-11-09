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

ColumnFilterOperation = typing.Union[
    typing.Literal["in", "not_in", "le", "ge", "lt", "gt", "eq", "neq"], typing.Any
]

# Union type for ColumnFilterValuesItem
# Pydantic will attempt to validate against each type in order
ColumnFilterValuesItem = Union[str, int, float, str, bool]
# TypeAdapter for runtime validation of ColumnFilterValuesItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ColumnFilterValuesItem_adapter = TypeAdapter(ColumnFilterValuesItem)


class ColumnFilter(BaseModel):
    """ColumnFilter

    :param column: column
    :type column: str
    :param operation: operation
    :type operation: ColumnFilterOperation
    :param values: values
    :type values: List[ColumnFilterValuesItem]
    """

    column: str
    operation: ColumnFilterOperation
    values: List[ColumnFilterValuesItem]
