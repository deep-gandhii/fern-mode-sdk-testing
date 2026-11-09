from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AgentMetadataResponseModel(BaseModel):
    """AgentMetadataResponseModel

    :param created_at_unix_secs: The creation time of the agent in unix seconds
    :type created_at_unix_secs: int
    :param updated_at_unix_secs: The last update time of the agent in unix seconds
    :type updated_at_unix_secs: int
    """

    created_at_unix_secs: int = Field(
        description="The creation time of the agent in unix seconds"
    )
    updated_at_unix_secs: int = Field(
        description="The last update time of the agent in unix seconds"
    )
