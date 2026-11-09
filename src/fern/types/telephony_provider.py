from __future__ import annotations
import typing
from typing import Any

TelephonyProvider = typing.Union[
    typing.Literal["twilio", "sip_trunk", "exotel"], typing.Any
]
