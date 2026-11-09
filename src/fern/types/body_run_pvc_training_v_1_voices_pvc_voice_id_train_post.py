from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyRunPvcTrainingV1VoicesPvcVoiceIdTrainPost(BaseModel):
    """BodyRunPvcTrainingV1VoicesPvcVoiceIdTrainPost

    :param model_id: The model ID to use for the conversion., defaults to None
    :type model_id: str, optional
    """

    model_id: Optional[str] = Field(
        default=None, description="The model ID to use for the conversion."
    )
