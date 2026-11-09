from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .manual_verification_file_response import ManualVerificationFileResponse


class ManualVerificationResponse(BaseModel):
    """ManualVerificationResponse

    :param extra_text: The extra text of the manual verification.
    :type extra_text: str
    :param request_time_unix: The date of the manual verification in Unix time.
    :type request_time_unix: int
    :param files: The files of the manual verification.
    :type files: List[ManualVerificationFileResponse]
    """

    extra_text: str = Field(description="The extra text of the manual verification.")
    request_time_unix: int = Field(
        description="The date of the manual verification in Unix time."
    )
    files: List[ManualVerificationFileResponse] = Field(
        description="The files of the manual verification."
    )
