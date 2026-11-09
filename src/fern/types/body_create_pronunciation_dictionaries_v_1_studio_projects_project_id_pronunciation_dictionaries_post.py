from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .pronunciation_dictionary_version_locator import (
    PronunciationDictionaryVersionLocator,
)


class BodyCreatePronunciationDictionariesV1StudioProjectsProjectIdPronunciationDictionariesPost(
    BaseModel
):
    """BodyCreatePronunciationDictionariesV1StudioProjectsProjectIdPronunciationDictionariesPost

    :param pronunciation_dictionary_locators: A list of pronunciation dictionary locators (pronunciation_dictionary_id, version_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"Vmd4Zor6fplcA7WrINey\\",\\"version_id\\":\\"hRPaxjlTdR7wFMhV4w0b\\"}"' --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"JzWtcGQMJ6bnlWwyMo7e\\",\\"version_id\\":\\"lbmwxiLu4q6txYxgdZqn\\"}"'.
    :type pronunciation_dictionary_locators: List[PronunciationDictionaryVersionLocator]
    :param invalidate_affected_text: This will automatically mark text in this project for reconversion when the new dictionary applies or the old one no longer does., defaults to None
    :type invalidate_affected_text: bool, optional
    """

    pronunciation_dictionary_locators: List[PronunciationDictionaryVersionLocator] = (
        Field(
            description='A list of pronunciation dictionary locators (pronunciation_dictionary_id, version_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form \'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"Vmd4Zor6fplcA7WrINey\\",\\"version_id\\":\\"hRPaxjlTdR7wFMhV4w0b\\"}"\' --form \'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"JzWtcGQMJ6bnlWwyMo7e\\",\\"version_id\\":\\"lbmwxiLu4q6txYxgdZqn\\"}"\'.'
        )
    )
    invalidate_affected_text: Optional[bool] = Field(
        default=None,
        description="This will automatically mark text in this project for reconversion when the new dictionary applies or the old one no longer does.",
    )
