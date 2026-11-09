from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .literal_json_schema_property import LiteralJsonSchemaProperty


class QueryParamsJsonSchema(BaseModel):
    """QueryParamsJsonSchema

    :param properties: properties
    :type properties: Dict[str, LiteralJsonSchemaProperty]
    :param required: required, defaults to None
    :type required: List[str], optional
    """

    properties: Dict[str, LiteralJsonSchemaProperty]
    required: Optional[List[str]] = Field(default=None)
