from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class CloseSocket(BaseModel):
    """Payload to signal closing the entire WebSocket connection.

    :param close_socket: If true, closes all contexts and closes the entire WebSocket connection. Any context that was previously set to flush will wait to flush before closing., defaults to None
    :type close_socket: bool, optional
    """

    close_socket: Optional[bool] = Field(
        default=None,
        description="If true, closes all contexts and closes the entire WebSocket connection. Any context that was previously set to flush will wait to flush before closing.",
    )
