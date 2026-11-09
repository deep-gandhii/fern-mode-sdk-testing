from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .workspace_webhook_response_model import WorkspaceWebhookResponseModel


class WorkspaceWebhookListResponseModel(BaseModel):
    """WorkspaceWebhookListResponseModel

    :param webhooks: List of webhooks currently configured for the workspace
    :type webhooks: List[WorkspaceWebhookResponseModel]
    """

    webhooks: List[WorkspaceWebhookResponseModel] = Field(
        description="List of webhooks currently configured for the workspace"
    )
