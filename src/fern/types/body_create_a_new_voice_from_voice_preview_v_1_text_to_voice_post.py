from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel


class BodyCreateANewVoiceFromVoicePreviewV1TextToVoicePost(BaseModel):
    """BodyCreateANewVoiceFromVoicePreviewV1TextToVoicePost

    :param voice_name: Name to use for the created voice.
    :type voice_name: str
    :param voice_description: Description to use for the created voice.
    :type voice_description: str
    :param generated_voice_id: The generated_voice_id to create; obtain it from POST /v1/text-to-voice/design, POST /v1/text-to-voice/:voice_id/remix, or the response headers when generating previews.
    :type generated_voice_id: str
    :param labels: Optional, metadata to add to the created voice. Defaults to None., defaults to None
    :type labels: Dict[str, str], optional
    :param played_not_selected_voice_ids: List of voice ids that the user has played but not selected. Used for RLHF., defaults to None
    :type played_not_selected_voice_ids: List[str], optional
    """

    voice_name: str = Field(description="Name to use for the created voice.")
    voice_description: str = Field(
        description="Description to use for the created voice."
    )
    generated_voice_id: str = Field(
        description="The generated_voice_id to create; obtain it from POST /v1/text-to-voice/design, POST /v1/text-to-voice/:voice_id/remix, or the response headers when generating previews."
    )
    labels: Optional[Dict[str, str]] = Field(
        default=None,
        description="Optional, metadata to add to the created voice. Defaults to None.",
    )
    played_not_selected_voice_ids: Optional[List[str]] = Field(
        default=None,
        description="List of voice ids that the user has played but not selected. Used for RLHF.",
    )
