from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class FlushContext(BaseModel):
    """Payload to flush the audio buffer for a specific context.

    :param context_id: The context_id to flush.
    :type context_id: str
    :param text: The text to append to the buffer to be flushed., defaults to None
    :type text: str, optional
    :param flush: If true, flushes the audio buffer for the specified context. If false, the context will remain open and the text will be appended to the buffer to be generated.
    :type flush: bool
    """

    context_id: str = Field(description="The context_id to flush.")
    text: Optional[str] = Field(
        default=None, description="The text to append to the buffer to be flushed."
    )
    flush: bool = Field(
        description="If true, flushes the audio buffer for the specified context. If false, the context will remain open and the text will be appended to the buffer to be generated."
    )
