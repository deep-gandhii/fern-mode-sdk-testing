from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .canvas_placement import CanvasPlacement
from .clip_animation import ClipAnimation
from .pending_clip_task import PendingClipTask
from .image_analysis import ImageAnalysis

ProjectImageResponseModelType = typing.Union[typing.Literal["image"], typing.Any]

ProjectImageResponseModelSource = typing.Union[typing.Literal["upload"], typing.Any]


class ProjectImageResponseModel(BaseModel):
    """ProjectImageResponseModel

    :param image_id: image_id
    :type image_id: str
    :param filename: filename
    :type filename: str
    :param signed_url: signed_url, defaults to None
    :type signed_url: str, optional
    :param thumbnail_signed_url: thumbnail_signed_url, defaults to None
    :type thumbnail_signed_url: str, optional
    :param type: type, defaults to None
    :type type: ProjectImageResponseModelType, optional
    :param source: source, defaults to None
    :type source: ProjectImageResponseModelSource, optional
    :param file_size_bytes: file_size_bytes
    :type file_size_bytes: int
    :param width: width
    :type width: int
    :param height: height
    :type height: int
    :param track_id: track_id, defaults to None
    :type track_id: str, optional
    :param offset_ms: offset_ms
    :type offset_ms: int
    :param duration_ms: duration_ms
    :type duration_ms: int
    :param order: order
    :type order: str
    :param canvas_placement: Defines asset positioning and transformation on canvas.
    :type canvas_placement: CanvasPlacement
    :param animation: animation, defaults to None
    :type animation: ClipAnimation, optional
    :param opacity: opacity, defaults to None
    :type opacity: float, optional
    :param created_at_ms: created_at_ms
    :type created_at_ms: int
    :param updated_at_ms: updated_at_ms
    :type updated_at_ms: int
    :param current_snapshot_id: current_snapshot_id, defaults to None
    :type current_snapshot_id: str, optional
    :param source_asset_id: source_asset_id, defaults to None
    :type source_asset_id: str, optional
    :param source_platform_asset_id: source_platform_asset_id, defaults to None
    :type source_platform_asset_id: str, optional
    :param error: error, defaults to None
    :type error: str, optional
    :param pending_task: pending_task, defaults to None
    :type pending_task: PendingClipTask, optional
    :param analysis: analysis, defaults to None
    :type analysis: ImageAnalysis, optional
    """

    image_id: str
    filename: str
    signed_url: Optional[str] = Field(default=None)
    thumbnail_signed_url: Optional[str] = Field(default=None)
    type: Optional[ProjectImageResponseModelType] = Field(default=None)
    source: Optional[ProjectImageResponseModelSource] = Field(default=None)
    file_size_bytes: int
    width: int
    height: int
    track_id: Optional[str] = Field(default=None)
    offset_ms: int
    duration_ms: int
    order: str
    canvas_placement: CanvasPlacement = Field(
        description="Defines asset positioning and transformation on canvas."
    )
    animation: Optional[ClipAnimation] = Field(default=None)
    opacity: Optional[float] = Field(default=None)
    created_at_ms: int
    updated_at_ms: int
    current_snapshot_id: Optional[str] = Field(default=None)
    source_asset_id: Optional[str] = Field(default=None)
    source_platform_asset_id: Optional[str] = Field(default=None)
    error: Optional[str] = Field(default=None)
    pending_task: Optional[PendingClipTask] = Field(default=None)
    analysis: Optional[ImageAnalysis] = Field(default=None)
