from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .client_event import ClientEvent
from .file_input_config import FileInputConfig
from .background_sound_config import BackgroundSoundConfig


class ConversationConfigInput(BaseModel):
    """ConversationConfigInput

    :param text_only: If enabled audio will not be processed and only text will be used, use to avoid audio pricing., defaults to None
    :type text_only: bool, optional
    :param max_duration_seconds: The maximum duration of a conversation in seconds, defaults to None
    :type max_duration_seconds: int, optional
    :param client_events: The events that will be sent to the client, defaults to None
    :type client_events: List[ClientEvent], optional
    :param file_input: file_input, defaults to None
    :type file_input: FileInputConfig, optional
    :param monitoring_enabled: Enable real-time monitoring of conversations via WebSocket, defaults to None
    :type monitoring_enabled: bool, optional
    :param monitoring_events: The events that will be sent to monitoring connections., defaults to None
    :type monitoring_events: List[ClientEvent], optional
    :param background_sound: background_sound, defaults to None
    :type background_sound: BackgroundSoundConfig, optional
    :param source_attribution: When enabled and knowledge base content is present, the LLM is instructed to report which sources it used., defaults to None
    :type source_attribution: bool, optional
    """

    text_only: Optional[bool] = Field(
        default=None,
        description="If enabled audio will not be processed and only text will be used, use to avoid audio pricing.",
    )
    max_duration_seconds: Optional[int] = Field(
        default=None, description="The maximum duration of a conversation in seconds"
    )
    client_events: Optional[List[ClientEvent]] = Field(
        default=None, description="The events that will be sent to the client"
    )
    file_input: Optional[FileInputConfig] = Field(default=None)
    monitoring_enabled: Optional[bool] = Field(
        default=None,
        description="Enable real-time monitoring of conversations via WebSocket",
    )
    monitoring_events: Optional[List[ClientEvent]] = Field(
        default=None,
        description="The events that will be sent to monitoring connections.",
    )
    background_sound: Optional[BackgroundSoundConfig] = Field(default=None)
    source_attribution: Optional[bool] = Field(
        default=None,
        description="When enabled and knowledge base content is present, the LLM is instructed to report which sources it used.",
    )
