from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .object_json_schema_property_output import ObjectJsonSchemaPropertyOutput


class SubAgentOutput(BaseModel):
    """SubAgentOutput

    :param agent_id: agent_id
    :type agent_id: str
    :param branch_id: branch_id, defaults to None
    :type branch_id: str, optional
    :param description: description
    :type description: str
    :param parameters: parameters, defaults to None
    :type parameters: ObjectJsonSchemaPropertyOutput, optional
    """

    agent_id: str
    branch_id: Optional[str] = Field(default=None)
    description: str
    parameters: Optional[ObjectJsonSchemaPropertyOutput] = Field(default=None)
