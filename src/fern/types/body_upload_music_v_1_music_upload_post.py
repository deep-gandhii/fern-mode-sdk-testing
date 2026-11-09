from __future__ import annotations
from enum import Enum
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyUploadMusicV1MusicUploadPostExtractCompositionPlan(Enum):
    """An enumeration representing different categories.

    :cvar TRUE: True
    :vartype TRUE: str
    :cvar FALSE: False
    :vartype FALSE: str
    :cvar MUSICV1: "music_v1"
    :vartype MUSICV1: str
    :cvar MUSICV2: "music_v2"
    :vartype MUSICV2: str
    """

    TRUE = True
    FALSE = False
    MUSICV1 = "music_v1"
    MUSICV2 = "music_v2"

    @staticmethod
    def list():
        """Lists all enum values.

        :return: A list of all enum values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                BodyUploadMusicV1MusicUploadPostExtractCompositionPlan._member_map_.values(),
            )
        )


class BodyUploadMusicV1MusicUploadPost(BaseModel):
    """BodyUploadMusicV1MusicUploadPost

    :param file: The audio file to upload.
    :type file: bytes
    :param extract_composition_plan: Whether to generate and return the composition plan for the uploaded song. Pass a model id (`music_v1` or `music_v2`) to control which composition plan format is returned. Passing `true`/`false` is deprecated; `true` defaults to the `music_v1` plan format. Enabling this will increase the latency., defaults to None
    :type extract_composition_plan: BodyUploadMusicV1MusicUploadPostExtractCompositionPlan, optional
    :param with_timestamps: Whether to transcribe the uploaded song and return word-level timestamps. If True, the response will include words_timestamps but will increase the latency., defaults to None
    :type with_timestamps: bool, optional
    """

    file: bytes = Field(description="The audio file to upload.")
    extract_composition_plan: Optional[
        BodyUploadMusicV1MusicUploadPostExtractCompositionPlan
    ] = Field(
        default=None,
        description="Whether to generate and return the composition plan for the uploaded song. Pass a model id (`music_v1` or `music_v2`) to control which composition plan format is returned. Passing `true`/`false` is deprecated; `true` defaults to the `music_v1` plan format. Enabling this will increase the latency.",
    )
    with_timestamps: Optional[bool] = Field(
        default=None,
        description="Whether to transcribe the uploaded song and return word-level timestamps. If True, the response will include words_timestamps but will increase the latency.",
    )
