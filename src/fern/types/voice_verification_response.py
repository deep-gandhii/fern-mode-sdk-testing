from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .verification_attempt_response import VerificationAttemptResponse


class VoiceVerificationResponse(BaseModel):
    """VoiceVerificationResponse

    :param requires_verification: Whether the voice requires verification.
    :type requires_verification: bool
    :param is_verified: Whether the voice has been verified.
    :type is_verified: bool
    :param verification_failures: List of verification failures.
    :type verification_failures: List[str]
    :param verification_attempts_count: The number of verification attempts.
    :type verification_attempts_count: int
    :param language: The language of the voice., defaults to None
    :type language: str, optional
    :param verification_attempts: Number of times a verification was attempted., defaults to None
    :type verification_attempts: List[VerificationAttemptResponse], optional
    """

    requires_verification: bool = Field(
        description="Whether the voice requires verification."
    )
    is_verified: bool = Field(description="Whether the voice has been verified.")
    verification_failures: List[str] = Field(
        description="List of verification failures."
    )
    verification_attempts_count: int = Field(
        description="The number of verification attempts."
    )
    language: Optional[str] = Field(
        default=None, description="The language of the voice."
    )
    verification_attempts: Optional[List[VerificationAttemptResponse]] = Field(
        default=None, description="Number of times a verification was attempted."
    )
