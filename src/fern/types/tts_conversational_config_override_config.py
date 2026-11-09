from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class TtsConversationalConfigOverrideConfig(BaseModel):
    """TtsConversationalConfigOverrideConfig

    :param model_id: Whether to allow overriding the model_id field., defaults to None
    :type model_id: bool, optional
    :param voice_id: Whether to allow overriding the voice_id field., defaults to None
    :type voice_id: bool, optional
    :param stability: Whether to allow overriding the stability field., defaults to None
    :type stability: bool, optional
    :param speed: Whether to allow overriding the speed field., defaults to None
    :type speed: bool, optional
    :param similarity_boost: Whether to allow overriding the similarity_boost field., defaults to None
    :type similarity_boost: bool, optional
    """

    model_id: Optional[bool] = Field(
        default=None, description="Whether to allow overriding the model_id field."
    )
    voice_id: Optional[bool] = Field(
        default=None, description="Whether to allow overriding the voice_id field."
    )
    stability: Optional[bool] = Field(
        default=None, description="Whether to allow overriding the stability field."
    )
    speed: Optional[bool] = Field(
        default=None, description="Whether to allow overriding the speed field."
    )
    similarity_boost: Optional[bool] = Field(
        default=None,
        description="Whether to allow overriding the similarity_boost field.",
    )
