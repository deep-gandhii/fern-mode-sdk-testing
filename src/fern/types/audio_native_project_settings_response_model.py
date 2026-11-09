from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

AudioNativeProjectSettingsResponseModelStatus = typing.Union[
    typing.Literal["processing", "ready"], typing.Any
]


class AudioNativeProjectSettingsResponseModel(BaseModel):
    """AudioNativeProjectSettingsResponseModel

    :param title: The title of the project.
    :type title: str
    :param image: The image of the project.
    :type image: str
    :param author: The author of the project.
    :type author: str
    :param small: Whether the project is small.
    :type small: bool
    :param text_color: The text color of the project.
    :type text_color: str
    :param background_color: The background color of the project.
    :type background_color: str
    :param sessionization: The sessionization of the project. Specifies for how many minutes to persist the session across page reloads.
    :type sessionization: int
    :param audio_path: The path of the audio file., defaults to None
    :type audio_path: str, optional
    :param audio_url: The URL of the audio file., defaults to None
    :type audio_url: str, optional
    :param status: Current state of the project, defaults to None
    :type status: AudioNativeProjectSettingsResponseModelStatus, optional
    """

    title: str = Field(description="The title of the project.")
    image: str = Field(description="The image of the project.")
    author: str = Field(description="The author of the project.")
    small: bool = Field(description="Whether the project is small.")
    text_color: str = Field(description="The text color of the project.")
    background_color: str = Field(description="The background color of the project.")
    sessionization: int = Field(
        description="The sessionization of the project. Specifies for how many minutes to persist the session across page reloads."
    )
    audio_path: Optional[str] = Field(
        default=None, description="The path of the audio file."
    )
    audio_url: Optional[str] = Field(
        default=None, description="The URL of the audio file."
    )
    status: Optional[AudioNativeProjectSettingsResponseModelStatus] = Field(
        default=None, description="Current state of the project"
    )
