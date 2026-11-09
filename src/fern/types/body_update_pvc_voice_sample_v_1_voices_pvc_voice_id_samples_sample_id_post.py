from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyUpdatePvcVoiceSampleV1VoicesPvcVoiceIdSamplesSampleIdPost(BaseModel):
    """BodyUpdatePvcVoiceSampleV1VoicesPvcVoiceIdSamplesSampleIdPost

    :param remove_background_noise: If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse., defaults to None
    :type remove_background_noise: bool, optional
    :param selected_speaker_ids: Speaker IDs to be used for PVC training. Make sure you send all the speaker IDs you want to use for PVC training in one request because the last request will override the previous ones., defaults to None
    :type selected_speaker_ids: List[str], optional
    :param trim_start_time: The start time of the audio to be used for PVC training. Time should be in milliseconds, defaults to None
    :type trim_start_time: int, optional
    :param trim_end_time: The end time of the audio to be used for PVC training. Time should be in milliseconds, defaults to None
    :type trim_end_time: int, optional
    :param file_name: The name of the audio file to be used for PVC training., defaults to None
    :type file_name: str, optional
    """

    remove_background_noise: Optional[bool] = Field(
        default=None,
        description="If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.",
    )
    selected_speaker_ids: Optional[List[str]] = Field(
        default=None,
        description="Speaker IDs to be used for PVC training. Make sure you send all the speaker IDs you want to use for PVC training in one request because the last request will override the previous ones.",
    )
    trim_start_time: Optional[int] = Field(
        default=None,
        description="The start time of the audio to be used for PVC training. Time should be in milliseconds",
    )
    trim_end_time: Optional[int] = Field(
        default=None,
        description="The end time of the audio to be used for PVC training. Time should be in milliseconds",
    )
    file_name: Optional[str] = Field(
        default=None,
        description="The name of the audio file to be used for PVC training.",
    )
