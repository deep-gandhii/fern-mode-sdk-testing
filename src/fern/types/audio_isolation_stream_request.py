from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

AudioIsolationStreamRequestFileFormat = typing.Union[
    typing.Literal["pcm_s16le_16", "other"], typing.Any
]


class AudioIsolationStreamRequest(BaseModel):
    """AudioIsolationStreamRequest

    :param audio: The audio file from which vocals/speech will be isolated from.
    :type audio: bytes
    :param file_format: The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform., defaults to None
    :type file_format: AudioIsolationStreamRequestFileFormat, optional
    """

    audio: bytes = Field(
        description="The audio file from which vocals/speech will be isolated from."
    )
    file_format: Optional[AudioIsolationStreamRequestFileFormat] = Field(
        default=None,
        description="The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform.",
    )
