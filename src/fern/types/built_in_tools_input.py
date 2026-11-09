from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .system_tool_config_input import SystemToolConfigInput


class BuiltInToolsInput(BaseModel):
    """BuiltInToolsInput

    :param end_call: The end call tool, defaults to None
    :type end_call: SystemToolConfigInput, optional
    :param language_detection: The language detection tool, defaults to None
    :type language_detection: SystemToolConfigInput, optional
    :param transfer_to_agent: The transfer to agent tool, defaults to None
    :type transfer_to_agent: SystemToolConfigInput, optional
    :param transfer_to_number: The transfer to number tool, defaults to None
    :type transfer_to_number: SystemToolConfigInput, optional
    :param skip_turn: The skip turn tool, defaults to None
    :type skip_turn: SystemToolConfigInput, optional
    :param play_keypad_touch_tone: The play DTMF tool, defaults to None
    :type play_keypad_touch_tone: SystemToolConfigInput, optional
    :param voicemail_detection: The voicemail detection tool, defaults to None
    :type voicemail_detection: SystemToolConfigInput, optional
    """

    end_call: Optional[SystemToolConfigInput] = Field(
        default=None, description="The end call tool"
    )
    language_detection: Optional[SystemToolConfigInput] = Field(
        default=None, description="The language detection tool"
    )
    transfer_to_agent: Optional[SystemToolConfigInput] = Field(
        default=None, description="The transfer to agent tool"
    )
    transfer_to_number: Optional[SystemToolConfigInput] = Field(
        default=None, description="The transfer to number tool"
    )
    skip_turn: Optional[SystemToolConfigInput] = Field(
        default=None, description="The skip turn tool"
    )
    play_keypad_touch_tone: Optional[SystemToolConfigInput] = Field(
        default=None, description="The play DTMF tool"
    )
    voicemail_detection: Optional[SystemToolConfigInput] = Field(
        default=None, description="The voicemail detection tool"
    )
