from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class SpeechToTextWebhookResponseModel(BaseModel):
    """SpeechToTextWebhookResponseModel

    :param message: The message of the webhook response.
    :type message: str
    :param request_id: The request ID of the webhook response.
    :type request_id: str
    :param transcription_id: The transcription ID of the webhook response., defaults to None
    :type transcription_id: str, optional
    """

    message: str = Field(description="The message of the webhook response.")
    request_id: str = Field(description="The request ID of the webhook response.")
    transcription_id: Optional[str] = Field(
        default=None, description="The transcription ID of the webhook response."
    )
