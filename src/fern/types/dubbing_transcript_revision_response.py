from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DubbingTranscriptRevisionResponse(BaseModel):
    """The new revision after a source edit that returns no segment (e.g. a delete).

    :param revision: The project's source-transcript revision after this edit.
    :type revision: int
    """

    revision: int = Field(
        description="The project's source-transcript revision after this edit."
    )
