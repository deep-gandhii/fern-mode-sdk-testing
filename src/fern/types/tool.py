from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .icon import Icon
from .tool_annotations import ToolAnnotations
from .tool_execution import ToolExecution


class Tool(BaseModel):
    """Definition for a tool the client can call.

    :param name: name
    :type name: str
    :param title: title, defaults to None
    :type title: str, optional
    :param description: description, defaults to None
    :type description: str, optional
    :param input_schema: input_schema
    :type input_schema: Dict[str, Any]
    :param output_schema: output_schema, defaults to None
    :type output_schema: Dict[str, Any], optional
    :param icons: icons, defaults to None
    :type icons: List[Icon], optional
    :param annotations: annotations, defaults to None
    :type annotations: ToolAnnotations, optional
    :param meta: meta, defaults to None
    :type meta: Dict[str, Any], optional
    :param execution: execution, defaults to None
    :type execution: ToolExecution, optional
    """

    name: str
    title: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    input_schema: Dict[str, Any] = Field(
        alias="inputSchema", serialization_alias="inputSchema"
    )
    output_schema: Optional[Dict[str, Any]] = Field(
        alias="outputSchema", serialization_alias="outputSchema", default=None
    )
    icons: Optional[List[Icon]] = Field(default=None)
    annotations: Optional[ToolAnnotations] = Field(default=None)
    meta: Optional[Dict[str, Any]] = Field(
        alias="_meta", serialization_alias="_meta", default=None
    )
    execution: Optional[ToolExecution] = Field(default=None)

    def model_dump_original(self, **kwargs):
        result = super().model_dump_original(**kwargs)
        extra_fields = self.model_extra or {}
        return {**extra_fields, **result}
