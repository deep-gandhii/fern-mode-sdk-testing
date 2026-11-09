from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .webhook_hmac_settings import WebhookHmacSettings


class BodyCreateWorkspaceWebhookV1WorkspaceWebhooksPost(BaseModel):
    """BodyCreateWorkspaceWebhookV1WorkspaceWebhooksPost

    :param settings: Settings for creating an HMAC-authenticated webhook
    :type settings: WebhookHmacSettings
    """

    settings: WebhookHmacSettings = Field(
        description="Settings for creating an HMAC-authenticated webhook"
    )
