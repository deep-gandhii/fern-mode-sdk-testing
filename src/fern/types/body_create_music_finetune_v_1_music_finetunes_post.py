from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

BodyCreateMusicFinetuneV1MusicFinetunesPostVisibility = typing.Union[
    typing.Literal["private", "workspace"], typing.Any
]

BodyCreateMusicFinetuneV1MusicFinetunesPostModelId = typing.Union[
    typing.Literal["music_v1", "music_v2"], typing.Any
]


class BodyCreateMusicFinetuneV1MusicFinetunesPost(BaseModel):
    """BodyCreateMusicFinetuneV1MusicFinetunesPost

    :param name: Name for the finetune (5-200 characters).
    :type name: str
    :param primary_genre: Primary musical genre of the finetune.
    :type primary_genre: str
    :param files: Audio files to train on., defaults to None
    :type files: List[bytes], optional
    :param tags: Tags to associate with the finetune., defaults to None
    :type tags: List[str], optional
    :param visibility: Finetune visibility. Only 'private' and 'workspace' can be set., defaults to None
    :type visibility: BodyCreateMusicFinetuneV1MusicFinetunesPostVisibility, optional
    :param model_id: The model to create a finetune for., defaults to None
    :type model_id: BodyCreateMusicFinetuneV1MusicFinetunesPostModelId, optional
    """

    name: str = Field(description="Name for the finetune (5-200 characters).")
    primary_genre: str = Field(description="Primary musical genre of the finetune.")
    files: Optional[List[bytes]] = Field(
        default=None, description="Audio files to train on."
    )
    tags: Optional[List[str]] = Field(
        default=None, description="Tags to associate with the finetune."
    )
    visibility: Optional[BodyCreateMusicFinetuneV1MusicFinetunesPostVisibility] = Field(
        default=None,
        description="Finetune visibility. Only 'private' and 'workspace' can be set.",
    )
    model_id: Optional[BodyCreateMusicFinetuneV1MusicFinetunesPostModelId] = Field(
        default=None, description="The model to create a finetune for."
    )
