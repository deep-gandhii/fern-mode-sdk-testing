from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .environment_variable_response import EnvironmentVariableResponse


class EnvironmentVariablesListResponse(BaseModel):
    """EnvironmentVariablesListResponse

    :param environment_variables: environment_variables
    :type environment_variables: List[EnvironmentVariableResponse]
    :param next_cursor: next_cursor, defaults to None
    :type next_cursor: str, optional
    :param has_more: has_more
    :type has_more: bool
    """

    environment_variables: List[EnvironmentVariableResponse]
    next_cursor: Optional[str] = Field(default=None)
    has_more: bool
