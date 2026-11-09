from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .character_gender import CharacterGender
from .character_age import CharacterAge
from .character_role import CharacterRole


class CharacterMetadataResponseModel(BaseModel):
    """CharacterMetadataResponseModel

    :param description: description, defaults to None
    :type description: str, optional
    :param sample_message: sample_message, defaults to None
    :type sample_message: str, optional
    :param voice_creation_prompt_suggestion: voice_creation_prompt_suggestion, defaults to None
    :type voice_creation_prompt_suggestion: str, optional
    :param gender: gender, defaults to None
    :type gender: CharacterGender, optional
    :param age: age, defaults to None
    :type age: CharacterAge, optional
    :param accent: accent, defaults to None
    :type accent: str, optional
    :param role: role, defaults to None
    :type role: CharacterRole, optional
    """

    description: Optional[str] = Field(default=None)
    sample_message: Optional[str] = Field(default=None)
    voice_creation_prompt_suggestion: Optional[str] = Field(default=None)
    gender: Optional[CharacterGender] = Field(default=None)
    age: Optional[CharacterAge] = Field(default=None)
    accent: Optional[str] = Field(default=None)
    role: Optional[CharacterRole] = Field(default=None)
