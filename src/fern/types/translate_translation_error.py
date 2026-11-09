from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslateTranslationErrorMessageType = typing.Union[
    typing.Literal["translation_error"], typing.Any
]


class TranslateTranslationError(BaseModel):
    """TranslateTranslationError

    :param message_type: message_type
    :type message_type: TranslateTranslationErrorMessageType
    :param error: error
    :type error: str
    """

    message_type: TranslateTranslationErrorMessageType = Field(
        default="translation_error"
    )
    error: str
