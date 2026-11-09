from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .voice_settings import VoiceSettings
from .pronunciation_dictionary_version_locator import (
    PronunciationDictionaryVersionLocator,
)

BodyTextToSpeechFullWithTimestampsApplyTextNormalization = typing.Union[
    typing.Literal["auto", "on", "off"], typing.Any
]


class BodyTextToSpeechFullWithTimestamps(BaseModel):
    """BodyTextToSpeechFullWithTimestamps

    :param text: The text that will get converted into speech.
    :type text: str
    :param model_id: Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property., defaults to None
    :type model_id: str, optional
    :param language_code: Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models., defaults to None
    :type language_code: str, optional
    :param voice_settings: Voice settings overriding stored settings for the given voice. They are applied only on the given request., defaults to None
    :type voice_settings: VoiceSettings, optional
    :param pronunciation_dictionary_locators: A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request, defaults to None
    :type pronunciation_dictionary_locators: List[PronunciationDictionaryVersionLocator], optional
    :param seed: If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295., defaults to None
    :type seed: int, optional
    :param previous_text: The text that came before the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation., defaults to None
    :type previous_text: str, optional
    :param next_text: The text that comes after the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation., defaults to None
    :type next_text: str, optional
    :param previous_request_ids: A list of request_id of the samples that were generated before this generation. Can be used to improve the speech's continuity when splitting up a large task into multiple requests. The results will be best when the same model is used across the generations. In case both previous_text and previous_request_ids is send, previous_text will be ignored. A maximum of 3 request_ids can be send., defaults to None
    :type previous_request_ids: List[str], optional
    :param next_request_ids: A list of request_id of the samples that come after this generation. next_request_ids is especially useful for maintaining the speech's continuity when regenerating a sample that has had some audio quality issues. For example, if you have generated 3 speech clips, and you want to improve clip 2, passing the request id of clip 3 as a next_request_id (and that of clip 1 as a previous_request_id) will help maintain natural flow in the combined speech. The results will be best when the same model is used across the generations. In case both next_text and next_request_ids is send, next_text will be ignored. A maximum of 3 request_ids can be send., defaults to None
    :type next_request_ids: List[str], optional
    :param use_pvc_as_ivc: If true, we won't use PVC version of the voice for the generation but the IVC version. This is a temporary workaround for higher latency in PVC versions., defaults to None
    :type use_pvc_as_ivc: bool, optional
    :param apply_text_normalization: This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped., defaults to None
    :type apply_text_normalization: BodyTextToSpeechFullWithTimestampsApplyTextNormalization, optional
    :param apply_language_text_normalization: This parameter controls language text normalization. This helps with proper pronunciation of text in some supported languages. WARNING: This parameter can heavily increase the latency of the request. Currently only supported for Japanese., defaults to None
    :type apply_language_text_normalization: bool, optional
    """

    text: str = Field(description="The text that will get converted into speech.")
    model_id: Optional[str] = Field(
        default=None,
        description="Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.",
    )
    language_code: Optional[str] = Field(
        default=None,
        description="Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.",
    )
    voice_settings: Optional[VoiceSettings] = Field(
        default=None,
        description="Voice settings overriding stored settings for the given voice. They are applied only on the given request.",
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
    previous_text: Optional[str] = Field(
        default=None,
        description="The text that came before the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.",
    )
    next_text: Optional[str] = Field(
        default=None,
        description="The text that comes after the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation.",
    )
    previous_request_ids: Optional[List[str]] = Field(
        default=None,
        description="A list of request_id of the samples that were generated before this generation. Can be used to improve the speech's continuity when splitting up a large task into multiple requests. The results will be best when the same model is used across the generations. In case both previous_text and previous_request_ids is send, previous_text will be ignored. A maximum of 3 request_ids can be send.",
    )
    next_request_ids: Optional[List[str]] = Field(
        default=None,
        description="A list of request_id of the samples that come after this generation. next_request_ids is especially useful for maintaining the speech's continuity when regenerating a sample that has had some audio quality issues. For example, if you have generated 3 speech clips, and you want to improve clip 2, passing the request id of clip 3 as a next_request_id (and that of clip 1 as a previous_request_id) will help maintain natural flow in the combined speech. The results will be best when the same model is used across the generations. In case both next_text and next_request_ids is send, next_text will be ignored. A maximum of 3 request_ids can be send.",
    )
    use_pvc_as_ivc: Optional[bool] = Field(
        default=None,
        description="If true, we won't use PVC version of the voice for the generation but the IVC version. This is a temporary workaround for higher latency in PVC versions.",
    )
    apply_text_normalization: Optional[
        BodyTextToSpeechFullWithTimestampsApplyTextNormalization
    ] = Field(
        default=None,
        description="This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.",
    )
    apply_language_text_normalization: Optional[bool] = Field(
        default=None,
        description="This parameter controls language text normalization. This helps with proper pronunciation of text in some supported languages. WARNING: This parameter can heavily increase the latency of the request. Currently only supported for Japanese.",
    )
