from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .voice_settings import VoiceSettings
from .dubbing_language_outputs import DubbingLanguageOutputs

DubbingLanguageResponseStatus = typing.Union[
    typing.Literal["queued", "processing", "completed", "stale", "failed"], typing.Any
]


class DubbingLanguageResponse(BaseModel):
    """DubbingLanguageResponse

    :param language_id: Unique identifier of the language target.
    :type language_id: str
    :param project_id: Identifier of the parent dubbing project.
    :type project_id: str
    :param target_language: BCP-47 language tag this target is dubbed into.
    :type target_language: str
    :param status: Lifecycle status: 'queued' (waiting on the project), 'processing', 'completed', 'stale' (source/transcript changed), or 'failed'.
    :type status: DubbingLanguageResponseStatus
    :param model_id: Effective dubbing model id (target override or project default)., defaults to None
    :type model_id: str, optional
    :param voice_settings: Voice settings applied to the whole language, or null if unset., defaults to None
    :type voice_settings: VoiceSettings, optional
    :param outputs: Signed output URLs; null until the target has produced an output (present once 'completed', and kept while 'stale' -- compare `output_revision` against `revision` to tell whether the output is up to date)., defaults to None
    :type outputs: DubbingLanguageOutputs, optional
    :param revision: Monotonic counter incremented whenever this target's transcript changes (a source edit affecting it, or an edit to its translation).
    :type revision: int
    :param output_revision: The `revision` the current dubbed output was generated from; equal to `revision` when up to date, less than it when 'stale'. Null until a generation has completed., defaults to None
    :type output_revision: int, optional
    :param created_at: When the language target was created.
    :type created_at: str
    :param updated_at: When the language target was last updated.
    :type updated_at: str
    """

    language_id: str = Field(description="Unique identifier of the language target.")
    project_id: str = Field(description="Identifier of the parent dubbing project.")
    target_language: str = Field(
        description="BCP-47 language tag this target is dubbed into."
    )
    status: DubbingLanguageResponseStatus = Field(
        description="Lifecycle status: 'queued' (waiting on the project), 'processing', 'completed', 'stale' (source/transcript changed), or 'failed'."
    )
    model_id: Optional[str] = Field(
        default=None,
        description="Effective dubbing model id (target override or project default).",
    )
    voice_settings: Optional[VoiceSettings] = Field(
        default=None,
        description="Voice settings applied to the whole language, or null if unset.",
    )
    outputs: Optional[DubbingLanguageOutputs] = Field(
        default=None,
        description="Signed output URLs; null until the target has produced an output (present once 'completed', and kept while 'stale' -- compare `output_revision` against `revision` to tell whether the output is up to date).",
    )
    revision: int = Field(
        description="Monotonic counter incremented whenever this target's transcript changes (a source edit affecting it, or an edit to its translation)."
    )
    output_revision: Optional[int] = Field(
        default=None,
        description="The `revision` the current dubbed output was generated from; equal to `revision` when up to date, less than it when 'stale'. Null until a generation has completed.",
    )
    created_at: str = Field(description="When the language target was created.")
    updated_at: str = Field(description="When the language target was last updated.")
