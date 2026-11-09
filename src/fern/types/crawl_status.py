from __future__ import annotations
import typing
from typing import Any

CrawlStatus = typing.Union[
    typing.Literal[
        "queued", "processing", "succeeded", "failed", "skipped", "cancelled"
    ],
    typing.Any,
]
