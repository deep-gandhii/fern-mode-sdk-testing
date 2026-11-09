from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .soft_timeout_config_override_config import SoftTimeoutConfigOverrideConfig


class TurnConfigOverrideConfig(BaseModel):
    """TurnConfigOverrideConfig

    :param soft_timeout_config: soft_timeout_config, defaults to None
    :type soft_timeout_config: SoftTimeoutConfigOverrideConfig, optional
    """

    soft_timeout_config: Optional[SoftTimeoutConfigOverrideConfig] = Field(default=None)
