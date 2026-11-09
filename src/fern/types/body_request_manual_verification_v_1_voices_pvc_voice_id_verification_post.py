from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyRequestManualVerificationV1VoicesPvcVoiceIdVerificationPost(BaseModel):
    """BodyRequestManualVerificationV1VoicesPvcVoiceIdVerificationPost

    :param files: Verification documents
    :type files: List[bytes]
    :param extra_text: Extra text to be used in the manual verification process., defaults to None
    :type extra_text: str, optional
    """

    files: List[bytes] = Field(description="Verification documents")
    extra_text: Optional[str] = Field(
        default=None,
        description="Extra text to be used in the manual verification process.",
    )
