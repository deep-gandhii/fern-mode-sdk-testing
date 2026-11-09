from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

BodyCreatesAudioNativeEnabledProjectV1AudioNativePostApplyTextNormalization = (
    typing.Union[typing.Literal["auto", "on", "off", "apply_english"], typing.Any]
)


class BodyCreatesAudioNativeEnabledProjectV1AudioNativePost(BaseModel):
    """BodyCreatesAudioNativeEnabledProjectV1AudioNativePost

    :param name: Project name.
    :type name: str
    :param image: (Deprecated) Image URL used in the player. If not provided, default image set in the Player settings is used., defaults to None
    :type image: str, optional
    :param author: Author used in the player and inserted at the start of the uploaded article. If not provided, the default author set in the Player settings is used., defaults to None
    :type author: str, optional
    :param title: Title used in the player and inserted at the top of the uploaded article. If not provided, the default title set in the Player settings is used., defaults to None
    :type title: str, optional
    :param small: (Deprecated) Whether to use small player or not. If not provided, default value set in the Player settings is used., defaults to None
    :type small: bool, optional
    :param text_color: Text color used in the player. If not provided, default text color set in the Player settings is used., defaults to None
    :type text_color: str, optional
    :param background_color: Background color used in the player. If not provided, default background color set in the Player settings is used., defaults to None
    :type background_color: str, optional
    :param sessionization: (Deprecated) Specifies for how many minutes to persist the session across page reloads. If not provided, default sessionization set in the Player settings is used., defaults to None
    :type sessionization: int, optional
    :param voice_id: Voice ID used to voice the content. If not provided, default voice ID set in the Player settings is used., defaults to None
    :type voice_id: str, optional
    :param model_id: TTS Model ID used in the player. If not provided, default model ID set in the Player settings is used., defaults to None
    :type model_id: str, optional
    :param file: Either txt or HTML input file containing the article content. HTML should be formatted as follows '&lt;html&gt;&lt;body&gt;&lt;div&gt;&lt;p&gt;Your content&lt;/p&gt;&lt;h3&gt;More of your content&lt;/h3&gt;&lt;p&gt;Some more of your content&lt;/p&gt;&lt;/div&gt;&lt;/body&gt;&lt;/html&gt;', defaults to None
    :type file: bytes, optional
    :param auto_convert: Whether to auto convert the project to audio or not., defaults to None
    :type auto_convert: bool, optional
    :param apply_text_normalization: This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English., defaults to None
    :type apply_text_normalization: BodyCreatesAudioNativeEnabledProjectV1AudioNativePostApplyTextNormalization, optional
    :param pronunciation_dictionary_locators: A list of pronunciation dictionary locators (pronunciation_dictionary_id, version_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"Vmd4Zor6fplcA7WrINey\\",\\"version_id\\":\\"hRPaxjlTdR7wFMhV4w0b\\"}"' --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"JzWtcGQMJ6bnlWwyMo7e\\",\\"version_id\\":\\"lbmwxiLu4q6txYxgdZqn\\"}"'., defaults to None
    :type pronunciation_dictionary_locators: List[str], optional
    """

    name: str = Field(description="Project name.")
    image: Optional[str] = Field(
        default=None,
        description="(Deprecated) Image URL used in the player. If not provided, default image set in the Player settings is used.",
    )
    author: Optional[str] = Field(
        default=None,
        description="Author used in the player and inserted at the start of the uploaded article. If not provided, the default author set in the Player settings is used.",
    )
    title: Optional[str] = Field(
        default=None,
        description="Title used in the player and inserted at the top of the uploaded article. If not provided, the default title set in the Player settings is used.",
    )
    small: Optional[bool] = Field(
        default=None,
        description="(Deprecated) Whether to use small player or not. If not provided, default value set in the Player settings is used.",
    )
    text_color: Optional[str] = Field(
        default=None,
        description="Text color used in the player. If not provided, default text color set in the Player settings is used.",
    )
    background_color: Optional[str] = Field(
        default=None,
        description="Background color used in the player. If not provided, default background color set in the Player settings is used.",
    )
    sessionization: Optional[int] = Field(
        default=None,
        description="(Deprecated) Specifies for how many minutes to persist the session across page reloads. If not provided, default sessionization set in the Player settings is used.",
    )
    voice_id: Optional[str] = Field(
        default=None,
        description="Voice ID used to voice the content. If not provided, default voice ID set in the Player settings is used.",
    )
    model_id: Optional[str] = Field(
        default=None,
        description="TTS Model ID used in the player. If not provided, default model ID set in the Player settings is used.",
    )
    file: Optional[bytes] = Field(
        default=None,
        description="Either txt or HTML input file containing the article content. HTML should be formatted as follows '&lt;html&gt;&lt;body&gt;&lt;div&gt;&lt;p&gt;Your content&lt;/p&gt;&lt;h3&gt;More of your content&lt;/h3&gt;&lt;p&gt;Some more of your content&lt;/p&gt;&lt;/div&gt;&lt;/body&gt;&lt;/html&gt;'",
    )
    auto_convert: Optional[bool] = Field(
        default=None, description="Whether to auto convert the project to audio or not."
    )
    apply_text_normalization: Optional[
        BodyCreatesAudioNativeEnabledProjectV1AudioNativePostApplyTextNormalization
    ] = Field(
        default=None,
        description="This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English.",
    )
    pronunciation_dictionary_locators: Optional[List[str]] = Field(
        default=None,
        description='A list of pronunciation dictionary locators (pronunciation_dictionary_id, version_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form \'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"Vmd4Zor6fplcA7WrINey\\",\\"version_id\\":\\"hRPaxjlTdR7wFMhV4w0b\\"}"\' --form \'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"JzWtcGQMJ6bnlWwyMo7e\\",\\"version_id\\":\\"lbmwxiLu4q6txYxgdZqn\\"}"\'.',
    )
