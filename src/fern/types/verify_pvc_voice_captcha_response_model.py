from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class VerifyPvcVoiceCaptchaResponseModel(BaseModel):
    """VerifyPvcVoiceCaptchaResponseModel

    :param status: The status of the verify PVC captcha request. If the request was successful, the status will be 'ok'. Otherwise an error message with status 500 will be returned.
    :type status: str
    """

    status: str = Field(
        description="The status of the verify PVC captcha request. If the request was successful, the status will be 'ok'. Otherwise an error message with status 500 will be returned."
    )
