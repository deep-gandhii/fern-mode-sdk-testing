from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DubbingRenderResponseModel(BaseModel):
    """DubbingRenderResponseModel

    :param version: version
    :type version: int
    :param render_id: render_id
    :type render_id: str
    """

    version: int
    render_id: str
