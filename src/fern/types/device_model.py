from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class DeviceModel(BaseModel):
    """Device information. Spec: https://schema.ocsf.io/1.6.0/objects/device

    :param ip: IP address, defaults to None
    :type ip: str, optional
    :param hostname: Device hostname, defaults to None
    :type hostname: str, optional
    :param type_id: Device type ID (99 = Unknown), defaults to None
    :type type_id: int, optional
    """

    ip: Optional[str] = Field(default=None, description="IP address")
    hostname: Optional[str] = Field(default=None, description="Device hostname")
    type_id: Optional[int] = Field(
        default=None, description="Device type ID (99 = Unknown)"
    )
