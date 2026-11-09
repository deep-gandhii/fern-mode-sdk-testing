from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

BodyCreateDubbingProjectV1DubbingProjectPostModelId = typing.Union[
    typing.Literal["dubbing_v2"], typing.Any
]


class BodyCreateDubbingProjectV1DubbingProjectPost(BaseModel):
    """BodyCreateDubbingProjectV1DubbingProjectPost

    :param file: The source media file to dub. Provide this or source_url., defaults to None
    :type file: bytes, optional
    :param source_url: Public URL to fetch the source media from. Provide this or file., defaults to None
    :type source_url: str, optional
    :param reference: Optional free-form string (max 500 characters) to identify the project on your end., defaults to None
    :type reference: str, optional
    :param source_language: BCP-47 language tag of the source media. Omit to auto-detect., defaults to None
    :type source_language: str, optional
    :param model_id: Default dubbing model id for the project's language targets; a target may override it. Omit to use the system default., defaults to None
    :type model_id: BodyCreateDubbingProjectV1DubbingProjectPostModelId, optional
    :param keyterms: Key terms to bias transcription/translation toward (e.g. product or brand names). At most 1000 terms; each term at most 50 characters and 5 words; the characters `<>{}[]\\` are not allowed., defaults to None
    :type keyterms: List[str], optional
    :param target_language: Optional shortcut: also create a language target in this BCP-47 language, queued to start once the project is ready., defaults to None
    :type target_language: str, optional
    """

    file: Optional[bytes] = Field(
        default=None,
        description="The source media file to dub. Provide this or source_url.",
    )
    source_url: Optional[str] = Field(
        default=None,
        description="Public URL to fetch the source media from. Provide this or file.",
    )
    reference: Optional[str] = Field(
        default=None,
        description="Optional free-form string (max 500 characters) to identify the project on your end.",
    )
    source_language: Optional[str] = Field(
        default=None,
        description="BCP-47 language tag of the source media. Omit to auto-detect.",
    )
    model_id: Optional[BodyCreateDubbingProjectV1DubbingProjectPostModelId] = Field(
        default=None,
        description="Default dubbing model id for the project's language targets; a target may override it. Omit to use the system default.",
    )
    keyterms: Optional[List[str]] = Field(
        default=None,
        description="Key terms to bias transcription/translation toward (e.g. product or brand names). At most 1000 terms; each term at most 50 characters and 5 words; the characters `<>{}[]\\` are not allowed.",
    )
    target_language: Optional[str] = Field(
        default=None,
        description="Optional shortcut: also create a language target in this BCP-47 language, queued to start once the project is ready.",
    )
