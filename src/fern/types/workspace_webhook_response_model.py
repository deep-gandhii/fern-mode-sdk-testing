from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .webhook_auth_method_type import WebhookAuthMethodType
from .workspace_webhook_usage_response_model import WorkspaceWebhookUsageResponseModel
from .workspace_webhook_event_type import WorkspaceWebhookEventType


class WorkspaceWebhookResponseModel(BaseModel):
    """WorkspaceWebhookResponseModel

    :param name: The display name for this webhook.
    :type name: str
    :param webhook_id: The unique ID for this webhook.
    :type webhook_id: str
    :param webhook_url: The HTTPS callback URL that is called when this webhook is triggered in the platform.
    :type webhook_url: str
    :param is_disabled: Whether the webhook has been manually disabled by a user.
    :type is_disabled: bool
    :param is_auto_disabled: Whether the webhook has been automatically disabled due to repeated consecutive failures over a long period of time.
    :type is_auto_disabled: bool
    :param created_at_unix: Original creation time of the webhook.
    :type created_at_unix: int
    :param auth_type: auth_type
    :type auth_type: WebhookAuthMethodType
    :param usage: The list of products that are currently configured to trigger this webhook., defaults to None
    :type usage: List[WorkspaceWebhookUsageResponseModel], optional
    :param events: The workspace-level events this webhook is currently subscribed to. Only populated when usages are requested., defaults to None
    :type events: List[WorkspaceWebhookEventType], optional
    :param most_recent_failure_error_code: The most recent error code returned from the callback URL., defaults to None
    :type most_recent_failure_error_code: int, optional
    :param most_recent_failure_timestamp: The most recent time the webhook failed, failures are any non-200 codes returned by the callback URL., defaults to None
    :type most_recent_failure_timestamp: int, optional
    """

    name: str = Field(description="The display name for this webhook.")
    webhook_id: str = Field(description="The unique ID for this webhook.")
    webhook_url: str = Field(
        description="The HTTPS callback URL that is called when this webhook is triggered in the platform."
    )
    is_disabled: bool = Field(
        description="Whether the webhook has been manually disabled by a user."
    )
    is_auto_disabled: bool = Field(
        description="Whether the webhook has been automatically disabled due to repeated consecutive failures over a long period of time."
    )
    created_at_unix: int = Field(description="Original creation time of the webhook.")
    auth_type: WebhookAuthMethodType
    usage: Optional[List[WorkspaceWebhookUsageResponseModel]] = Field(
        default=None,
        description="The list of products that are currently configured to trigger this webhook.",
    )
    events: Optional[List[WorkspaceWebhookEventType]] = Field(
        default=None,
        description="The workspace-level events this webhook is currently subscribed to. Only populated when usages are requested.",
    )
    most_recent_failure_error_code: Optional[int] = Field(
        default=None,
        description="The most recent error code returned from the callback URL.",
    )
    most_recent_failure_timestamp: Optional[int] = Field(
        default=None,
        description="The most recent time the webhook failed, failures are any non-200 codes returned by the callback URL.",
    )
