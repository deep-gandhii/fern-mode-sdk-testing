from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel

ReviewResponseModelReviewStatus = typing.Union[
    typing.Literal["approved", "edits_required", "rejected"], typing.Any
]

ReviewResponseModelRejectReasonsItem = typing.Union[
    typing.Literal[
        "lacks_structure",
        "doesnt_open",
        "not_literary_work",
        "language_not_supported",
        "too_short",
        "duplicate",
        "promotional",
        "formatting_issues",
        "low_quality",
        "metadata_incomplete",
        "metadata_inaccurate",
        "typos",
        "review_error",
        "spam",
        "legal_violation",
        "content_policy",
        "public_domain",
        "other",
    ],
    typing.Any,
]


class ReviewResponseModel(BaseModel):
    """ReviewResponseModel

    :param review_status: review_status
    :type review_status: ReviewResponseModelReviewStatus
    :param reviewed_at_unix: reviewed_at_unix
    :type reviewed_at_unix: int
    :param reviewed_by: reviewed_by, defaults to None
    :type reviewed_by: str, optional
    :param reject_reasons: reject_reasons, defaults to None
    :type reject_reasons: List[ReviewResponseModelRejectReasonsItem], optional
    :param scores_breakdown: scores_breakdown, defaults to None
    :type scores_breakdown: Dict[str, int], optional
    :param rejected_details: rejected_details, defaults to None
    :type rejected_details: str, optional
    :param explanation: explanation, defaults to None
    :type explanation: str, optional
    """

    review_status: ReviewResponseModelReviewStatus
    reviewed_at_unix: int
    reviewed_by: Optional[str] = Field(default=None)
    reject_reasons: Optional[List[ReviewResponseModelRejectReasonsItem]] = Field(
        default=None
    )
    scores_breakdown: Optional[Dict[str, int]] = Field(default=None)
    rejected_details: Optional[str] = Field(default=None)
    explanation: Optional[str] = Field(default=None)
