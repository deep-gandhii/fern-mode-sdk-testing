from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .realtime_voice_settings import RealtimeVoiceSettings
from .generation_config import GenerationConfig
from .pronunciation_dictionary_locator import PronunciationDictionaryLocator

InitializeConnectionMultiText = typing.Union[typing.Literal[" "], typing.Any]


class InitializeConnectionMulti(BaseModel):
    """Payload to initialize a new context in a multi-stream WebSocket connection.

    :param text: Must be a single space character to initiate the context.
    :type text: InitializeConnectionMultiText
    :param voice_settings: voice_settings, defaults to None
    :type voice_settings: RealtimeVoiceSettings, optional
    :param generation_config: generation_config, defaults to None
    :type generation_config: GenerationConfig, optional
    :param pronunciation_dictionary_locators: Optional pronunciation dictionaries for this context., defaults to None
    :type pronunciation_dictionary_locators: List[PronunciationDictionaryLocator], optional
    :param xi_api_key: Your ElevenLabs API key (if not in header). For this context's first message only., defaults to None
    :type xi_api_key: str, optional
    :param authorization: Your authorization bearer token (if not in header). For this context's first message only., defaults to None
    :type authorization: str, optional
    :param context_id: A unique identifier for the first context created in the websocket. If not provided, a default context will be used., defaults to None
    :type context_id: str, optional
    """

    text: InitializeConnectionMultiText = Field(
        default=" ",
        description="Must be a single space character to initiate the context.",
    )
    voice_settings: Optional[RealtimeVoiceSettings] = Field(default=None)
    generation_config: Optional[GenerationConfig] = Field(default=None)
    pronunciation_dictionary_locators: Optional[
        List[PronunciationDictionaryLocator]
    ] = Field(
        default=None,
        description="Optional pronunciation dictionaries for this context.",
    )
    xi_api_key: Optional[str] = Field(
        default=None,
        description="Your ElevenLabs API key (if not in header). For this context's first message only.",
    )
    authorization: Optional[str] = Field(
        default=None,
        description="Your authorization bearer token (if not in header). For this context's first message only.",
    )
    context_id: Optional[str] = Field(
        default=None,
        description="A unique identifier for the first context created in the websocket. If not provided, a default context will be used.",
    )
