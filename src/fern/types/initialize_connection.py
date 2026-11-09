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

InitializeConnectionText = typing.Union[typing.Literal[" "], typing.Any]


class InitializeConnection(BaseModel):
    """InitializeConnection

    :param text: The initial text that must be sent is a blank space.
    :type text: InitializeConnectionText
    :param voice_settings: voice_settings, defaults to None
    :type voice_settings: RealtimeVoiceSettings, optional
    :param generation_config: generation_config, defaults to None
    :type generation_config: GenerationConfig, optional
    :param pronunciation_dictionary_locators: Optional list of pronunciation dictionary locators. If provided, these dictionaries will be used to modify pronunciation of matching text. Must only be provided in the first message. Note: Pronunciation dictionary matches will only be respected within a provided chunk., defaults to None
    :type pronunciation_dictionary_locators: List[PronunciationDictionaryLocator], optional
    :param xi_api_key: Your ElevenLabs API key. This can only be included in the first message and is not needed if present in the header., defaults to None
    :type xi_api_key: str, optional
    :param authorization: Your authorization bearer token. This can only be included in the first message and is not needed if present in the header., defaults to None
    :type authorization: str, optional
    """

    text: InitializeConnectionText = Field(
        default=" ", description="The initial text that must be sent is a blank space."
    )
    voice_settings: Optional[RealtimeVoiceSettings] = Field(default=None)
    generation_config: Optional[GenerationConfig] = Field(default=None)
    pronunciation_dictionary_locators: Optional[
        List[PronunciationDictionaryLocator]
    ] = Field(
        default=None,
        description="Optional list of pronunciation dictionary locators. If provided, these dictionaries will be used to modify pronunciation of matching text. Must only be provided in the first message. Note: Pronunciation dictionary matches will only be respected within a provided chunk.",
    )
    xi_api_key: Optional[str] = Field(
        alias="xi-api-key",
        serialization_alias="xi-api-key",
        default=None,
        description="Your ElevenLabs API key. This can only be included in the first message and is not needed if present in the header.",
    )
    authorization: Optional[str] = Field(
        default=None,
        description="Your authorization bearer token. This can only be included in the first message and is not needed if present in the header.",
    )
