from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

VoicemailDetectionToolConfigSystemToolType = typing.Union[
    typing.Literal["voicemail_detection"], typing.Any
]


class VoicemailDetectionToolConfig(BaseModel):
    """Allows the agent to detect when a voicemail system is encountered. This tool should be invoked by the LLM when it detects that the call has been answered by a voicemail system rather than a human. If a voicemail message is configured, it will be played; otherwise the call will end immediately.

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: VoicemailDetectionToolConfigSystemToolType, optional
    :param voicemail_message: Optional message to leave on voicemail when detected. If not provided, the call will end immediately when voicemail is detected. Supports dynamic variables (e.g., {{system__time}}, {{system__call_duration_secs}}, {{custom_variable}})., defaults to None
    :type voicemail_message: str, optional
    """

    system_tool_type: Optional[VoicemailDetectionToolConfigSystemToolType] = Field(
        default=None
    )
    voicemail_message: Optional[str] = Field(
        default=None,
        description="Optional message to leave on voicemail when detected. If not provided, the call will end immediately when voicemail is detected. Supports dynamic variables (e.g., {{system__time}}, {{system__call_duration_secs}}, {{custom_variable}}).",
    )
