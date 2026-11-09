from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .voice_preview_response_model import VoicePreviewResponseModel


class VoiceDesignPreviewResponse(BaseModel):
    """VoiceDesignPreviewResponse

    :param previews: The previews of the generated voices.
    :type previews: List[VoicePreviewResponseModel]
    :param text: The text used to preview the voices.
    :type text: str
    """

    previews: List[VoicePreviewResponseModel] = Field(
        description="The previews of the generated voices."
    )
    text: str = Field(description="The text used to preview the voices.")
