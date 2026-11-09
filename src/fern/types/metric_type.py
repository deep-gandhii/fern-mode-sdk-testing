from __future__ import annotations
import typing
from typing import Any

MetricType = typing.Union[
    typing.Literal[
        "credits",
        "tts_characters",
        "minutes_used",
        "request_count",
        "ttfb_avg",
        "ttfb_p95",
        "fiat_units_spent",
        "concurrency",
        "concurrency_average",
    ],
    typing.Any,
]
