from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .dubbing_source_media_info import DubbingSourceMediaInfo

DubbingProjectResponseStatus = typing.Union[
    typing.Literal["queued", "preparing", "processing", "ready", "failed"], typing.Any
]


class DubbingProjectResponse(BaseModel):
    """DubbingProjectResponse

    :param project_id: Unique identifier of the dubbing project.
    :type project_id: str
    :param status: Lifecycle status of the project: 'preparing'/'processing' while it transcribes, 'ready' once transcription is done, or 'failed'.
    :type status: DubbingProjectResponseStatus
    :param reference: Optional free-form string the customer can provide to identify the project on their end., defaults to None
    :type reference: str, optional
    :param source_language: BCP-47 language tag of the source media (null if auto-detected)., defaults to None
    :type source_language: str, optional
    :param model_id: Default dubbing model id applied to this project's language targets., defaults to None
    :type model_id: str, optional
    :param media: Source media metadata; null until the project is ready., defaults to None
    :type media: DubbingSourceMediaInfo, optional
    :param language_ids: Identifiers of the language targets created under this project., defaults to None
    :type language_ids: List[str], optional
    :param revision: Monotonic counter incremented whenever the source transcript is edited (segment add/edit/delete).
    :type revision: int
    :param created_at: When the project was created.
    :type created_at: str
    :param updated_at: When the project was last updated.
    :type updated_at: str
    """

    project_id: str = Field(description="Unique identifier of the dubbing project.")
    status: DubbingProjectResponseStatus = Field(
        description="Lifecycle status of the project: 'preparing'/'processing' while it transcribes, 'ready' once transcription is done, or 'failed'."
    )
    reference: Optional[str] = Field(
        default=None,
        description="Optional free-form string the customer can provide to identify the project on their end.",
    )
    source_language: Optional[str] = Field(
        default=None,
        description="BCP-47 language tag of the source media (null if auto-detected).",
    )
    model_id: Optional[str] = Field(
        default=None,
        description="Default dubbing model id applied to this project's language targets.",
    )
    media: Optional[DubbingSourceMediaInfo] = Field(
        default=None,
        description="Source media metadata; null until the project is ready.",
    )
    language_ids: Optional[List[str]] = Field(
        default=None,
        description="Identifiers of the language targets created under this project.",
    )
    revision: int = Field(
        description="Monotonic counter incremented whenever the source transcript is edited (segment add/edit/delete)."
    )
    created_at: str = Field(description="When the project was created.")
    updated_at: str = Field(description="When the project was last updated.")
