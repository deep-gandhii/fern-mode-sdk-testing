from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class EnvironmentVariableAuthConnectionValueRequest(BaseModel):
    """EnvironmentVariableAuthConnectionValueRequest

    :param auth_connection_id: auth_connection_id
    :type auth_connection_id: str
    """

    auth_connection_id: str
