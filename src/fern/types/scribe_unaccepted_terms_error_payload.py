from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ScribeUnacceptedTermsErrorPayloadMessageType = typing.Union[
    typing.Literal["unaccepted_terms"], typing.Any
]


class ScribeUnacceptedTermsErrorPayload(BaseModel):
    """Payload for unaccepted terms errors.

    :param message_type: The message type identifier.
    :type message_type: ScribeUnacceptedTermsErrorPayloadMessageType
    :param error: Unaccepted terms error details.
    :type error: str
    """

    message_type: ScribeUnacceptedTermsErrorPayloadMessageType = Field(
        default="unaccepted_terms", description="The message type identifier."
    )
    error: str = Field(description="Unaccepted terms error details.")
