from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslateTranslationPayloadMessageType = typing.Union[
    typing.Literal["translation"], typing.Any
]


class TranslateTranslationPayload(BaseModel):
    """Translated text in the target language.

    :param message_type: The message type identifier.
    :type message_type: TranslateTranslationPayloadMessageType
    :param text: Translated text.
    :type text: str
    """

    message_type: TranslateTranslationPayloadMessageType = Field(
        default="translation", description="The message type identifier."
    )
    text: str = Field(description="Translated text.")
