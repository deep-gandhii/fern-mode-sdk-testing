from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DependentAvailableAgentIdentifierType = typing.Union[
    typing.Literal["available"], typing.Any
]

DependentAvailableAgentIdentifierAccessLevel = typing.Union[
    typing.Literal["admin", "editor", "commenter", "viewer"], typing.Any
]


class DependentAvailableAgentIdentifier(BaseModel):
    """DependentAvailableAgentIdentifier

    :param referenced_resource_ids: If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly., defaults to None
    :type referenced_resource_ids: List[str], optional
    :param id: id
    :type id: str
    :param name: name
    :type name: str
    :param type: type, defaults to None
    :type type: DependentAvailableAgentIdentifierType, optional
    :param created_at_unix_secs: created_at_unix_secs
    :type created_at_unix_secs: int
    :param access_level: access_level
    :type access_level: DependentAvailableAgentIdentifierAccessLevel
    """

    referenced_resource_ids: Optional[List[str]] = Field(
        default=None,
        description="If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.",
    )
    id: str
    name: str
    type: Optional[DependentAvailableAgentIdentifierType] = Field(default=None)
    created_at_unix_secs: int
    access_level: DependentAvailableAgentIdentifierAccessLevel
