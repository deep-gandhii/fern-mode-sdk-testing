from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .verification_attempt_response import VerificationAttemptResponse
from .manual_verification_response import ManualVerificationResponse

FineTuningResponseStateValue = typing.Union[
    typing.Literal[
        "not_started", "queued", "fine_tuning", "fine_tuned", "failed", "delayed"
    ],
    typing.Any,
]


class FineTuningResponse(BaseModel):
    """FineTuningResponse

    :param is_allowed_to_fine_tune: Whether the user is allowed to fine-tune the voice., defaults to None
    :type is_allowed_to_fine_tune: bool, optional
    :param state: The state of the fine-tuning process for each model., defaults to None
    :type state: Dict[str, FineTuningResponseStateValue], optional
    :param verification_failures: List of verification failures in the fine-tuning process., defaults to None
    :type verification_failures: List[str], optional
    :param verification_attempts_count: The number of verification attempts in the fine-tuning process., defaults to None
    :type verification_attempts_count: int, optional
    :param manual_verification_requested: Whether a manual verification was requested for the fine-tuning process., defaults to None
    :type manual_verification_requested: bool, optional
    :param language: The language of the fine-tuning process., defaults to None
    :type language: str, optional
    :param progress: The progress of the fine-tuning process., defaults to None
    :type progress: Dict[str, float], optional
    :param message: The message of the fine-tuning process., defaults to None
    :type message: Dict[str, str], optional
    :param dataset_duration_seconds: The duration of the dataset in seconds., defaults to None
    :type dataset_duration_seconds: float, optional
    :param verification_attempts: The number of verification attempts., defaults to None
    :type verification_attempts: List[VerificationAttemptResponse], optional
    :param slice_ids: List of slice IDs., defaults to None
    :type slice_ids: List[str], optional
    :param manual_verification: The manual verification of the fine-tuning process., defaults to None
    :type manual_verification: ManualVerificationResponse, optional
    :param max_verification_attempts: The maximum number of verification attempts., defaults to None
    :type max_verification_attempts: int, optional
    :param next_max_verification_attempts_reset_unix_ms: The next maximum verification attempts reset time in Unix milliseconds., defaults to None
    :type next_max_verification_attempts_reset_unix_ms: int, optional
    :param finetuning_state: finetuning_state, defaults to None
    :type finetuning_state: Any, optional
    """

    is_allowed_to_fine_tune: Optional[bool] = Field(
        default=None, description="Whether the user is allowed to fine-tune the voice."
    )
    state: Optional[Dict[str, FineTuningResponseStateValue]] = Field(
        default=None, description="The state of the fine-tuning process for each model."
    )
    verification_failures: Optional[List[str]] = Field(
        default=None,
        description="List of verification failures in the fine-tuning process.",
    )
    verification_attempts_count: Optional[int] = Field(
        default=None,
        description="The number of verification attempts in the fine-tuning process.",
    )
    manual_verification_requested: Optional[bool] = Field(
        default=None,
        description="Whether a manual verification was requested for the fine-tuning process.",
    )
    language: Optional[str] = Field(
        default=None, description="The language of the fine-tuning process."
    )
    progress: Optional[Dict[str, float]] = Field(
        default=None, description="The progress of the fine-tuning process."
    )
    message: Optional[Dict[str, str]] = Field(
        default=None, description="The message of the fine-tuning process."
    )
    dataset_duration_seconds: Optional[float] = Field(
        default=None, description="The duration of the dataset in seconds."
    )
    verification_attempts: Optional[List[VerificationAttemptResponse]] = Field(
        default=None, description="The number of verification attempts."
    )
    slice_ids: Optional[List[str]] = Field(
        default=None, description="List of slice IDs."
    )
    manual_verification: Optional[ManualVerificationResponse] = Field(
        default=None, description="The manual verification of the fine-tuning process."
    )
    max_verification_attempts: Optional[int] = Field(
        default=None, description="The maximum number of verification attempts."
    )
    next_max_verification_attempts_reset_unix_ms: Optional[int] = Field(
        default=None,
        description="The next maximum verification attempts reset time in Unix milliseconds.",
    )
    finetuning_state: Optional[Any] = Field(default=None)
