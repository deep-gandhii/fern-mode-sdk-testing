from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .audio_output import AudioOutput
from .final_output import FinalOutput

# Union type for ReceiveMessage
# Pydantic will attempt to validate against each type in order
ReceiveMessage = Union[AudioOutput, FinalOutput]
# TypeAdapter for runtime validation of ReceiveMessage
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ReceiveMessage_adapter = TypeAdapter(ReceiveMessage)
