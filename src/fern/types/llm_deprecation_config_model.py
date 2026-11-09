from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class LlmDeprecationConfigModel(BaseModel):
    """LlmDeprecationConfigModel

    :param warning_start_days: Number of days before the provider deprecation date when warnings start being shown.
    :type warning_start_days: int
    :param fallback_start_days: Number of days before the provider deprecation date when traffic starts being routed to the replacement model.
    :type fallback_start_days: int
    :param fallback_complete_days: Number of days before the provider deprecation date when all traffic is routed to the replacement model.
    :type fallback_complete_days: int
    :param fallback_start_percentage: Percentage of traffic routed to the replacement model when fallback begins.
    :type fallback_start_percentage: int
    :param fallback_complete_percentage: Percentage of traffic routed to the replacement model when fallback is complete.
    :type fallback_complete_percentage: int
    """

    warning_start_days: int = Field(
        description="Number of days before the provider deprecation date when warnings start being shown."
    )
    fallback_start_days: int = Field(
        description="Number of days before the provider deprecation date when traffic starts being routed to the replacement model."
    )
    fallback_complete_days: int = Field(
        description="Number of days before the provider deprecation date when all traffic is routed to the replacement model."
    )
    fallback_start_percentage: int = Field(
        description="Percentage of traffic routed to the replacement model when fallback begins."
    )
    fallback_complete_percentage: int = Field(
        description="Percentage of traffic routed to the replacement model when fallback is complete."
    )
