from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .workspace_webhook_event_type import WorkspaceWebhookEventType


class BodyUpdateWorkspaceWebhookV1WorkspaceWebhooksWebhookIdPatch(BaseModel):
    """BodyUpdateWorkspaceWebhookV1WorkspaceWebhooksWebhookIdPatch

    :param is_disabled: Whether to disable or enable the webhook
    :type is_disabled: bool
    :param name: The display name of the webhook (used for display purposes only).
    :type name: str
    :param retry_enabled: Whether to enable automatic retries for transient failures (5xx, 429, timeout), defaults to None
    :type retry_enabled: bool, optional
    :param request_headers: A list of request headers to include with the webhook delivery (optional), defaults to None
    :type request_headers: Dict[str, str], optional
    :param events: The complete set of workspace-level events this webhook should be subscribed to. The webhook is added to the events in the list and removed from any not in the list. Omit to leave the current event subscriptions unchanged., defaults to None
    :type events: List[WorkspaceWebhookEventType], optional
    """

    is_disabled: bool = Field(description="Whether to disable or enable the webhook")
    name: str = Field(
        description="The display name of the webhook (used for display purposes only)."
    )
    retry_enabled: Optional[bool] = Field(
        default=None,
        description="Whether to enable automatic retries for transient failures (5xx, 429, timeout)",
    )
    request_headers: Optional[Dict[str, str]] = Field(
        default=None,
        description="A list of request headers to include with the webhook delivery (optional)",
    )
    events: Optional[List[WorkspaceWebhookEventType]] = Field(
        default=None,
        description="The complete set of workspace-level events this webhook should be subscribed to. The webhook is added to the events in the list and removed from any not in the list. Omit to leave the current event subscriptions unchanged.",
    )
