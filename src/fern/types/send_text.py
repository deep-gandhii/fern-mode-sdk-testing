from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .realtime_voice_settings import RealtimeVoiceSettings
from .generation_config import GenerationConfig


class SendText(BaseModel):
    """SendText

    :param text: The text to be sent to the API for audio generation. Should always end with a single space string.
    :type text: str
    :param try_trigger_generation: This is an advanced setting that most users shouldn't need to use. It relates to our generation schedule. Use this to attempt to immediately trigger the generation of audio, overriding the `chunk_length_schedule`. Unlike flush, `try_trigger_generation` will only generate audio if our buffer contains more than a minimum threshold of characters, this is to ensure a higher quality response from our model. Note that overriding the chunk schedule to generate small amounts of text may result in lower quality audio, therefore, only use this parameter if you really need text to be processed immediately. We generally recommend keeping the default value of `false` and adjusting the `chunk_length_schedule` in the `generation_config` instead., defaults to None
    :type try_trigger_generation: bool, optional
    :param voice_settings: voice_settings, defaults to None
    :type voice_settings: RealtimeVoiceSettings, optional
    :param generator_config: generator_config, defaults to None
    :type generator_config: GenerationConfig, optional
    :param flush: Flush forces the generation of audio. Set this value to true when you have finished sending text, but want to keep the websocket connection open. This is useful when you want to ensure that the last chunk of audio is generated even when the length of text sent is smaller than the value set in chunk_length_schedule (e.g. 120 or 50)., defaults to None
    :type flush: bool, optional
    """

    text: str = Field(
        description="The text to be sent to the API for audio generation. Should always end with a single space string."
    )
    try_trigger_generation: Optional[bool] = Field(
        default=None,
        description="This is an advanced setting that most users shouldn't need to use. It relates to our generation schedule. Use this to attempt to immediately trigger the generation of audio, overriding the `chunk_length_schedule`. Unlike flush, `try_trigger_generation` will only generate audio if our buffer contains more than a minimum threshold of characters, this is to ensure a higher quality response from our model. Note that overriding the chunk schedule to generate small amounts of text may result in lower quality audio, therefore, only use this parameter if you really need text to be processed immediately. We generally recommend keeping the default value of `false` and adjusting the `chunk_length_schedule` in the `generation_config` instead.",
    )
    voice_settings: Optional[RealtimeVoiceSettings] = Field(default=None)
    generator_config: Optional[GenerationConfig] = Field(default=None)
    flush: Optional[bool] = Field(
        default=None,
        description="Flush forces the generation of audio. Set this value to true when you have finished sending text, but want to keep the websocket connection open. This is useful when you want to ensure that the last chunk of audio is generated even when the length of text sent is smaller than the value set in chunk_length_schedule (e.g. 120 or 50).",
    )
