from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .initialize_connection_multi import InitializeConnectionMulti
from .initialise_context import InitialiseContext
from .send_text_multi import SendTextMulti
from .flush_context import FlushContext
from .close_context import CloseContext
from .close_socket import CloseSocket
from .keep_context_alive import KeepContextAlive

# Union type for SendMessageMulti
# Pydantic will attempt to validate against each type in order
SendMessageMulti = Union[
    InitializeConnectionMulti,
    InitialiseContext,
    SendTextMulti,
    FlushContext,
    CloseContext,
    CloseSocket,
    KeepContextAlive,
]
# TypeAdapter for runtime validation of SendMessageMulti
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

SendMessageMulti_adapter = TypeAdapter(SendMessageMulti)
