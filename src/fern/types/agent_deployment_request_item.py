from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .agent_deployment_percentage_strategy import AgentDeploymentPercentageStrategy


class AgentDeploymentRequestItem(BaseModel):
    """AgentDeploymentRequestItem

    :param branch_id: ID of the branch to deploy
    :type branch_id: str
    :param deployment_strategy: deployment_strategy
    :type deployment_strategy: AgentDeploymentPercentageStrategy
    """

    branch_id: str = Field(description="ID of the branch to deploy")
    deployment_strategy: AgentDeploymentPercentageStrategy
