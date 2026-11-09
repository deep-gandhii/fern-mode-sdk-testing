from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class DownloadHistoryRequest(BaseModel):
    """DownloadHistoryRequest

    :param history_item_ids: A list of history items to download, you can get IDs of history items and other metadata using the GET https://api.elevenlabs.io/v1/history endpoint.
    :type history_item_ids: List[str]
    :param output_format: Output format to transcode the audio file, can be wav or default., defaults to None
    :type output_format: str, optional
    """

    history_item_ids: List[str] = Field(
        description="A list of history items to download, you can get IDs of history items and other metadata using the GET https://api.elevenlabs.io/v1/history endpoint."
    )
    output_format: Optional[str] = Field(
        default=None,
        description="Output format to transcode the audio file, can be wav or default.",
    )
