from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from .utils.base_model import BaseModel
from .translated_string import TranslatedString

SayNodeLiteralMessageOutputType = typing.Union[typing.Literal["literal"], typing.Any]


class SayNodeLiteralMessageOutput(BaseModel):
    """SayNodeLiteralMessageOutput

    :param type: type
    :type type: SayNodeLiteralMessageOutputType
    :param text: Literal text message to be spoken by the agent.
    :type text: str
    :param text_translations: Translations for the text field
    :type text_translations: Dict[str, TranslatedString]
    """

    type: SayNodeLiteralMessageOutputType = Field(default="literal")
    text: str = Field(description="Literal text message to be spoken by the agent.")
    text_translations: Dict[str, TranslatedString] = Field(
        description="Translations for the text field"
    )
