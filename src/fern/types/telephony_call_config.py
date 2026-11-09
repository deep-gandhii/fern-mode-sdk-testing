from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class TelephonyCallConfig(BaseModel):
    """TelephonyCallConfig

    :param ringing_timeout_secs: How long to ring the recipient before giving up, in seconds. Note that this will also be limited by the provider's own constraints., defaults to None
    :type ringing_timeout_secs: int, optional
    :param twilio_call_recording_enabled: Whether to record the call using Twilio call recording. Ignored for non-Twilio providers. Recordings are stored in your Twilio account., defaults to None
    :type twilio_call_recording_enabled: bool, optional
    """

    ringing_timeout_secs: Optional[int] = Field(
        default=None,
        description="How long to ring the recipient before giving up, in seconds. Note that this will also be limited by the provider's own constraints.",
    )
    twilio_call_recording_enabled: Optional[bool] = Field(
        default=None,
        description="Whether to record the call using Twilio call recording. Ignored for non-Twilio providers. Recordings are stored in your Twilio account.",
    )
