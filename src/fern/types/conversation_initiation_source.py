from __future__ import annotations
import typing
from typing import Any

ConversationInitiationSource = typing.Union[
    typing.Literal[
        "unknown",
        "android_sdk",
        "node_js_sdk",
        "react_native_sdk",
        "react_sdk",
        "js_sdk",
        "python_sdk",
        "widget",
        "sip_trunk",
        "twilio",
        "exotel",
        "genesys",
        "swift_sdk",
        "whatsapp",
        "twilio_sms",
        "flutter_sdk",
        "zendesk_integration",
        "slack_integration",
        "telegram_integration",
        "intercom_integration",
        "freshdesk_integration",
        "salesforce_integration",
        "template_preview",
        "genesys_bot_connector",
        "subagent_tool",
    ],
    typing.Any,
]
