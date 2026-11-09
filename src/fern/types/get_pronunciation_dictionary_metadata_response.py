from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

GetPronunciationDictionaryMetadataResponsePermissionOnResource = typing.Union[
    typing.Literal["admin", "editor", "commenter", "viewer"], typing.Any
]


class GetPronunciationDictionaryMetadataResponse(BaseModel):
    """GetPronunciationDictionaryMetadataResponse

    :param id: The ID of the pronunciation dictionary.
    :type id: str
    :param latest_version_id: The ID of the latest version of the pronunciation dictionary.
    :type latest_version_id: str
    :param latest_version_rules_num: The number of rules in the latest version of the pronunciation dictionary.
    :type latest_version_rules_num: int
    :param name: The name of the pronunciation dictionary.
    :type name: str
    :param permission_on_resource: The permission on the resource of the pronunciation dictionary.
    :type permission_on_resource: GetPronunciationDictionaryMetadataResponsePermissionOnResource
    :param created_by: The user ID of the creator of the pronunciation dictionary.
    :type created_by: str
    :param creation_time_unix: The creation time of the pronunciation dictionary in Unix timestamp.
    :type creation_time_unix: int
    :param archived_time_unix: The archive time of the pronunciation dictionary in Unix timestamp., defaults to None
    :type archived_time_unix: int, optional
    :param description: The description of the pronunciation dictionary., defaults to None
    :type description: str, optional
    """

    id: str = Field(description="The ID of the pronunciation dictionary.")
    latest_version_id: str = Field(
        description="The ID of the latest version of the pronunciation dictionary."
    )
    latest_version_rules_num: int = Field(
        description="The number of rules in the latest version of the pronunciation dictionary."
    )
    name: str = Field(description="The name of the pronunciation dictionary.")
    permission_on_resource: Optional[
        GetPronunciationDictionaryMetadataResponsePermissionOnResource
    ] = Field(
        description="The permission on the resource of the pronunciation dictionary."
    )
    created_by: str = Field(
        description="The user ID of the creator of the pronunciation dictionary."
    )
    creation_time_unix: int = Field(
        description="The creation time of the pronunciation dictionary in Unix timestamp."
    )
    archived_time_unix: Optional[int] = Field(
        default=None,
        description="The archive time of the pronunciation dictionary in Unix timestamp.",
    )
    description: Optional[str] = Field(
        default=None, description="The description of the pronunciation dictionary."
    )
