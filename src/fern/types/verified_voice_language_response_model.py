from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class VerifiedVoiceLanguageResponseModel(BaseModel):
    """VerifiedVoiceLanguageResponseModel

    :param language: The language of the voice.
    :type language: str
    :param model_id: The voice's model ID.
    :type model_id: str
    :param accent: The voice's accent, if applicable., defaults to None
    :type accent: str, optional
    :param locale: The voice's locale, if applicable., defaults to None
    :type locale: str, optional
    :param preview_url: The voice's preview URL, if applicable., defaults to None
    :type preview_url: str, optional
    """

    language: str = Field(description="The language of the voice.")
    model_id: str = Field(description="The voice's model ID.")
    accent: Optional[str] = Field(
        default=None, description="The voice's accent, if applicable."
    )
    locale: Optional[str] = Field(
        default=None, description="The voice's locale, if applicable."
    )
    preview_url: Optional[str] = Field(
        default=None, description="The voice's preview URL, if applicable."
    )
