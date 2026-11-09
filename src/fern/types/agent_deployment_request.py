from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .agent_deployment_request_item import AgentDeploymentRequestItem


class AgentDeploymentRequest(BaseModel):
    """AgentDeploymentRequest

    :param requests: List of deployment requests
    :type requests: List[AgentDeploymentRequestItem]
    """

    requests: List[AgentDeploymentRequestItem] = Field(
        description="List of deployment requests"
    )
