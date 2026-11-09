from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .alerting_monitor_config import AlertingMonitorConfig
from .alerting_webhook_notifier_response import AlertingWebhookNotifierResponse


class AlertingSettingsResponse(BaseModel):
    """Customer-facing view of alerting settings. Unlike AdminAlertingSettingsResponse, it has no internal_notifiers field: those are ElevenLabs-internal delivery channels whose URLs must never be returned outside the admin API.

    :param monitor_configs: monitor_configs, defaults to None
    :type monitor_configs: Dict[str, AlertingMonitorConfig], optional
    :param auto_resolve_after_inactive_minutes: auto_resolve_after_inactive_minutes, defaults to None
    :type auto_resolve_after_inactive_minutes: int, optional
    :param notifiers: notifiers, defaults to None
    :type notifiers: List[AlertingWebhookNotifierResponse], optional
    """

    monitor_configs: Optional[Dict[str, AlertingMonitorConfig]] = Field(default=None)
    auto_resolve_after_inactive_minutes: Optional[int] = Field(default=None)
    notifiers: Optional[List[AlertingWebhookNotifierResponse]] = Field(default=None)
