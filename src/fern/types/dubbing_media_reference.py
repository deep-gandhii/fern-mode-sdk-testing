from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DubbingMediaReference(BaseModel):
    """DubbingMediaReference

    :param src: src
    :type src: str
    :param content_type: content_type
    :type content_type: str
    :param bucket_name: bucket_name
    :type bucket_name: str
    :param random_path_slug: random_path_slug
    :type random_path_slug: str
    :param duration_secs: duration_secs
    :type duration_secs: float
    :param is_audio: is_audio
    :type is_audio: bool
    :param url: url
    :type url: str
    """

    src: str
    content_type: str
    bucket_name: str
    random_path_slug: str
    duration_secs: float
    is_audio: bool
    url: str
