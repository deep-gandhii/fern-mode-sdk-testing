from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

PronunciationDictionaryVersionResponseModelPermissionOnResource = typing.Union[
    typing.Literal["admin", "editor", "commenter", "viewer"], typing.Any
]


class PronunciationDictionaryVersionResponseModel(BaseModel):
    """PronunciationDictionaryVersionResponseModel

    :param version_id: version_id
    :type version_id: str
    :param version_rules_num: version_rules_num
    :type version_rules_num: int
    :param pronunciation_dictionary_id: pronunciation_dictionary_id
    :type pronunciation_dictionary_id: str
    :param dictionary_name: dictionary_name
    :type dictionary_name: str
    :param version_name: version_name
    :type version_name: str
    :param permission_on_resource: permission_on_resource
    :type permission_on_resource: PronunciationDictionaryVersionResponseModelPermissionOnResource
    :param created_by: created_by
    :type created_by: str
    :param creation_time_unix: creation_time_unix
    :type creation_time_unix: int
    :param archived_time_unix: archived_time_unix, defaults to None
    :type archived_time_unix: int, optional
    """

    version_id: str
    version_rules_num: int
    pronunciation_dictionary_id: str
    dictionary_name: str
    version_name: str
    permission_on_resource: Optional[
        PronunciationDictionaryVersionResponseModelPermissionOnResource
    ]
    created_by: str
    creation_time_unix: int
    archived_time_unix: Optional[int] = Field(default=None)
