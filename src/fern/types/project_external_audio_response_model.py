from __future__ import annotations
import typing
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .pending_blocks_metadata_model import PendingBlocksMetadataModel
from .pending_external_audios_metadata_model import PendingExternalAudiosMetadataModel
from .pending_clip_task import PendingClipTask
from .audio_analysis import AudioAnalysis
from .asset_transcription import AssetTranscription
from .song_source_context import SongSourceContext
from .music_explore_song_source_context import MusicExploreSongSourceContext
from .sfx_source_context import SfxSourceContext


# fernMode variant type for a shared-component member of ProjectExternalAudioResponseModelSourceContext
class ProjectExternalAudioResponseModelSourceContext_Song(SongSourceContext):
    pass


# fernMode variant type for a shared-component member of ProjectExternalAudioResponseModelSourceContext
class ProjectExternalAudioResponseModelSourceContext_MusicExploreSong(
    MusicExploreSongSourceContext
):
    pass


# fernMode variant type for a shared-component member of ProjectExternalAudioResponseModelSourceContext
class ProjectExternalAudioResponseModelSourceContext_Sfx(SfxSourceContext):
    pass


# Union type for ProjectExternalAudioResponseModelSourceContext
# Pydantic will attempt to validate against each type in order
ProjectExternalAudioResponseModelSourceContext = Union[
    SongSourceContext, MusicExploreSongSourceContext, SfxSourceContext
]
# TypeAdapter for runtime validation of ProjectExternalAudioResponseModelSourceContext
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ProjectExternalAudioResponseModelSourceContext_adapter = TypeAdapter(
    ProjectExternalAudioResponseModelSourceContext
)


ProjectExternalAudioResponseModelType = typing.Union[
    typing.Literal["audio"], typing.Any
]


class ProjectExternalAudioResponseModel(BaseModel):
    """ProjectExternalAudioResponseModel

    :param external_audio_id: external_audio_id
    :type external_audio_id: str
    :param filename: filename
    :type filename: str
    :param signed_url: signed_url
    :type signed_url: str
    :param offset_ms: offset_ms
    :type offset_ms: int
    :param duration_ms: duration_ms
    :type duration_ms: int
    :param start_time_ms: start_time_ms
    :type start_time_ms: int
    :param end_time_ms: end_time_ms
    :type end_time_ms: int
    :param order: order
    :type order: str
    :param track_id: track_id
    :type track_id: str
    :param created_at_ms: created_at_ms
    :type created_at_ms: int
    :param updated_at_ms: updated_at_ms
    :type updated_at_ms: int
    :param volume_gain_db: volume_gain_db, defaults to None
    :type volume_gain_db: float, optional
    :param muted: muted, defaults to None
    :type muted: bool, optional
    :param fade_in_ms: fade_in_ms, defaults to None
    :type fade_in_ms: int, optional
    :param fade_out_ms: fade_out_ms, defaults to None
    :type fade_out_ms: int, optional
    :param source_external_audio_id: source_external_audio_id, defaults to None
    :type source_external_audio_id: str, optional
    :param source_asset_id: source_asset_id, defaults to None
    :type source_asset_id: str, optional
    :param source_platform_asset_id: source_platform_asset_id, defaults to None
    :type source_platform_asset_id: str, optional
    :param pending_blocks_metadata: pending_blocks_metadata, defaults to None
    :type pending_blocks_metadata: PendingBlocksMetadataModel, optional
    :param pending_external_audios_metadata: pending_external_audios_metadata, defaults to None
    :type pending_external_audios_metadata: PendingExternalAudiosMetadataModel, optional
    :param speech_imported: speech_imported, defaults to None
    :type speech_imported: bool, optional
    :param pending_task: pending_task, defaults to None
    :type pending_task: PendingClipTask, optional
    :param error: error, defaults to None
    :type error: str, optional
    :param current_snapshot_id: current_snapshot_id, defaults to None
    :type current_snapshot_id: str, optional
    :param source_context: source_context, defaults to None
    :type source_context: ProjectExternalAudioResponseModelSourceContext, optional
    :param analysis: analysis, defaults to None
    :type analysis: AudioAnalysis, optional
    :param transcription: transcription, defaults to None
    :type transcription: AssetTranscription, optional
    :param type: type, defaults to None
    :type type: ProjectExternalAudioResponseModelType, optional
    :param import_speech_progress: import_speech_progress, defaults to None
    :type import_speech_progress: float, optional
    """

    external_audio_id: str
    filename: str
    signed_url: Optional[str]
    offset_ms: int
    duration_ms: int
    start_time_ms: int
    end_time_ms: Optional[int]
    order: str
    track_id: str
    created_at_ms: int
    updated_at_ms: int
    volume_gain_db: Optional[float] = Field(default=None)
    muted: Optional[bool] = Field(default=None)
    fade_in_ms: Optional[int] = Field(default=None)
    fade_out_ms: Optional[int] = Field(default=None)
    source_external_audio_id: Optional[str] = Field(default=None)
    source_asset_id: Optional[str] = Field(default=None)
    source_platform_asset_id: Optional[str] = Field(default=None)
    pending_blocks_metadata: Optional[PendingBlocksMetadataModel] = Field(default=None)
    pending_external_audios_metadata: Optional[PendingExternalAudiosMetadataModel] = (
        Field(default=None)
    )
    speech_imported: Optional[bool] = Field(default=None)
    pending_task: Optional[PendingClipTask] = Field(default=None)
    error: Optional[str] = Field(default=None)
    current_snapshot_id: Optional[str] = Field(default=None)
    source_context: Optional[ProjectExternalAudioResponseModelSourceContext] = Field(
        default=None
    )
    analysis: Optional[AudioAnalysis] = Field(default=None)
    transcription: Optional[AssetTranscription] = Field(default=None)
    type: Optional[ProjectExternalAudioResponseModelType] = Field(default=None)
    import_speech_progress: Optional[float] = Field(default=None)
