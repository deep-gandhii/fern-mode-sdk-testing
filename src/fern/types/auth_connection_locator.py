from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AuthConnectionLocator(BaseModel):
    """Used to reference an auth connection from the workspace's auth connection store.

    :param auth_connection_id: auth_connection_id
    :type auth_connection_id: str
    """

    auth_connection_id: str
