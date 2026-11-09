from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .resource_access_info import ResourceAccessInfo


class SpeechEngineSummaryResponse(BaseModel):
    """SpeechEngineSummaryResponse

    :param speech_engine_id: The speech engine resource ID
    :type speech_engine_id: str
    :param name: Human-readable name for the speech engine
    :type name: str
    :param created_at_unix_secs: Creation time in Unix seconds
    :type created_at_unix_secs: int
    :param tags: Arbitrary tags for categorization and filtering
    :type tags: List[str]
    :param access_info: access_info
    :type access_info: ResourceAccessInfo
    """

    speech_engine_id: str = Field(description="The speech engine resource ID")
    name: str = Field(description="Human-readable name for the speech engine")
    created_at_unix_secs: int = Field(description="Creation time in Unix seconds")
    tags: List[str] = Field(
        description="Arbitrary tags for categorization and filtering"
    )
    access_info: ResourceAccessInfo
