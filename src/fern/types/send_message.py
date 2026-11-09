from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .initialize_connection import InitializeConnection
from .send_text import SendText
from .close_connection import CloseConnection

# Union type for SendMessage
# Pydantic will attempt to validate against each type in order
SendMessage = Union[InitializeConnection, SendText, CloseConnection]
# TypeAdapter for runtime validation of SendMessage
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

SendMessage_adapter = TypeAdapter(SendMessage)
