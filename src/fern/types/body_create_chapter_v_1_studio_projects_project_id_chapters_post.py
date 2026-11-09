from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyCreateChapterV1StudioProjectsProjectIdChaptersPost(BaseModel):
    """BodyCreateChapterV1StudioProjectsProjectIdChaptersPost

    :param name: The name of the chapter, used for identification only.
    :type name: str
    :param from_url: An optional URL from which we will extract content to initialize the Studio project. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank., defaults to None
    :type from_url: str, optional
    """

    name: str = Field(
        description="The name of the chapter, used for identification only."
    )
    from_url: Optional[str] = Field(
        default=None,
        description="An optional URL from which we will extract content to initialize the Studio project. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.",
    )
