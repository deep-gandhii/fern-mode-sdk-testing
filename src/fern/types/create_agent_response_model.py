from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class CreateAgentResponseModel(BaseModel):
    """CreateAgentResponseModel

    :param agent_id: ID of the created agent
    :type agent_id: str
    """

    agent_id: str = Field(description="ID of the created agent")
