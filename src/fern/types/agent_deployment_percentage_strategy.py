from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AgentDeploymentPercentageStrategyType = typing.Union[
    typing.Literal["percentage"], typing.Any
]


class AgentDeploymentPercentageStrategy(BaseModel):
    """AgentDeploymentPercentageStrategy

    :param type: type, defaults to None
    :type type: AgentDeploymentPercentageStrategyType, optional
    :param traffic_percentage: Traffic percentage to deploy
    :type traffic_percentage: float
    """

    type: Optional[AgentDeploymentPercentageStrategyType] = Field(default=None)
    traffic_percentage: float = Field(description="Traffic percentage to deploy")
