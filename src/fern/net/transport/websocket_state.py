"""Connection state for a websocket channel.

The state is read from the underlying ``websockets`` connection rather than tracked separately, so
it stays correct for transitions the SDK does not drive — a server-initiated close, or a handshake
still in flight. Both the sync and asyncio clients expose ``.state`` with these same four member
names, so the mapping is by name.
"""

import typing
from enum import Enum


class WebSocketState(str, Enum):
    CONNECTING = "connecting"
    OPEN = "open"
    CLOSING = "closing"
    CLOSED = "closed"


def resolve_websocket_state(websocket: typing.Any) -> WebSocketState:
    state = getattr(websocket, "state", None)
    name = getattr(state, "name", None)

    if name is None:
        return WebSocketState.CLOSED

    try:
        return WebSocketState[name]
    except KeyError:
        return WebSocketState.CLOSED
