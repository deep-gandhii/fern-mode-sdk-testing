from __future__ import annotations
import typing
from typing import Any

WorkspaceWebhookEventType = typing.Union[
    typing.Literal["voice_library_removal_notice", "speech_to_text", "agent_qa"],
    typing.Any,
]
