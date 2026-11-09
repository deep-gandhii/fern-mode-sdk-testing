from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .chapter_content_block_tts_node_response_model import (
    ChapterContentBlockTtsNodeResponseModel,
)
from .chapter_content_block_extendable_node_response_model import (
    ChapterContentBlockExtendableNodeResponseModel,
)


# fernMode variant type for a shared-component member of ChapterContentBlockResponseModelNodesItem
class ChapterContentBlockResponseModelNodesItem_TtsNode(
    ChapterContentBlockTtsNodeResponseModel
):
    pass


# fernMode variant type for a shared-component member of ChapterContentBlockResponseModelNodesItem
class ChapterContentBlockResponseModelNodesItem_Other(
    ChapterContentBlockExtendableNodeResponseModel
):
    pass


# Union type for ChapterContentBlockResponseModelNodesItem
# Pydantic will attempt to validate against each type in order
ChapterContentBlockResponseModelNodesItem = Union[
    ChapterContentBlockTtsNodeResponseModel,
    ChapterContentBlockExtendableNodeResponseModel,
]
# TypeAdapter for runtime validation of ChapterContentBlockResponseModelNodesItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ChapterContentBlockResponseModelNodesItem_adapter = TypeAdapter(
    ChapterContentBlockResponseModelNodesItem
)


class ChapterContentBlockResponseModel(BaseModel):
    """ChapterContentBlockResponseModel

    :param block_id: block_id
    :type block_id: str
    :param nodes: nodes
    :type nodes: List[ChapterContentBlockResponseModelNodesItem]
    """

    block_id: str
    nodes: List[ChapterContentBlockResponseModelNodesItem]
