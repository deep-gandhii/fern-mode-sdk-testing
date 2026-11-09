from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conv_ai_workspace_stored_secret_config import ConvAiWorkspaceStoredSecretConfig


class GetWorkspaceSecretsResponseModel(BaseModel):
    """GetWorkspaceSecretsResponseModel

    :param secrets: secrets
    :type secrets: List[ConvAiWorkspaceStoredSecretConfig]
    :param next_cursor: Cursor for fetching the next page of secrets, defaults to None
    :type next_cursor: str, optional
    """

    secrets: List[ConvAiWorkspaceStoredSecretConfig]
    next_cursor: Optional[str] = Field(
        default=None, description="Cursor for fetching the next page of secrets"
    )
