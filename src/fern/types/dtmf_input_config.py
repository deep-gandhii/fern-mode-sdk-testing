from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DtmfInputConfig(BaseModel):
    """Configuration for DTMF (keypad) input collection during phone calls.

    :param dtmf_input_timeout: Timeout in seconds to wait for additional DTMF digits, defaults to None
    :type dtmf_input_timeout: float, optional
    :param hash_terminator: If true, pressing # immediately completes DTMF input, defaults to None
    :type hash_terminator: bool, optional
    """

    dtmf_input_timeout: Optional[float] = Field(
        default=None,
        description="Timeout in seconds to wait for additional DTMF digits",
    )
    hash_terminator: Optional[bool] = Field(
        default=None, description="If true, pressing # immediately completes DTMF input"
    )
