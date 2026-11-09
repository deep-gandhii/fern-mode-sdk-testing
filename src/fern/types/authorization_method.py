from __future__ import annotations
import typing
from typing import Any

AuthorizationMethod = typing.Union[
    typing.Literal[
        "invalid",
        "public",
        "authorization_header",
        "signed_url",
        "shareable_link",
        "livekit_token",
        "livekit_token_website",
        "genesys_api_key",
        "whatsapp",
        "sms",
    ],
    typing.Any,
]
