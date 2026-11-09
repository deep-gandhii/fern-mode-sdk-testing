from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class AsrConversationalConfigOverride(BaseModel):
    """AsrConversationalConfigOverride

    :param keywords: Keywords to boost prediction probability for, defaults to None
    :type keywords: List[str], optional
    """

    keywords: Optional[List[str]] = Field(
        default=None, description="Keywords to boost prediction probability for"
    )
