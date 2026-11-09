from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

AddPronunciationDictionaryResponseModelPermissionOnResource = typing.Union[
    typing.Literal["admin", "editor", "commenter", "viewer"], typing.Any
]


class AddPronunciationDictionaryResponseModel(BaseModel):
    """AddPronunciationDictionaryResponseModel

    :param id: The ID of the created pronunciation dictionary.
    :type id: str
    :param name: The name of the created pronunciation dictionary.
    :type name: str
    :param created_by: The user ID of the creator of the pronunciation dictionary.
    :type created_by: str
    :param creation_time_unix: The creation time of the pronunciation dictionary in Unix timestamp.
    :type creation_time_unix: int
    :param version_id: The ID of the created pronunciation dictionary version.
    :type version_id: str
    :param version_rules_num: The number of rules in the version of the pronunciation dictionary.
    :type version_rules_num: int
    :param description: The description of the pronunciation dictionary., defaults to None
    :type description: str, optional
    :param permission_on_resource: The permission on the resource of the pronunciation dictionary.
    :type permission_on_resource: AddPronunciationDictionaryResponseModelPermissionOnResource
    """

    id: str = Field(description="The ID of the created pronunciation dictionary.")
    name: str = Field(description="The name of the created pronunciation dictionary.")
    created_by: str = Field(
        description="The user ID of the creator of the pronunciation dictionary."
    )
    creation_time_unix: int = Field(
        description="The creation time of the pronunciation dictionary in Unix timestamp."
    )
    version_id: str = Field(
        description="The ID of the created pronunciation dictionary version."
    )
    version_rules_num: int = Field(
        description="The number of rules in the version of the pronunciation dictionary."
    )
    description: Optional[str] = Field(
        default=None, description="The description of the pronunciation dictionary."
    )
    permission_on_resource: Optional[
        AddPronunciationDictionaryResponseModelPermissionOnResource
    ] = Field(
        description="The permission on the resource of the pronunciation dictionary."
    )
