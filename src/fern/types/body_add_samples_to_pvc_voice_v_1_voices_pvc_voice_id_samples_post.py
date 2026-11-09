from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyAddSamplesToPvcVoiceV1VoicesPvcVoiceIdSamplesPost(BaseModel):
    """BodyAddSamplesToPvcVoiceV1VoicesPvcVoiceIdSamplesPost

    :param files: Audio files used to create the voice.
    :type files: List[bytes]
    :param remove_background_noise: If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse., defaults to None
    :type remove_background_noise: bool, optional
    """

    files: List[bytes] = Field(description="Audio files used to create the voice.")
    remove_background_noise: Optional[bool] = Field(
        default=None,
        description="If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.",
    )
