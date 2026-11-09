from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from .utils.base_model import BaseModel
from .translated_string import TranslatedString

SayNodeLiteralMessageInputType = typing.Union[typing.Literal["literal"], typing.Any]


class SayNodeLiteralMessageInput(BaseModel):
    """SayNodeLiteralMessageInput

    :param type: type, defaults to None
    :type type: SayNodeLiteralMessageInputType, optional
    :param text: Literal text message to be spoken by the agent.
    :type text: str
    :param text_translations: Translations for the text field, defaults to None
    :type text_translations: Dict[str, TranslatedString], optional
    """

    type: Optional[SayNodeLiteralMessageInputType] = Field(default=None)
    text: str = Field(description="Literal text message to be spoken by the agent.")
    text_translations: Optional[Dict[str, TranslatedString]] = Field(
        default=None, description="Translations for the text field"
    )
