from __future__ import annotations
import typing
from typing import Any

WebhookAuthMethodType = typing.Union[
    typing.Literal["hmac", "oauth2", "mtls"], typing.Any
]
