from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class WorkspaceCreateApiKeyResponseModel(BaseModel):
    """WorkspaceCreateApiKeyResponseModel

    :param xi_api_key: xi_api_key
    :type xi_api_key: str
    :param key_id: key_id
    :type key_id: str
    """

    xi_api_key: str = Field(alias="xi-api-key", serialization_alias="xi-api-key")
    key_id: str
