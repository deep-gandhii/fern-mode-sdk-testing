from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class AlertingWebhookHeader(BaseModel):
    """AlertingWebhookHeader

    :param name: name
    :type name: str
    :param is_secret: is_secret, defaults to None
    :type is_secret: bool, optional
    :param value: Header value. May be null only for a secret header on update., defaults to None
    :type value: str, optional
    """

    name: str
    is_secret: Optional[bool] = Field(default=None)
    value: Optional[str] = Field(
        default=None,
        description="Header value. May be null only for a secret header on update.",
    )
