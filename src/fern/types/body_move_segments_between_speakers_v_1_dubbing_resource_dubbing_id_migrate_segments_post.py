from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyMoveSegmentsBetweenSpeakersV1DubbingResourceDubbingIdMigrateSegmentsPost(
    BaseModel
):
    """BodyMoveSegmentsBetweenSpeakersV1DubbingResourceDubbingIdMigrateSegmentsPost

    :param segment_ids: segment_ids
    :type segment_ids: List[str]
    :param speaker_id: speaker_id
    :type speaker_id: str
    """

    segment_ids: List[str]
    speaker_id: str
