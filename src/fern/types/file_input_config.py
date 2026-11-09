from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class FileInputConfig(BaseModel):
    """FileInputConfig

    :param enabled: When enabled, users may attach images or PDFs in chat when the LLM supports multimodal input., defaults to None
    :type enabled: bool, optional
    :param max_files_in_memory: Number of most-recent files kept in memory during a conversation. Older files are summarized and their bytes freed., defaults to None
    :type max_files_in_memory: int, optional
    :param max_files_per_conversation: Total files a user can upload in one conversation. Uploads are billed per file. Use -1 for no limit, or a value >= max_files_in_memory., defaults to None
    :type max_files_per_conversation: int, optional
    """

    enabled: Optional[bool] = Field(
        default=None,
        description="When enabled, users may attach images or PDFs in chat when the LLM supports multimodal input.",
    )
    max_files_in_memory: Optional[int] = Field(
        default=None,
        description="Number of most-recent files kept in memory during a conversation. Older files are summarized and their bytes freed.",
    )
    max_files_per_conversation: Optional[int] = Field(
        default=None,
        description="Total files a user can upload in one conversation. Uploads are billed per file. Use -1 for no limit, or a value >= max_files_in_memory.",
    )
