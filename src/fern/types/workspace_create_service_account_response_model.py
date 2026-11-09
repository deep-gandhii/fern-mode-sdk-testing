from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class WorkspaceCreateServiceAccountResponseModel(BaseModel):
    """WorkspaceCreateServiceAccountResponseModel

    :param service_account_user_id: service_account_user_id
    :type service_account_user_id: str
    """

    service_account_user_id: str = Field(
        alias="service-account-user-id", serialization_alias="service-account-user-id"
    )
