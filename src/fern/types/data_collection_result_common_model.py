from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .literal_json_schema_property import LiteralJsonSchemaProperty


class DataCollectionResultCommonModel(BaseModel):
    """DataCollectionResultCommonModel

    :param data_collection_id: data_collection_id
    :type data_collection_id: str
    :param value: value, defaults to None
    :type value: Any, optional
    :param json_schema: json_schema, defaults to None
    :type json_schema: LiteralJsonSchemaProperty, optional
    :param rationale: rationale
    :type rationale: str
    """

    data_collection_id: str
    value: Optional[Any] = Field(default=None)
    json_schema: Optional[LiteralJsonSchemaProperty] = Field(default=None)
    rationale: str
