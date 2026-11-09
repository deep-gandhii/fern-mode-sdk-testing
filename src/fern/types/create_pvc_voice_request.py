from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel


class CreatePvcVoiceRequest(BaseModel):
    """CreatePvcVoiceRequest

    :param name: The name that identifies this voice. This will be displayed in the dropdown of the website.
    :type name: str
    :param language: Language used in the samples.
    :type language: str
    :param description: Description to use for the created voice., defaults to None
    :type description: str, optional
    :param labels: Labels for the voice. Keys can be language, accent, gender, or age., defaults to None
    :type labels: Dict[str, str], optional
    """

    name: str = Field(
        description="The name that identifies this voice. This will be displayed in the dropdown of the website."
    )
    language: str = Field(description="Language used in the samples.")
    description: Optional[str] = Field(
        default=None, description="Description to use for the created voice."
    )
    labels: Optional[Dict[str, str]] = Field(
        default=None,
        description="Labels for the voice. Keys can be language, accent, gender, or age.",
    )
