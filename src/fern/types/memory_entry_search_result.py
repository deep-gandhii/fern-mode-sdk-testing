from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .conversation_source import ConversationSource
from .manual_source import ManualSource


# fernMode variant type for a shared-component member of MemoryEntrySearchResultSource
class MemoryEntrySearchResultSource_Conversation(ConversationSource):
    pass


# fernMode variant type for a shared-component member of MemoryEntrySearchResultSource
class MemoryEntrySearchResultSource_Manual(ManualSource):
    pass


# Union type for MemoryEntrySearchResultSource
# Pydantic will attempt to validate against each type in order
MemoryEntrySearchResultSource = Union[ConversationSource, ManualSource]
# TypeAdapter for runtime validation of MemoryEntrySearchResultSource
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

MemoryEntrySearchResultSource_adapter = TypeAdapter(MemoryEntrySearchResultSource)


class MemoryEntrySearchResult(BaseModel):
    """MemoryEntrySearchResult

    :param entry_id: entry_id
    :type entry_id: str
    :param version: version
    :type version: int
    :param summary: summary, defaults to None
    :type summary: str, optional
    :param text: text, defaults to None
    :type text: str, optional
    :param source: source, defaults to None
    :type source: MemoryEntrySearchResultSource, optional
    """

    entry_id: str
    version: int
    summary: Optional[str] = Field(default=None)
    text: Optional[str] = Field(default=None)
    source: Optional[MemoryEntrySearchResultSource] = Field(default=None)
