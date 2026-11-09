from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SendTextMulti(BaseModel):
    """Payload to send text for synthesis to an existing context.

    :param text: Text to synthesize. Should end with a single space.
    :type text: str
    :param context_id: The target context_id for this text., defaults to None
    :type context_id: str, optional
    :param flush: If true, flushes the audio buffer for the specified context. If false, the text will be appended to the buffer to be generated., defaults to None
    :type flush: bool, optional
    """

    text: str = Field(description="Text to synthesize. Should end with a single space.")
    context_id: Optional[str] = Field(
        default=None, description="The target context_id for this text."
    )
    flush: Optional[bool] = Field(
        default=None,
        description="If true, flushes the audio buffer for the specified context. If false, the text will be appended to the buffer to be generated.",
    )
