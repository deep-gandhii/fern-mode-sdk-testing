from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .dialogue_input import DialogueInput
from .model_settings_response_model import ModelSettingsResponseModel
from .pronunciation_dictionary_version_locator import (
    PronunciationDictionaryVersionLocator,
)

BodyTextToDialogueFullWithTimestampsApplyTextNormalization = typing.Union[
    typing.Literal["auto", "on", "off"], typing.Any
]


class BodyTextToDialogueFullWithTimestamps(BaseModel):
    """BodyTextToDialogueFullWithTimestamps

    :param inputs: A list of dialogue inputs, each containing text and a voice ID which will be converted into speech. The maximum number of unique voice IDs is 10. For reliable generation, keep the total character count across all `inputs[].text` values at or below 2,000 characters per request. Longer requests can terminate early in streaming responses or return a validation error.
    :type inputs: List[DialogueInput]
    :param model_id: Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property., defaults to None
    :type model_id: str, optional
    :param language_code: Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models., defaults to None
    :type language_code: str, optional
    :param settings: Settings controlling the dialogue generation., defaults to None
    :type settings: ModelSettingsResponseModel, optional
    :param pronunciation_dictionary_locators: A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request, defaults to None
    :type pronunciation_dictionary_locators: List[PronunciationDictionaryVersionLocator], optional
    :param seed: If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295., defaults to None
    :type seed: int, optional
    :param apply_text_normalization: This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped., defaults to None
    :type apply_text_normalization: BodyTextToDialogueFullWithTimestampsApplyTextNormalization, optional
    """

    inputs: List[DialogueInput] = Field(
        description="A list of dialogue inputs, each containing text and a voice ID which will be converted into speech. The maximum number of unique voice IDs is 10. For reliable generation, keep the total character count across all `inputs[].text` values at or below 2,000 characters per request. Longer requests can terminate early in streaming responses or return a validation error."
    )
    model_id: Optional[str] = Field(
        default=None,
        description="Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.",
    )
    language_code: Optional[str] = Field(
        default=None,
        description="Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.",
    )
    settings: Optional[ModelSettingsResponseModel] = Field(
        default=None, description="Settings controlling the dialogue generation."
    )
    pronunciation_dictionary_locators: Optional[
        List[PronunciationDictionaryVersionLocator]
    ] = Field(
        default=None,
        description="A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request",
    )
    seed: Optional[int] = Field(
        default=None,
        description="If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.",
    )
    apply_text_normalization: Optional[
        BodyTextToDialogueFullWithTimestampsApplyTextNormalization
    ] = Field(
        default=None,
        description="This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.",
    )
