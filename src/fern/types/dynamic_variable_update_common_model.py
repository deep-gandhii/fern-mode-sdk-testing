from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class DynamicVariableUpdateCommonModel(BaseModel):
    """Tracks a dynamic variable update that occurred during tool execution.

    :param variable_name: variable_name
    :type variable_name: str
    :param old_value: old_value
    :type old_value: str
    :param new_value: new_value
    :type new_value: str
    :param updated_at: updated_at
    :type updated_at: float
    :param tool_name: tool_name
    :type tool_name: str
    :param tool_request_id: tool_request_id
    :type tool_request_id: str
    """

    variable_name: str
    old_value: Optional[str]
    new_value: str
    updated_at: float
    tool_name: str
    tool_request_id: str
