from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel

WebhookHmacSettingsAuthType = typing.Union[typing.Literal["hmac"], typing.Any]


class WebhookHmacSettings(BaseModel):
    """Settings for creating an HMAC-authenticated webhook

    :param auth_type: The authentication type for this webhook
    :type auth_type: WebhookHmacSettingsAuthType
    :param name: The display name for this webhook
    :type name: str
    :param webhook_url: The HTTPS callback URL that will be called when this webhook is triggered
    :type webhook_url: str
    :param request_headers: Optional custom request headers to include with each webhook delivery, defaults to None
    :type request_headers: Dict[str, str], optional
    """

    auth_type: WebhookHmacSettingsAuthType = Field(
        default="hmac", description="The authentication type for this webhook"
    )
    name: str = Field(description="The display name for this webhook")
    webhook_url: str = Field(
        description="The HTTPS callback URL that will be called when this webhook is triggered"
    )
    request_headers: Optional[Dict[str, str]] = Field(
        default=None,
        description="Optional custom request headers to include with each webhook delivery",
    )
