from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SpeakerCreatedResponse(BaseModel):
    """SpeakerCreatedResponse

    :param version: version
    :type version: int
    :param speaker_id: speaker_id
    :type speaker_id: str
    """

    version: int
    speaker_id: str
