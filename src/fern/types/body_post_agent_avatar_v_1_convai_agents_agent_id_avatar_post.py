from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyPostAgentAvatarV1ConvaiAgentsAgentIdAvatarPost(BaseModel):
    """BodyPostAgentAvatarV1ConvaiAgentsAgentIdAvatarPost

    :param avatar_file: An image file to be used as the agent's avatar.
    :type avatar_file: bytes
    """

    avatar_file: bytes = Field(
        description="An image file to be used as the agent's avatar."
    )
