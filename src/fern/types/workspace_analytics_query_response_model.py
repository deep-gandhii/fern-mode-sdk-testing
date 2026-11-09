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
from .column_unit import ColumnUnit

WorkspaceAnalyticsQueryResponseModelColumnTypesItem = typing.Union[
    typing.Literal[
        "String", "Float", "DateTime", "Int", "Bool", "JSON", "Map", "Array"
    ],
    typing.Any,
]

# Union type for WorkspaceAnalyticsQueryResponseModelRowsItemItem
# Pydantic will attempt to validate against each type in order
WorkspaceAnalyticsQueryResponseModelRowsItemItem = Union[str, int, float, bool, str]
# TypeAdapter for runtime validation of WorkspaceAnalyticsQueryResponseModelRowsItemItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkspaceAnalyticsQueryResponseModelRowsItemItem_adapter = TypeAdapter(
    WorkspaceAnalyticsQueryResponseModelRowsItemItem
)


class WorkspaceAnalyticsQueryResponseModel(BaseModel):
    """WorkspaceAnalyticsQueryResponseModel

    :param columns: columns
    :type columns: List[str]
    :param column_types: column_types
    :type column_types: List[WorkspaceAnalyticsQueryResponseModelColumnTypesItem]
    :param rows: rows
    :type rows: List[List[WorkspaceAnalyticsQueryResponseModelRowsItemItem]]
    :param column_units: column_units
    :type column_units: List[ColumnUnit]
    """

    columns: List[str]
    column_types: List[WorkspaceAnalyticsQueryResponseModelColumnTypesItem]
    rows: List[List[WorkspaceAnalyticsQueryResponseModelRowsItemItem]]
    column_units: List[ColumnUnit]
