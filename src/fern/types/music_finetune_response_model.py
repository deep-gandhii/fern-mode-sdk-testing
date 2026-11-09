from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .finetune_visibility import FinetuneVisibility
from .finetune_created_by import FinetuneCreatedBy
from .music_finetune_status import MusicFinetuneStatus
from .music_finetune_failure_reason import MusicFinetuneFailureReason


class MusicFinetuneResponseModel(BaseModel):
    """MusicFinetuneResponseModel

    :param id: Unique identifier of the finetune.
    :type id: str
    :param name: Name of the finetune.
    :type name: str
    :param tags: Tags associated with the finetune.
    :type tags: List[str]
    :param primary_genre: Primary musical genre of the finetune., defaults to None
    :type primary_genre: str, optional
    :param model_id: The base music model the finetune was trained on.
    :type model_id: str
    :param created_at: When the finetune was created (UTC).
    :type created_at: str
    :param visibility: visibility
    :type visibility: FinetuneVisibility
    :param created_by: created_by
    :type created_by: FinetuneCreatedBy
    :param status: status
    :type status: MusicFinetuneStatus
    :param training_progress: Training progress from 0.0 to 1.0.
    :type training_progress: float
    :param failure_reason: Reason the finetune failed or was blocked, if applicable., defaults to None
    :type failure_reason: MusicFinetuneFailureReason, optional
    """

    id: str = Field(description="Unique identifier of the finetune.")
    name: str = Field(description="Name of the finetune.")
    tags: List[str] = Field(description="Tags associated with the finetune.")
    primary_genre: Optional[str] = Field(
        default=None, description="Primary musical genre of the finetune."
    )
    model_id: str = Field(
        description="The base music model the finetune was trained on."
    )
    created_at: str = Field(description="When the finetune was created (UTC).")
    visibility: FinetuneVisibility
    created_by: FinetuneCreatedBy
    status: MusicFinetuneStatus
    training_progress: float = Field(description="Training progress from 0.0 to 1.0.")
    failure_reason: Optional[MusicFinetuneFailureReason] = Field(
        default=None,
        description="Reason the finetune failed or was blocked, if applicable.",
    )
