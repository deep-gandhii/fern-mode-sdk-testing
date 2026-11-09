from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .similar_voice import SimilarVoice


class SimilarVoicesForSpeakerResponse(BaseModel):
    """SimilarVoicesForSpeakerResponse

    :param voices: voices
    :type voices: List[SimilarVoice]
    """

    voices: List[SimilarVoice]
