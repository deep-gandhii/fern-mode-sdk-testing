from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .soft_timeout_config_override import SoftTimeoutConfigOverride


class TurnConfigOverride(BaseModel):
    """TurnConfigOverride

    :param soft_timeout_config: Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses., defaults to None
    :type soft_timeout_config: SoftTimeoutConfigOverride, optional
    """

    soft_timeout_config: Optional[SoftTimeoutConfigOverride] = Field(
        default=None,
        description="Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.",
    )
