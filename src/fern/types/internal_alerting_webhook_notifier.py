from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .alerting_webhook_method import AlertingWebhookMethod
from .alerting_webhook_header import AlertingWebhookHeader

InternalAlertingWebhookNotifierType = typing.Union[
    typing.Literal["webhook"], typing.Any
]


class InternalAlertingWebhookNotifier(BaseModel):
    """InternalAlertingWebhookNotifier

    :param type: type, defaults to None
    :type type: InternalAlertingWebhookNotifierType, optional
    :param url: The URL to send alert lifecycle notifications to.
    :type url: str
    :param method: method, defaults to None
    :type method: AlertingWebhookMethod, optional
    :param headers: Custom request headers sent with every notification. Secret header values are encrypted at rest and never returned by the API., defaults to None
    :type headers: List[AlertingWebhookHeader], optional
    """

    type: Optional[InternalAlertingWebhookNotifierType] = Field(default=None)
    url: str = Field(description="The URL to send alert lifecycle notifications to.")
    method: Optional[AlertingWebhookMethod] = Field(default=None)
    headers: Optional[List[AlertingWebhookHeader]] = Field(
        default=None,
        description="Custom request headers sent with every notification. Secret header values are encrypted at rest and never returned by the API.",
    )
