from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

BodyStemSeparationV1MusicStemSeparationPostStemVariationId = typing.Union[
    typing.Literal["two_stems_v1", "six_stems_v1"], typing.Any
]


class BodyStemSeparationV1MusicStemSeparationPost(BaseModel):
    """BodyStemSeparationV1MusicStemSeparationPost

    :param file: The audio file to separate into stems.
    :type file: bytes
    :param stem_variation_id: The id of the stem variation to use., defaults to None
    :type stem_variation_id: BodyStemSeparationV1MusicStemSeparationPostStemVariationId, optional
    :param sign_with_c_2_pa: Whether to sign the generated song with C2PA. Applicable only for mp3 files., defaults to None
    :type sign_with_c_2_pa: bool, optional
    """

    file: bytes = Field(description="The audio file to separate into stems.")
    stem_variation_id: Optional[
        BodyStemSeparationV1MusicStemSeparationPostStemVariationId
    ] = Field(default=None, description="The id of the stem variation to use.")
    sign_with_c_2_pa: Optional[bool] = Field(
        alias="sign_with_c2pa",
        serialization_alias="sign_with_c2pa",
        default=None,
        description="Whether to sign the generated song with C2PA. Applicable only for mp3 files.",
    )
