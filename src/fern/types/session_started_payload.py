from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .audio_format_enum import AudioFormatEnum

SessionStartedPayloadMessageType = typing.Union[
    typing.Literal["session_started"], typing.Any
]

SessionStartedPayloadConfigCommitStrategy = typing.Union[
    typing.Literal["manual", "vad"], typing.Any
]


class SessionStartedPayloadConfig(BaseModel):
    """Configuration for the transcription session.

    :param sample_rate: Sample rate of the audio in Hz., defaults to None
    :type sample_rate: int, optional
    :param audio_format: Audio encoding format for speech-to-text., defaults to None
    :type audio_format: AudioFormatEnum, optional
    :param language_code: Language code in ISO 639-1 or ISO 639-3 format., defaults to None
    :type language_code: str, optional
    :param commit_strategy: Strategy for committing transcriptions., defaults to None
    :type commit_strategy: SessionStartedPayloadConfigCommitStrategy, optional
    :param vad_silence_threshold_secs: Silence threshold in seconds., defaults to None
    :type vad_silence_threshold_secs: float, optional
    :param vad_threshold: Threshold for voice activity detection., defaults to None
    :type vad_threshold: float, optional
    :param min_speech_duration_ms: Minimum speech duration in milliseconds., defaults to None
    :type min_speech_duration_ms: int, optional
    :param min_silence_duration_ms: Minimum silence duration in milliseconds., defaults to None
    :type min_silence_duration_ms: int, optional
    :param model_id: ID of the model to use for transcription., defaults to None
    :type model_id: str, optional
    :param enable_logging: When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request. Zero retention mode may only be used by enterprise customers., defaults to None
    :type enable_logging: bool, optional
    :param include_timestamps: Whether the session will include word-level timestamps in the committed transcript., defaults to None
    :type include_timestamps: bool, optional
    :param include_language_detection: Whether the session will include language detection in the committed transcript., defaults to None
    :type include_language_detection: bool, optional
    :param keyterms: List of keyterms the model is biased towards., defaults to None
    :type keyterms: List[str], optional
    :param no_verbatim: Whether filler words and disfluencies are removed from the transcript., defaults to None
    :type no_verbatim: bool, optional
    """

    sample_rate: Optional[int] = Field(
        default=None, description="Sample rate of the audio in Hz."
    )
    audio_format: Optional[AudioFormatEnum] = Field(
        default=None, description="Audio encoding format for speech-to-text."
    )
    language_code: Optional[str] = Field(
        default=None, description="Language code in ISO 639-1 or ISO 639-3 format."
    )
    commit_strategy: Optional[SessionStartedPayloadConfigCommitStrategy] = Field(
        default=None, description="Strategy for committing transcriptions."
    )
    vad_silence_threshold_secs: Optional[float] = Field(
        default=None, description="Silence threshold in seconds."
    )
    vad_threshold: Optional[float] = Field(
        default=None, description="Threshold for voice activity detection."
    )
    min_speech_duration_ms: Optional[int] = Field(
        default=None, description="Minimum speech duration in milliseconds."
    )
    min_silence_duration_ms: Optional[int] = Field(
        default=None, description="Minimum silence duration in milliseconds."
    )
    model_id: Optional[str] = Field(
        default=None, description="ID of the model to use for transcription."
    )
    enable_logging: Optional[bool] = Field(
        default=None,
        description="When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request. Zero retention mode may only be used by enterprise customers.",
    )
    include_timestamps: Optional[bool] = Field(
        default=None,
        description="Whether the session will include word-level timestamps in the committed transcript.",
    )
    include_language_detection: Optional[bool] = Field(
        default=None,
        description="Whether the session will include language detection in the committed transcript.",
    )
    keyterms: Optional[List[str]] = Field(
        default=None, description="List of keyterms the model is biased towards."
    )
    no_verbatim: Optional[bool] = Field(
        default=None,
        description="Whether filler words and disfluencies are removed from the transcript.",
    )


class SessionStartedPayload(BaseModel):
    """Payload sent when the transcription session is successfully started.

    :param message_type: The message type identifier.
    :type message_type: SessionStartedPayloadMessageType
    :param session_id: Unique identifier for the session.
    :type session_id: str
    :param config: Configuration for the transcription session.
    :type config: SessionStartedPayloadConfig
    """

    message_type: SessionStartedPayloadMessageType = Field(
        default="session_started", description="The message type identifier."
    )
    session_id: str = Field(description="Unique identifier for the session.")
    config: SessionStartedPayloadConfig = Field(
        description="Configuration for the transcription session."
    )
