from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AgentCallLimits(BaseModel):
    """AgentCallLimits

    :param agent_concurrency_limit: The maximum number of concurrent conversations. -1 indicates that there is no maximum, defaults to None
    :type agent_concurrency_limit: int, optional
    :param daily_limit: The maximum number of conversations per day, defaults to None
    :type daily_limit: int, optional
    :param bursting_enabled: Whether to enable bursting. If true, exceeding workspace concurrency limit will be allowed up to 3 times the limit. Calls will be charged at double rate when exceeding the limit., defaults to None
    :type bursting_enabled: bool, optional
    """

    agent_concurrency_limit: Optional[int] = Field(
        default=None,
        description="The maximum number of concurrent conversations. -1 indicates that there is no maximum",
    )
    daily_limit: Optional[int] = Field(
        default=None, description="The maximum number of conversations per day"
    )
    bursting_enabled: Optional[bool] = Field(
        default=None,
        description="Whether to enable bursting. If true, exceeding workspace concurrency limit will be allowed up to 3 times the limit. Calls will be charged at double rate when exceeding the limit.",
    )
