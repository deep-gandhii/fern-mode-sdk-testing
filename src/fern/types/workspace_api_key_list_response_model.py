from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .workspace_api_key_response_model import WorkspaceApiKeyResponseModel


class WorkspaceApiKeyListResponseModel(BaseModel):
    """WorkspaceApiKeyListResponseModel

    :param api_keys: api_keys
    :type api_keys: List[WorkspaceApiKeyResponseModel]
    """

    api_keys: List[WorkspaceApiKeyResponseModel] = Field(
        alias="api-keys", serialization_alias="api-keys"
    )
