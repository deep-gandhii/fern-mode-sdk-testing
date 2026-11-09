from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .image_subject import ImageSubject


class ImageAnalysisResult(BaseModel):
    """ImageAnalysisResult

    :param title: title
    :type title: str
    :param description: description
    :type description: str
    :param content_type: content_type, defaults to None
    :type content_type: str, optional
    :param mood_and_style: mood_and_style, defaults to None
    :type mood_and_style: str, optional
    :param composition_notes: composition_notes, defaults to None
    :type composition_notes: str, optional
    :param visible_text: Readable text overlaid or shown in the image, if any., defaults to None
    :type visible_text: str, optional
    :param subjects: subjects, defaults to None
    :type subjects: List[ImageSubject], optional
    """

    title: str
    description: str
    content_type: Optional[str] = Field(default=None)
    mood_and_style: Optional[str] = Field(default=None)
    composition_notes: Optional[str] = Field(default=None)
    visible_text: Optional[str] = Field(
        default=None,
        description="Readable text overlaid or shown in the image, if any.",
    )
    subjects: Optional[List[ImageSubject]] = Field(default=None)
