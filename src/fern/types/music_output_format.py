from __future__ import annotations
import typing
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .music_allowed_output_formats import (
    MusicAllowedOutputFormats,
    MusicAllowedOutputFormats_adapter,
)
from .allowed_output_formats import AllowedOutputFormats
from .music_only_output_formats import MusicOnlyOutputFormats

MusicOutputFormatOne = typing.Union[typing.Literal["auto"], typing.Any]


# Union type for MusicOutputFormat
# Pydantic will attempt to validate against each type in order
MusicOutputFormat = Union[str, str, str]
# TypeAdapter for runtime validation of MusicOutputFormat
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

MusicOutputFormat_adapter = TypeAdapter(MusicOutputFormat)
