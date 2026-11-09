from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

TranscriptionOrderItemRequestKind = typing.Union[
    typing.Literal["transcription"], typing.Any
]


class TranscriptionOrderItemRequest(BaseModel):
    """TranscriptionOrderItemRequest

    :param kind: The type of order item., defaults to None
    :type kind: TranscriptionOrderItemRequestKind, optional
    :param media_ids: The IDs of the uploaded media files to transcribe.
    :type media_ids: List[str]
    :param source_language: The language code of the source media (e.g. 'en', 'es').
    :type source_language: str
    :param verbatim: Whether to transcribe every word exactly, including filler words., defaults to None
    :type verbatim: bool, optional
    :param instructions: Optional free-text instructions for the transcription team., defaults to None
    :type instructions: str, optional
    """

    kind: Optional[TranscriptionOrderItemRequestKind] = Field(
        default=None, description="The type of order item."
    )
    media_ids: List[str] = Field(
        description="The IDs of the uploaded media files to transcribe."
    )
    source_language: str = Field(
        description="The language code of the source media (e.g. 'en', 'es')."
    )
    verbatim: Optional[bool] = Field(
        default=None,
        description="Whether to transcribe every word exactly, including filler words.",
    )
    instructions: Optional[str] = Field(
        default=None,
        description="Optional free-text instructions for the transcription team.",
    )
