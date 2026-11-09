from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from .utils.base_model import BaseModel


class WidgetTextContentsTranslation(BaseModel):
    """WidgetTextContentsTranslation

    :param source: The source text each translated field was derived from, defaults to None
    :type source: Dict[str, str], optional
    :param text: The last auto-translated output for each translated field, defaults to None
    :type text: Dict[str, str], optional
    """

    source: Optional[Dict[str, str]] = Field(
        default=None,
        description="The source text each translated field was derived from",
    )
    text: Optional[Dict[str, str]] = Field(
        default=None,
        description="The last auto-translated output for each translated field",
    )
