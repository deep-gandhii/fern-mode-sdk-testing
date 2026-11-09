from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .system_tool_config_output import SystemToolConfigOutput


class BuiltInToolsWorkflowOverrideOutput(BaseModel):
    """BuiltInToolsWorkflowOverrideOutput

    :param end_call: The end call tool, defaults to None
    :type end_call: SystemToolConfigOutput, optional
    :param language_detection: The language detection tool, defaults to None
    :type language_detection: SystemToolConfigOutput, optional
    :param transfer_to_agent: The transfer to agent tool, defaults to None
    :type transfer_to_agent: SystemToolConfigOutput, optional
    :param transfer_to_number: The transfer to number tool, defaults to None
    :type transfer_to_number: SystemToolConfigOutput, optional
    :param skip_turn: The skip turn tool, defaults to None
    :type skip_turn: SystemToolConfigOutput, optional
    :param play_keypad_touch_tone: The play DTMF tool, defaults to None
    :type play_keypad_touch_tone: SystemToolConfigOutput, optional
    :param voicemail_detection: The voicemail detection tool, defaults to None
    :type voicemail_detection: SystemToolConfigOutput, optional
    """

    end_call: Optional[SystemToolConfigOutput] = Field(
        default=None, description="The end call tool"
    )
    language_detection: Optional[SystemToolConfigOutput] = Field(
        default=None, description="The language detection tool"
    )
    transfer_to_agent: Optional[SystemToolConfigOutput] = Field(
        default=None, description="The transfer to agent tool"
    )
    transfer_to_number: Optional[SystemToolConfigOutput] = Field(
        default=None, description="The transfer to number tool"
    )
    skip_turn: Optional[SystemToolConfigOutput] = Field(
        default=None, description="The skip turn tool"
    )
    play_keypad_touch_tone: Optional[SystemToolConfigOutput] = Field(
        default=None, description="The play DTMF tool"
    )
    voicemail_detection: Optional[SystemToolConfigOutput] = Field(
        default=None, description="The voicemail detection tool"
    )
