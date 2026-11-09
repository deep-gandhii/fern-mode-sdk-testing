from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyDuplicateAgentV1ConvaiAgentsAgentIdDuplicatePost(BaseModel):
    """BodyDuplicateAgentV1ConvaiAgentsAgentIdDuplicatePost

    :param name: A name to make the agent easier to find, defaults to None
    :type name: str, optional
    """

    name: Optional[str] = Field(
        default=None, description="A name to make the agent easier to find"
    )
