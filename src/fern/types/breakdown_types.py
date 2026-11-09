from __future__ import annotations
import typing
from typing import Any

BreakdownTypes = typing.Union[
    typing.Literal[
        "none",
        "voice",
        "voice_multiplier",
        "user",
        "groups",
        "api_keys",
        "all_api_keys",
        "product_type",
        "model",
        "resource",
        "request_queue",
        "region",
        "subresource_id",
        "reporting_workspace_id",
        "has_api_key",
        "request_source",
    ],
    typing.Any,
]
