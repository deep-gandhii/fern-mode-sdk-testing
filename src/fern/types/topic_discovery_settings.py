from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class TopicDiscoverySettings(BaseModel):
    """Per-agent topic-discovery configuration. Cadence and analysis window are managed internally; this only exposes the customer-facing on/off toggle."""

    pass
