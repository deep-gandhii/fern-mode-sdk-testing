from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .voice_category import VoiceCategory


class SimilarVoice(BaseModel):
    """SimilarVoice

    :param voice_id: voice_id
    :type voice_id: str
    :param name: name
    :type name: str
    :param category: category
    :type category: VoiceCategory
    :param description: description, defaults to None
    :type description: str, optional
    :param preview_url: preview_url, defaults to None
    :type preview_url: str, optional
    """

    voice_id: str
    name: str
    category: VoiceCategory
    description: Optional[str] = Field(default=None)
    preview_url: Optional[str] = Field(default=None)
