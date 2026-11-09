from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .alerting_monitor_config import AlertingMonitorConfig
from .alerting_webhook_notifier import AlertingWebhookNotifier


class AlertingSettings(BaseModel):
    """Alerting configuration used at both per-agent and per-workspace level. All fields are optional overrides; the cascade resolver fills in defaults when they are unset. Notifiers stack and dedupe (by webhook_id) across the workspace and agent layers rather than overriding each other. Cascade order for per-monitor threshold and auto-resolve: agent → workspace → system default.

    :param monitor_configs: Alerting configuration keyed by monitor name., defaults to None
    :type monitor_configs: Dict[str, AlertingMonitorConfig], optional
    :param auto_resolve_after_inactive_minutes: How many minutes an alert can stay inactive before it is auto-resolved. Unset values fall through to the next layer., defaults to None
    :type auto_resolve_after_inactive_minutes: int, optional
    :param notifiers: Delivery channels for alert lifecycle notifications. Stacked and deduped by webhook_id with other layers., defaults to None
    :type notifiers: List[AlertingWebhookNotifier], optional
    """

    monitor_configs: Optional[Dict[str, AlertingMonitorConfig]] = Field(
        default=None, description="Alerting configuration keyed by monitor name."
    )
    auto_resolve_after_inactive_minutes: Optional[int] = Field(
        default=None,
        description="How many minutes an alert can stay inactive before it is auto-resolved. Unset values fall through to the next layer.",
    )
    notifiers: Optional[List[AlertingWebhookNotifier]] = Field(
        default=None,
        description="Delivery channels for alert lifecycle notifications. Stacked and deduped by webhook_id with other layers.",
    )
