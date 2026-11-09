from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DetectedEntity(BaseModel):
    """An entity detected within transcribed text.

    :param text: The text that was identified as an entity.
    :type text: str
    :param entity_type: The type of entity detected (e.g., 'credit_card', 'email_address', 'person_name').
    :type entity_type: str
    :param start_char: Start character position in the transcript text.
    :type start_char: int
    :param end_char: End character position in the transcript text.
    :type end_char: int
    """

    text: str = Field(description="The text that was identified as an entity.")
    entity_type: str = Field(
        description="The type of entity detected (e.g., 'credit_card', 'email_address', 'person_name')."
    )
    start_char: int = Field(
        description="Start character position in the transcript text."
    )
    end_char: int = Field(description="End character position in the transcript text.")
