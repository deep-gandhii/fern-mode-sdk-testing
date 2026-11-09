from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

AddPronunciationDictionaryRequestWorkspaceAccess = typing.Union[
    typing.Literal["admin", "editor", "commenter", "viewer"], typing.Any
]


class AddPronunciationDictionaryRequest(BaseModel):
    """AddPronunciationDictionaryRequest

    :param name: The name of the pronunciation dictionary, used for identification only.
    :type name: str
    :param file: A lexicon .pls file which we will use to initialize the project with., defaults to None
    :type file: bytes, optional
    :param description: A description of the pronunciation dictionary, used for identification only., defaults to None
    :type description: str, optional
    :param workspace_access: Should be one of 'admin', 'editor' or 'viewer'. If not provided, defaults to no access., defaults to None
    :type workspace_access: AddPronunciationDictionaryRequestWorkspaceAccess, optional
    """

    name: str = Field(
        description="The name of the pronunciation dictionary, used for identification only."
    )
    file: Optional[bytes] = Field(
        default=None,
        description="A lexicon .pls file which we will use to initialize the project with.",
    )
    description: Optional[str] = Field(
        default=None,
        description="A description of the pronunciation dictionary, used for identification only.",
    )
    workspace_access: Optional[AddPronunciationDictionaryRequestWorkspaceAccess] = (
        Field(
            default=None,
            description="Should be one of 'admin', 'editor' or 'viewer'. If not provided, defaults to no access.",
        )
    )
