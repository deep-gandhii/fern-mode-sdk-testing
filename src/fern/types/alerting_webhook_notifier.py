from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AlertingWebhookNotifierType = typing.Union[typing.Literal["webhook"], typing.Any]


class AlertingWebhookNotifier(BaseModel):
    """AlertingWebhookNotifier

    :param type: type, defaults to None
    :type type: AlertingWebhookNotifierType, optional
    :param webhook_id: ID of the workspace webhook to deliver alert lifecycle notifications to.
    :type webhook_id: str
    """

    type: Optional[AlertingWebhookNotifierType] = Field(default=None)
    webhook_id: str = Field(
        description="ID of the workspace webhook to deliver alert lifecycle notifications to."
    )
