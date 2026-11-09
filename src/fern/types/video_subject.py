from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class VideoSubject(BaseModel):
    """VideoSubject

    :param name: name
    :type name: str
    :param description: description
    :type description: str
    """

    name: str
    description: str
