from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .realtime_voice_settings import RealtimeVoiceSettings
from .generation_config import GenerationConfig
from .pronunciation_dictionary_locator import PronunciationDictionaryLocator


class InitialiseContext(BaseModel):
    """Payload to initialize or re-initialize a TTS context with specific settings and initial text for multi-stream connections.

    :param text: The initial text to synthesize. Should end with a single space.
    :type text: str
    :param voice_settings: voice_settings, defaults to None
    :type voice_settings: RealtimeVoiceSettings, optional
    :param generation_config: generation_config, defaults to None
    :type generation_config: GenerationConfig, optional
    :param pronunciation_dictionary_locators: Optional list of pronunciation dictionary locators to be used for this context., defaults to None
    :type pronunciation_dictionary_locators: List[PronunciationDictionaryLocator], optional
    :param xi_api_key: Your ElevenLabs API key. Required if not provided in the WebSocket connection's header or query parameters. This applies to the (re)initialization of this specific context., defaults to None
    :type xi_api_key: str, optional
    :param authorization: Your authorization bearer token. Required if not provided in the WebSocket connection's header or query parameters. This applies to the (re)initialization of this specific context., defaults to None
    :type authorization: str, optional
    :param context_id: An identifier for the text-to-speech context. If omitted, a default context ID may be assigned by the server. If provided, this message will create a new context with this ID or re-initialize an existing one with the new settings and text., defaults to None
    :type context_id: str, optional
    """

    text: str = Field(
        description="The initial text to synthesize. Should end with a single space."
    )
    voice_settings: Optional[RealtimeVoiceSettings] = Field(default=None)
    generation_config: Optional[GenerationConfig] = Field(default=None)
    pronunciation_dictionary_locators: Optional[
        List[PronunciationDictionaryLocator]
    ] = Field(
        default=None,
        description="Optional list of pronunciation dictionary locators to be used for this context.",
    )
    xi_api_key: Optional[str] = Field(
        default=None,
        description="Your ElevenLabs API key. Required if not provided in the WebSocket connection's header or query parameters. This applies to the (re)initialization of this specific context.",
    )
    authorization: Optional[str] = Field(
        default=None,
        description="Your authorization bearer token. Required if not provided in the WebSocket connection's header or query parameters. This applies to the (re)initialization of this specific context.",
    )
    context_id: Optional[str] = Field(
        default=None,
        description="An identifier for the text-to-speech context. If omitted, a default context ID may be assigned by the server. If provided, this message will create a new context with this ID or re-initialize an existing one with the new settings and text.",
    )
