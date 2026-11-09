from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .tts_conversational_model import TtsConversationalModel
from .supported_voice import SupportedVoice
from .suggested_audio_tag import SuggestedAudioTag
from .tts_output_format import TtsOutputFormat
from .tts_optimize_streaming_latency import TtsOptimizeStreamingLatency
from .text_normalisation_type import TextNormalisationType
from .pydantic_pronunciation_dictionary_version_locator import (
    PydanticPronunciationDictionaryVersionLocator,
)


class TtsConversationalConfigInput(BaseModel):
    """TtsConversationalConfigInput

    :param model_id: model_id, defaults to None
    :type model_id: TtsConversationalModel, optional
    :param voice_id: The voice ID to use for TTS, defaults to None
    :type voice_id: str, optional
    :param supported_voices: Additional supported voices for the agent, defaults to None
    :type supported_voices: List[SupportedVoice], optional
    :param expressive_mode: When enabled, applies expressive audio tags prompt. Automatically disabled for non-v3 models., defaults to None
    :type expressive_mode: bool, optional
    :param suggested_audio_tags: Suggested audio tags to boost expressive speech (for eleven_v3 and eleven_v3_conversational models). The agent can still use other tags not listed here., defaults to None
    :type suggested_audio_tags: List[SuggestedAudioTag], optional
    :param agent_output_audio_format: agent_output_audio_format, defaults to None
    :type agent_output_audio_format: TtsOutputFormat, optional
    :param optimize_streaming_latency: optimize_streaming_latency, defaults to None
    :type optimize_streaming_latency: TtsOptimizeStreamingLatency, optional
    :param stability: The stability of generated speech, defaults to None
    :type stability: float, optional
    :param speed: The speed of generated speech, defaults to None
    :type speed: float, optional
    :param similarity_boost: The similarity boost for generated speech, defaults to None
    :type similarity_boost: float, optional
    :param text_normalisation_type: Method for converting numbers to words before sending to TTS, defaults to None
    :type text_normalisation_type: TextNormalisationType, optional
    :param pronunciation_dictionary_locators: The pronunciation dictionary locators, defaults to None
    :type pronunciation_dictionary_locators: List[PydanticPronunciationDictionaryVersionLocator], optional
    :param enable_phoneme_tags: Opt-in to SSML phoneme tag handling for V3 models. When enabled, phoneme tags (inline and from pronunciation dictionaries) are parsed into inline IPA before being sent to the model., defaults to None
    :type enable_phoneme_tags: bool, optional
    """

    model_id: Optional[TtsConversationalModel] = Field(default=None)
    voice_id: Optional[str] = Field(
        default=None, description="The voice ID to use for TTS"
    )
    supported_voices: Optional[List[SupportedVoice]] = Field(
        default=None, description="Additional supported voices for the agent"
    )
    expressive_mode: Optional[bool] = Field(
        default=None,
        description="When enabled, applies expressive audio tags prompt. Automatically disabled for non-v3 models.",
    )
    suggested_audio_tags: Optional[List[SuggestedAudioTag]] = Field(
        default=None,
        description="Suggested audio tags to boost expressive speech (for eleven_v3 and eleven_v3_conversational models). The agent can still use other tags not listed here.",
    )
    agent_output_audio_format: Optional[TtsOutputFormat] = Field(default=None)
    optimize_streaming_latency: Optional[TtsOptimizeStreamingLatency] = Field(
        default=None
    )
    stability: Optional[float] = Field(
        default=None, description="The stability of generated speech"
    )
    speed: Optional[float] = Field(
        default=None, description="The speed of generated speech"
    )
    similarity_boost: Optional[float] = Field(
        default=None, description="The similarity boost for generated speech"
    )
    text_normalisation_type: Optional[TextNormalisationType] = Field(
        default=None,
        description="Method for converting numbers to words before sending to TTS",
    )
    pronunciation_dictionary_locators: Optional[
        List[PydanticPronunciationDictionaryVersionLocator]
    ] = Field(default=None, description="The pronunciation dictionary locators")
    enable_phoneme_tags: Optional[bool] = Field(
        default=None,
        description="Opt-in to SSML phoneme tag handling for V3 models. When enabled, phoneme tags (inline and from pronunciation dictionaries) are parsed into inline IPA before being sent to the model.",
    )
