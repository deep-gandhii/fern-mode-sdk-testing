from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .webhook_usage_type import WebhookUsageType


class WorkspaceWebhookUsageResponseModel(BaseModel):
    """WorkspaceWebhookUsageResponseModel

    :param usage_type: usage_type
    :type usage_type: WebhookUsageType
    """

    usage_type: WebhookUsageType
