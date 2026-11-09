from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class CloseContext(BaseModel):
    """Payload to close a specific TTS context.

    :param context_id: The context_id to close.
    :type context_id: str
    :param close_context: Must set the close_context to true, to close the specified context. If false, the context will remain open and the text will be ignored. If set to true, the context will close. If it has already been set to flush it will continue flushing. The same context id can be used again but will not be linked to the previous context with the same name.
    :type close_context: bool
    """

    context_id: str = Field(description="The context_id to close.")
    close_context: bool = Field(
        description="Must set the close_context to true, to close the specified context. If false, the context will remain open and the text will be ignored. If set to true, the context will close. If it has already been set to flush it will continue flushing. The same context id can be used again but will not be linked to the previous context with the same name."
    )
