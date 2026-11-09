from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel


class BodyEditPvcVoiceV1VoicesPvcVoiceIdPost(BaseModel):
    """BodyEditPvcVoiceV1VoicesPvcVoiceIdPost

    :param name: The name that identifies this voice. This will be displayed in the dropdown of the website., defaults to None
    :type name: str, optional
    :param language: Language used in the samples., defaults to None
    :type language: str, optional
    :param description: Description to use for the created voice., defaults to None
    :type description: str, optional
    :param labels: Labels for the voice. Keys can be language, accent, gender, or age., defaults to None
    :type labels: Dict[str, str], optional
    """

    name: Optional[str] = Field(
        default=None,
        description="The name that identifies this voice. This will be displayed in the dropdown of the website.",
    )
    language: Optional[str] = Field(
        default=None, description="Language used in the samples."
    )
    description: Optional[str] = Field(
        default=None, description="Description to use for the created voice."
    )
    labels: Optional[Dict[str, str]] = Field(
        default=None,
        description="Labels for the voice. Keys can be language, accent, gender, or age.",
    )
