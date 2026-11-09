from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .allowed_output_formats import AllowedOutputFormats
from .music_only_output_formats import MusicOnlyOutputFormats

# Union type for MusicAllowedOutputFormats
# Pydantic will attempt to validate against each type in order
MusicAllowedOutputFormats = Union[str, str]
# TypeAdapter for runtime validation of MusicAllowedOutputFormats
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

MusicAllowedOutputFormats_adapter = TypeAdapter(MusicAllowedOutputFormats)
