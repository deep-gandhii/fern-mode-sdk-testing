from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_error import BaseError
from .utils.base_model import BaseModel


# Pydantic validation model for DownloadBadRequestResponse
class DownloadBadRequestResponseData(BaseModel):
    """DownloadBadRequestResponse

    :param error: error, defaults to None
    :type error: str, optional
    :param message: message, defaults to None
    :type message: str, optional
    """

    error: Optional[str] = Field(default=None)
    message: Optional[str] = Field(default=None)


# Error exception class
class DownloadBadRequestResponse(BaseError):
    """DownloadBadRequestResponse

    :param error: error, defaults to None
    :type error: str, optional
    :param message: message, defaults to None
    :type message: str, optional
    """

    _model_class = DownloadBadRequestResponseData
