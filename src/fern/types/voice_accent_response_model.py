from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class VoiceAccentResponseModel(BaseModel):
    """VoiceAccentResponseModel

    :param accent: The accent value used for filtering shared voices via the `accent` query parameter on `GET /v1/shared-voices`.
    :type accent: str
    :param language: The language code this accent belongs to, e.g. `en`.
    :type language: str
    :param code: The full accent code, e.g. `en-american`.
    :type code: str
    :param name: The human-readable accent name, e.g. `American`.
    :type name: str
    """

    accent: str = Field(
        description="The accent value used for filtering shared voices via the `accent` query parameter on `GET /v1/shared-voices`."
    )
    language: str = Field(
        description="The language code this accent belongs to, e.g. `en`."
    )
    code: str = Field(description="The full accent code, e.g. `en-american`.")
    name: str = Field(description="The human-readable accent name, e.g. `American`.")
