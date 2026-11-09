from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

BodyVideoToMusicV1MusicVideoToMusicPostModelId = typing.Union[
    typing.Literal["music_v1", "music_v2"], typing.Any
]


class BodyVideoToMusicV1MusicVideoToMusicPost(BaseModel):
    """BodyVideoToMusicV1MusicVideoToMusicPost

    :param videos: One or more video files sent via FormData array (multipart/form-data). They will be combined into one codec in order. A maximum of 10 videos is allowed, where the total size of the combined video is limited to 200MB. In total, the video can be up to 600 seconds long. Note that combining multiple videos may increase the request duration significantly. If possible, combine the videos beforehand.
    :type videos: List[bytes]
    :param description: Optional text description of the music you want. A maximum of 1000 characters is allowed., defaults to None
    :type description: str, optional
    :param tags: Optional list of style tags (e.g. ['upbeat', 'cinematic']). A maximum of 10 tags is allowed., defaults to None
    :type tags: List[str], optional
    :param model_id: The model to use for the generation., defaults to None
    :type model_id: BodyVideoToMusicV1MusicVideoToMusicPostModelId, optional
    :param sign_with_c_2_pa: Whether to sign the generated song with C2PA. Applicable only for mp3 files., defaults to None
    :type sign_with_c_2_pa: bool, optional
    """

    videos: List[bytes] = Field(
        description="One or more video files sent via FormData array (multipart/form-data). They will be combined into one codec in order. A maximum of 10 videos is allowed, where the total size of the combined video is limited to 200MB. In total, the video can be up to 600 seconds long. Note that combining multiple videos may increase the request duration significantly. If possible, combine the videos beforehand."
    )
    description: Optional[str] = Field(
        default=None,
        description="Optional text description of the music you want. A maximum of 1000 characters is allowed.",
    )
    tags: Optional[List[str]] = Field(
        default=None,
        description="Optional list of style tags (e.g. ['upbeat', 'cinematic']). A maximum of 10 tags is allowed.",
    )
    model_id: Optional[BodyVideoToMusicV1MusicVideoToMusicPostModelId] = Field(
        default=None, description="The model to use for the generation."
    )
    sign_with_c_2_pa: Optional[bool] = Field(
        alias="sign_with_c2pa",
        serialization_alias="sign_with_c2pa",
        default=None,
        description="Whether to sign the generated song with C2PA. Applicable only for mp3 files.",
    )
