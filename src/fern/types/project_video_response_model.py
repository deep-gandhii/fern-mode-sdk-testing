from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .project_video_thumbnail_sheet_response_model import (
    ProjectVideoThumbnailSheetResponseModel,
)
from .pending_blocks_metadata_model import PendingBlocksMetadataModel
from .pending_external_audios_metadata_model import PendingExternalAudiosMetadataModel
from .pending_clip_task import PendingClipTask
from .generation_source_context import GenerationSourceContext
from .video_analysis import VideoAnalysis
from .asset_transcription import AssetTranscription
from .canvas_placement import CanvasPlacement
from .clip_animation import ClipAnimation

ProjectVideoResponseModelType = typing.Union[typing.Literal["video"], typing.Any]


class ProjectVideoResponseModel(BaseModel):
    """ProjectVideoResponseModel

    :param video_id: video_id
    :type video_id: str
    :param filename: filename
    :type filename: str
    :param signed_url: signed_url
    :type signed_url: str
    :param signed_preview_url: signed_preview_url
    :type signed_preview_url: str
    :param offset_ms: offset_ms
    :type offset_ms: int
    :param duration_ms: duration_ms
    :type duration_ms: int
    :param volume_gain_db: volume_gain_db
    :type volume_gain_db: float
    :param muted: muted
    :type muted: bool
    :param fade_in_ms: fade_in_ms, defaults to None
    :type fade_in_ms: int, optional
    :param fade_out_ms: fade_out_ms, defaults to None
    :type fade_out_ms: int, optional
    :param width: width
    :type width: int
    :param height: height
    :type height: int
    :param codec: codec
    :type codec: str
    :param order: order
    :type order: str
    :param created_at_ms: created_at_ms
    :type created_at_ms: int
    :param updated_at_ms: updated_at_ms
    :type updated_at_ms: int
    :param error: error, defaults to None
    :type error: str, optional
    :param thumbnail_interval_seconds: thumbnail_interval_seconds
    :type thumbnail_interval_seconds: float
    :param thumbnail_size: thumbnail_size
    :type thumbnail_size: List[int]
    :param thumbnail_sheets: thumbnail_sheets
    :type thumbnail_sheets: List[ProjectVideoThumbnailSheetResponseModel]
    :param start_time_ms: start_time_ms
    :type start_time_ms: int
    :param end_time_ms: end_time_ms
    :type end_time_ms: int
    :param asset_preview_signed_url: asset_preview_signed_url, defaults to None
    :type asset_preview_signed_url: str, optional
    :param source_video_id: source_video_id, defaults to None
    :type source_video_id: str, optional
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
    :param audio_track_ready: audio_track_ready, defaults to None
    :type audio_track_ready: bool, optional
    :param export_format_ready: export_format_ready, defaults to None
    :type export_format_ready: bool, optional
    :param current_snapshot_id: current_snapshot_id, defaults to None
    :type current_snapshot_id: str, optional
    :param source_context: source_context, defaults to None
    :type source_context: GenerationSourceContext, optional
    :param analysis: analysis, defaults to None
    :type analysis: VideoAnalysis, optional
    :param transcription: transcription, defaults to None
    :type transcription: AssetTranscription, optional
    :param type: type, defaults to None
    :type type: ProjectVideoResponseModelType, optional
    :param canvas_placement: Defines asset positioning and transformation on canvas., defaults to None
    :type canvas_placement: CanvasPlacement, optional
    :param animation: animation, defaults to None
    :type animation: ClipAnimation, optional
    :param playback_speed: playback_speed, defaults to None
    :type playback_speed: float, optional
    :param opacity: opacity, defaults to None
    :type opacity: float, optional
    :param track_id: track_id, defaults to None
    :type track_id: str, optional
    :param preview_job_progress: preview_job_progress, defaults to None
    :type preview_job_progress: float, optional
    :param import_speech_progress: import_speech_progress, defaults to None
    :type import_speech_progress: float, optional
    """

    video_id: str
    filename: str
    signed_url: Optional[str]
    signed_preview_url: Optional[str]
    offset_ms: int
    duration_ms: int
    volume_gain_db: float
    muted: bool
    fade_in_ms: Optional[int] = Field(default=None)
    fade_out_ms: Optional[int] = Field(default=None)
    width: int
    height: int
    codec: str
    order: str
    created_at_ms: int
    updated_at_ms: int
    error: Optional[str] = Field(default=None)
    thumbnail_interval_seconds: float
    thumbnail_size: List[int]
    thumbnail_sheets: List[ProjectVideoThumbnailSheetResponseModel]
    start_time_ms: int
    end_time_ms: Optional[int]
    asset_preview_signed_url: Optional[str] = Field(default=None)
    source_video_id: Optional[str] = Field(default=None)
    source_asset_id: Optional[str] = Field(default=None)
    source_platform_asset_id: Optional[str] = Field(default=None)
    pending_blocks_metadata: Optional[PendingBlocksMetadataModel] = Field(default=None)
    pending_external_audios_metadata: Optional[PendingExternalAudiosMetadataModel] = (
        Field(default=None)
    )
    speech_imported: Optional[bool] = Field(default=None)
    pending_task: Optional[PendingClipTask] = Field(default=None)
    audio_track_ready: Optional[bool] = Field(default=None)
    export_format_ready: Optional[bool] = Field(default=None)
    current_snapshot_id: Optional[str] = Field(default=None)
    source_context: Optional[GenerationSourceContext] = Field(default=None)
    analysis: Optional[VideoAnalysis] = Field(default=None)
    transcription: Optional[AssetTranscription] = Field(default=None)
    type: Optional[ProjectVideoResponseModelType] = Field(default=None)
    canvas_placement: Optional[CanvasPlacement] = Field(
        default=None,
        description="Defines asset positioning and transformation on canvas.",
    )
    animation: Optional[ClipAnimation] = Field(default=None)
    playback_speed: Optional[float] = Field(default=None)
    opacity: Optional[float] = Field(default=None)
    track_id: Optional[str] = Field(default=None)
    preview_job_progress: Optional[float] = Field(default=None)
    import_speech_progress: Optional[float] = Field(default=None)
