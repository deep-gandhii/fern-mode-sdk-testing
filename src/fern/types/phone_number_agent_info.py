from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class PhoneNumberAgentInfo(BaseModel):
    """PhoneNumberAgentInfo

    :param agent_id: The ID of the agent
    :type agent_id: str
    :param agent_name: The name of the agent
    :type agent_name: str
    :param environment: Environment to use for resolving environment variables on calls to this number., defaults to None
    :type environment: str, optional
    :param branch_id: Agent branch to use for calls to this number., defaults to None
    :type branch_id: str, optional
    """

    agent_id: str = Field(description="The ID of the agent")
    agent_name: str = Field(description="The name of the agent")
    environment: Optional[str] = Field(
        default=None,
        description="Environment to use for resolving environment variables on calls to this number.",
    )
    branch_id: Optional[str] = Field(
        default=None, description="Agent branch to use for calls to this number."
    )
