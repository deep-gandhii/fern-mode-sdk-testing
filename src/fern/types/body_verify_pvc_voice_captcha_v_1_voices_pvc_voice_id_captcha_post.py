from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyVerifyPvcVoiceCaptchaV1VoicesPvcVoiceIdCaptchaPost(BaseModel):
    """BodyVerifyPvcVoiceCaptchaV1VoicesPvcVoiceIdCaptchaPost

    :param recording: Audio recording of the user
    :type recording: bytes
    """

    recording: bytes = Field(description="Audio recording of the user")
