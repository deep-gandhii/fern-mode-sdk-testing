from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .history_alignment_response_model import HistoryAlignmentResponseModel


class HistoryAlignmentsResponseModel(BaseModel):
    """HistoryAlignmentsResponseModel

    :param alignment: alignment
    :type alignment: HistoryAlignmentResponseModel
    :param normalized_alignment: normalized_alignment
    :type normalized_alignment: HistoryAlignmentResponseModel
    """

    alignment: HistoryAlignmentResponseModel
    normalized_alignment: HistoryAlignmentResponseModel
