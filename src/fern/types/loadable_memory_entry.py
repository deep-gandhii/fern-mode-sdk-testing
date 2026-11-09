from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class LoadableMemoryEntry(BaseModel):
    """LoadableMemoryEntry

    :param entry_id: entry_id
    :type entry_id: str
    :param summary: summary
    :type summary: str
    :param text: text
    :type text: str
    """

    entry_id: str
    summary: str
    text: str
