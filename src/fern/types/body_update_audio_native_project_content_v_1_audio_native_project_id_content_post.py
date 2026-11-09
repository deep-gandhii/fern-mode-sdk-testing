from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyUpdateAudioNativeProjectContentV1AudioNativeProjectIdContentPost(BaseModel):
    """BodyUpdateAudioNativeProjectContentV1AudioNativeProjectIdContentPost

    :param file: Either txt or HTML input file containing the article content. HTML should be formatted as follows '&lt;html&gt;&lt;body&gt;&lt;div&gt;&lt;p&gt;Your content&lt;/p&gt;&lt;h5&gt;More of your content&lt;/h5&gt;&lt;p&gt;Some more of your content&lt;/p&gt;&lt;/div&gt;&lt;/body&gt;&lt;/html&gt;', defaults to None
    :type file: bytes, optional
    :param auto_convert: Whether to auto convert the project to audio or not., defaults to None
    :type auto_convert: bool, optional
    :param auto_publish: Whether to auto publish the new project snapshot after it's converted., defaults to None
    :type auto_publish: bool, optional
    """

    file: Optional[bytes] = Field(
        default=None,
        description="Either txt or HTML input file containing the article content. HTML should be formatted as follows '&lt;html&gt;&lt;body&gt;&lt;div&gt;&lt;p&gt;Your content&lt;/p&gt;&lt;h5&gt;More of your content&lt;/h5&gt;&lt;p&gt;Some more of your content&lt;/p&gt;&lt;/div&gt;&lt;/body&gt;&lt;/html&gt;'",
    )
    auto_convert: Optional[bool] = Field(
        default=None, description="Whether to auto convert the project to audio or not."
    )
    auto_publish: Optional[bool] = Field(
        default=None,
        description="Whether to auto publish the new project snapshot after it's converted.",
    )
