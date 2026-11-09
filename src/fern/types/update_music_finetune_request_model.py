from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

UpdateMusicFinetuneRequestModelVisibility = typing.Union[
    typing.Literal["private", "workspace"], typing.Any
]


class UpdateMusicFinetuneRequestModel(BaseModel):
    """UpdateMusicFinetuneRequestModel

    :param name: Updated name for the finetune., defaults to None
    :type name: str, optional
    :param tags: Replacement set of tags., defaults to None
    :type tags: List[str], optional
    :param primary_genre: Updated primary musical genre., defaults to None
    :type primary_genre: str, optional
    :param visibility: Finetune visibility. Only 'private' and 'workspace' can be set., defaults to None
    :type visibility: UpdateMusicFinetuneRequestModelVisibility, optional
    """

    name: Optional[str] = Field(
        default=None, description="Updated name for the finetune."
    )
    tags: Optional[List[str]] = Field(
        default=None, description="Replacement set of tags."
    )
    primary_genre: Optional[str] = Field(
        default=None, description="Updated primary musical genre."
    )
    visibility: Optional[UpdateMusicFinetuneRequestModelVisibility] = Field(
        default=None,
        description="Finetune visibility. Only 'private' and 'workspace' can be set.",
    )
