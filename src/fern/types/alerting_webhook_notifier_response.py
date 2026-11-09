from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AlertingWebhookNotifierResponseType = typing.Union[
    typing.Literal["webhook"], typing.Any
]


class AlertingWebhookNotifierResponse(BaseModel):
    """AlertingWebhookNotifierResponse

    :param type: type, defaults to None
    :type type: AlertingWebhookNotifierResponseType, optional
    :param webhook_id: webhook_id
    :type webhook_id: str
    """

    type: Optional[AlertingWebhookNotifierResponseType] = Field(default=None)
    webhook_id: str
