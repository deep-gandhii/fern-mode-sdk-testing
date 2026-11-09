from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PlayDtmfToolConfigSystemToolType = typing.Union[
    typing.Literal["play_keypad_touch_tone"], typing.Any
]


class PlayDtmfToolConfig(BaseModel):
    """Allows the agent to play DTMF tones during a phone call. This tool can be used to interact with automated phone systems, such as navigating phone menus, entering extensions, or inputting numeric codes.

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: PlayDtmfToolConfigSystemToolType, optional
    :param use_out_of_band_dtmf: Send DTMF tones as out-of-band RTP events (RFC 4733) instead of in-band audio. Only effective for SIP trunk imported numbers., defaults to None
    :type use_out_of_band_dtmf: bool, optional
    :param suppress_turn_after_dtmf: If true, the agent will not generate further speech after playing DTMF tones. This prevents the agent's speech from interfering with IVR systems., defaults to None
    :type suppress_turn_after_dtmf: bool, optional
    """

    system_tool_type: Optional[PlayDtmfToolConfigSystemToolType] = Field(default=None)
    use_out_of_band_dtmf: Optional[bool] = Field(
        default=None,
        description="Send DTMF tones as out-of-band RTP events (RFC 4733) instead of in-band audio. Only effective for SIP trunk imported numbers.",
    )
    suppress_turn_after_dtmf: Optional[bool] = Field(
        default=None,
        description="If true, the agent will not generate further speech after playing DTMF tones. This prevents the agent's speech from interfering with IVR systems.",
    )
