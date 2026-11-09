from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class VoiceSharingModerationCheckResponseModel(BaseModel):
    """VoiceSharingModerationCheckResponseModel

    :param date_checked_unix: The date the moderation check was made in Unix time., defaults to None
    :type date_checked_unix: int, optional
    :param name_value: The name value of the voice., defaults to None
    :type name_value: str, optional
    :param name_check: Whether the name check was successful., defaults to None
    :type name_check: bool, optional
    :param description_value: The description value of the voice., defaults to None
    :type description_value: str, optional
    :param description_check: Whether the description check was successful., defaults to None
    :type description_check: bool, optional
    :param sample_ids: A list of sample IDs., defaults to None
    :type sample_ids: List[str], optional
    :param sample_checks: A list of sample checks., defaults to None
    :type sample_checks: List[float], optional
    :param captcha_ids: A list of captcha IDs., defaults to None
    :type captcha_ids: List[str], optional
    :param captcha_checks: A list of CAPTCHA check values., defaults to None
    :type captcha_checks: List[float], optional
    """

    date_checked_unix: Optional[int] = Field(
        default=None, description="The date the moderation check was made in Unix time."
    )
    name_value: Optional[str] = Field(
        default=None, description="The name value of the voice."
    )
    name_check: Optional[bool] = Field(
        default=None, description="Whether the name check was successful."
    )
    description_value: Optional[str] = Field(
        default=None, description="The description value of the voice."
    )
    description_check: Optional[bool] = Field(
        default=None, description="Whether the description check was successful."
    )
    sample_ids: Optional[List[str]] = Field(
        default=None, description="A list of sample IDs."
    )
    sample_checks: Optional[List[float]] = Field(
        default=None, description="A list of sample checks."
    )
    captcha_ids: Optional[List[str]] = Field(
        default=None, description="A list of captcha IDs."
    )
    captcha_checks: Optional[List[float]] = Field(
        default=None, description="A list of CAPTCHA check values."
    )
