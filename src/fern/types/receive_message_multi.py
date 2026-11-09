from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .audio_output_multi import AudioOutputMulti
from .final_output_multi import FinalOutputMulti

# Union type for ReceiveMessageMulti
# Pydantic will attempt to validate against each type in order
ReceiveMessageMulti = Union[AudioOutputMulti, FinalOutputMulti]
# TypeAdapter for runtime validation of ReceiveMessageMulti
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ReceiveMessageMulti_adapter = TypeAdapter(ReceiveMessageMulti)
