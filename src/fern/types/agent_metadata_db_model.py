from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .agent_definition_source import AgentDefinitionSource


class AgentMetadataDbModel(BaseModel):
    """AgentMetadataDbModel

    :param created_at_unix_secs: created_at_unix_secs
    :type created_at_unix_secs: int
    :param updated_at_unix_secs: updated_at_unix_secs
    :type updated_at_unix_secs: int
    :param created_from: created_from, defaults to None
    :type created_from: AgentDefinitionSource, optional
    :param last_updated_from: last_updated_from, defaults to None
    :type last_updated_from: AgentDefinitionSource, optional
    """

    created_at_unix_secs: int
    updated_at_unix_secs: int
    created_from: Optional[AgentDefinitionSource] = Field(default=None)
    last_updated_from: Optional[AgentDefinitionSource] = Field(default=None)
