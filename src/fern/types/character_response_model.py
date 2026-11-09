from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .character_metadata_response_model import CharacterMetadataResponseModel


class CharacterResponseModel(BaseModel):
    """CharacterResponseModel

    :param character_id: character_id
    :type character_id: str
    :param name: name
    :type name: str
    :param metadata: metadata
    :type metadata: CharacterMetadataResponseModel
    :param recommended_voice_ids: recommended_voice_ids, defaults to None
    :type recommended_voice_ids: List[str], optional
    """

    character_id: str
    name: str
    metadata: CharacterMetadataResponseModel
    recommended_voice_ids: Optional[List[str]] = Field(default=None)
