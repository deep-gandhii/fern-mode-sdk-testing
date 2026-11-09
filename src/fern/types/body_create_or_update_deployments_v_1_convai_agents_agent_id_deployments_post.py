from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .agent_deployment_request import AgentDeploymentRequest


class BodyCreateOrUpdateDeploymentsV1ConvaiAgentsAgentIdDeploymentsPost(BaseModel):
    """BodyCreateOrUpdateDeploymentsV1ConvaiAgentsAgentIdDeploymentsPost

    :param deployment_request: deployment_request
    :type deployment_request: AgentDeploymentRequest
    """

    deployment_request: AgentDeploymentRequest
