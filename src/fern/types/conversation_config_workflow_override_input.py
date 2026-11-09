from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .client_event import ClientEvent
from .file_input_config_workflow_override import FileInputConfigWorkflowOverride
from .background_sound_config_workflow_override import (
    BackgroundSoundConfigWorkflowOverride,
)


class ConversationConfigWorkflowOverrideInput(BaseModel):
    """ConversationConfigWorkflowOverrideInput

    :param text_only: If enabled audio will not be processed and only text will be used, use to avoid audio pricing., defaults to None
    :type text_only: bool, optional
    :param max_duration_seconds: The maximum duration of a conversation in seconds, defaults to None
    :type max_duration_seconds: int, optional
    :param client_events: The events that will be sent to the client, defaults to None
    :type client_events: List[ClientEvent], optional
    :param file_input: Configuration for file input (image/PDF uploads) during conversations., defaults to None
    :type file_input: FileInputConfigWorkflowOverride, optional
    :param monitoring_enabled: Enable real-time monitoring of conversations via WebSocket, defaults to None
    :type monitoring_enabled: bool, optional
    :param monitoring_events: The events that will be sent to monitoring connections., defaults to None
    :type monitoring_events: List[ClientEvent], optional
    :param background_sound: Configuration for background sound during conversations., defaults to None
    :type background_sound: BackgroundSoundConfigWorkflowOverride, optional
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
    file_input: Optional[FileInputConfigWorkflowOverride] = Field(
        default=None,
        description="Configuration for file input (image/PDF uploads) during conversations.",
    )
    monitoring_enabled: Optional[bool] = Field(
        default=None,
        description="Enable real-time monitoring of conversations via WebSocket",
    )
    monitoring_events: Optional[List[ClientEvent]] = Field(
        default=None,
        description="The events that will be sent to monitoring connections.",
    )
    background_sound: Optional[BackgroundSoundConfigWorkflowOverride] = Field(
        default=None,
        description="Configuration for background sound during conversations.",
    )
    source_attribution: Optional[bool] = Field(
        default=None,
        description="When enabled and knowledge base content is present, the LLM is instructed to report which sources it used.",
    )
