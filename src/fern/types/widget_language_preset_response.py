from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .widget_text_contents import WidgetTextContents


class WidgetLanguagePresetResponse(BaseModel):
    """WidgetLanguagePresetResponse

    :param first_message: first_message, defaults to None
    :type first_message: str, optional
    :param text_contents: The text contents for the selected language, defaults to None
    :type text_contents: WidgetTextContents, optional
    :param terms_text: The text to display for terms and conditions in this language, defaults to None
    :type terms_text: str, optional
    :param terms_html: The HTML to display for terms and conditions in this language, defaults to None
    :type terms_html: str, optional
    :param terms_key: The key to display for terms and conditions in this language, defaults to None
    :type terms_key: str, optional
    """

    first_message: Optional[str] = Field(default=None)
    text_contents: Optional[WidgetTextContents] = Field(
        default=None, description="The text contents for the selected language"
    )
    terms_text: Optional[str] = Field(
        default=None,
        description="The text to display for terms and conditions in this language",
    )
    terms_html: Optional[str] = Field(
        default=None,
        description="The HTML to display for terms and conditions in this language",
    )
    terms_key: Optional[str] = Field(
        default=None,
        description="The key to display for terms and conditions in this language",
    )
