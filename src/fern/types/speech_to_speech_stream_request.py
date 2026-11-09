from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

SpeechToSpeechStreamRequestFileFormat = typing.Union[
    typing.Literal["pcm_s16le_16", "other"], typing.Any
]


class SpeechToSpeechStreamRequest(BaseModel):
    """SpeechToSpeechStreamRequest

    :param audio: The audio file which holds the content and emotion that will control the generated speech.
    :type audio: bytes
    :param model_id: Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for speech to speech, you can check this using the can_do_voice_conversion property., defaults to None
    :type model_id: str, optional
    :param voice_settings: Voice settings overriding stored settings for the given voice. They are applied only on the given request. Needs to be send as a JSON encoded string., defaults to None
    :type voice_settings: str, optional
    :param seed: If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295., defaults to None
    :type seed: int, optional
    :param remove_background_noise: If set, will remove the background noise from your audio input using our audio isolation model. Only applies to Voice Changer., defaults to None
    :type remove_background_noise: bool, optional
    :param file_format: The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform., defaults to None
    :type file_format: SpeechToSpeechStreamRequestFileFormat, optional
    """

    audio: bytes = Field(
        description="The audio file which holds the content and emotion that will control the generated speech."
    )
    model_id: Optional[str] = Field(
        default=None,
        description="Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for speech to speech, you can check this using the can_do_voice_conversion property.",
    )
    voice_settings: Optional[str] = Field(
        default=None,
        description="Voice settings overriding stored settings for the given voice. They are applied only on the given request. Needs to be send as a JSON encoded string.",
    )
    seed: Optional[int] = Field(
        default=None,
        description="If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.",
    )
    remove_background_noise: Optional[bool] = Field(
        default=None,
        description="If set, will remove the background noise from your audio input using our audio isolation model. Only applies to Voice Changer.",
    )
    file_format: Optional[SpeechToSpeechStreamRequestFileFormat] = Field(
        default=None,
        description="The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform.",
    )
