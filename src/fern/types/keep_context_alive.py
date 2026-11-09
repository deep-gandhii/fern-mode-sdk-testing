from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

KeepContextAliveText = typing.Union[typing.Literal[""], typing.Any]


class KeepContextAlive(BaseModel):
    """Payload to keep a specific context alive by resetting its inactivity timeout. Empty text is ignored but resets the clock.

    :param text: An empty string. This text is ignored by the server but its presence resets the inactivity timeout for the specified context.
    :type text: KeepContextAliveText
    :param context_id: The identifier of the context to keep alive.
    :type context_id: str
    """

    text: KeepContextAliveText = Field(
        default="",
        description="An empty string. This text is ignored by the server but its presence resets the inactivity timeout for the specified context.",
    )
    context_id: str = Field(description="The identifier of the context to keep alive.")
