from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .speaker_separation_response_model import SpeakerSeparationResponseModel


class VoiceSample(BaseModel):
    """VoiceSample

    :param sample_id: The ID of the sample., defaults to None
    :type sample_id: str, optional
    :param file_name: The name of the sample file., defaults to None
    :type file_name: str, optional
    :param mime_type: The MIME type of the sample file., defaults to None
    :type mime_type: str, optional
    :param size_bytes: The size of the sample file in bytes., defaults to None
    :type size_bytes: int, optional
    :param hash: The hash of the sample file., defaults to None
    :type hash: str, optional
    :param duration_secs: duration_secs, defaults to None
    :type duration_secs: float, optional
    :param remove_background_noise: remove_background_noise, defaults to None
    :type remove_background_noise: bool, optional
    :param has_isolated_audio: has_isolated_audio, defaults to None
    :type has_isolated_audio: bool, optional
    :param has_isolated_audio_preview: has_isolated_audio_preview, defaults to None
    :type has_isolated_audio_preview: bool, optional
    :param speaker_separation: speaker_separation, defaults to None
    :type speaker_separation: SpeakerSeparationResponseModel, optional
    :param trim_start: trim_start, defaults to None
    :type trim_start: int, optional
    :param trim_end: trim_end, defaults to None
    :type trim_end: int, optional
    """

    sample_id: Optional[str] = Field(default=None, description="The ID of the sample.")
    file_name: Optional[str] = Field(
        default=None, description="The name of the sample file."
    )
    mime_type: Optional[str] = Field(
        default=None, description="The MIME type of the sample file."
    )
    size_bytes: Optional[int] = Field(
        default=None, description="The size of the sample file in bytes."
    )
    hash: Optional[str] = Field(
        default=None, description="The hash of the sample file."
    )
    duration_secs: Optional[float] = Field(default=None)
    remove_background_noise: Optional[bool] = Field(default=None)
    has_isolated_audio: Optional[bool] = Field(default=None)
    has_isolated_audio_preview: Optional[bool] = Field(default=None)
    speaker_separation: Optional[SpeakerSeparationResponseModel] = Field(default=None)
    trim_start: Optional[int] = Field(default=None)
    trim_end: Optional[int] = Field(default=None)
