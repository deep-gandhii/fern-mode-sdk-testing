from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AsrConversationalConfigOverrideConfig(BaseModel):
    """AsrConversationalConfigOverrideConfig

    :param keywords: Whether to allow overriding the keywords field., defaults to None
    :type keywords: bool, optional
    """

    keywords: Optional[bool] = Field(
        default=None, description="Whether to allow overriding the keywords field."
    )
