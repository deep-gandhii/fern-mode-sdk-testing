from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .workspace_service_account_response_model import (
    WorkspaceServiceAccountResponseModel,
)


class WorkspaceServiceAccountListResponseModel(BaseModel):
    """WorkspaceServiceAccountListResponseModel

    :param service_accounts: service_accounts
    :type service_accounts: List[WorkspaceServiceAccountResponseModel]
    """

    service_accounts: List[WorkspaceServiceAccountResponseModel] = Field(
        alias="service-accounts", serialization_alias="service-accounts"
    )
