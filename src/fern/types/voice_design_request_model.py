from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

VoiceDesignRequestModelModelId = typing.Union[
    typing.Literal["eleven_multilingual_ttv_v2", "eleven_ttv_v3"], typing.Any
]


class VoiceDesignRequestModel(BaseModel):
    """VoiceDesignRequestModel

    :param voice_description: Description to use for the created voice.
    :type voice_description: str
    :param model_id: Model to use for the voice generation. Possible values: eleven_multilingual_ttv_v2, eleven_ttv_v3., defaults to None
    :type model_id: VoiceDesignRequestModelModelId, optional
    :param text: Text to generate, text length has to be between 100 and 1000., defaults to None
    :type text: str, optional
    :param auto_generate_text: Whether to automatically generate a text suitable for the voice description., defaults to None
    :type auto_generate_text: bool, optional
    :param loudness: Controls the volume level of the generated voice. -1 is quietest, 1 is loudest, 0 corresponds to roughly -24 LUFS., defaults to None
    :type loudness: float, optional
    :param seed: Random number that controls the voice generation. Same seed with same inputs produces same voice., defaults to None
    :type seed: int, optional
    :param guidance_scale: Controls how closely the AI follows the prompt. Lower numbers give the AI more freedom to be creative, while higher numbers force it to stick more to the prompt. High numbers can cause voice to sound artificial or robotic. We recommend to use longer, more detailed prompts at lower Guidance Scale., defaults to None
    :type guidance_scale: float, optional
    :param stream_previews: Determines whether the Text to Voice previews should be included in the response. If true, only the generated IDs will be returned which can then be streamed via the /v1/text-to-voice/:generated_voice_id/stream endpoint., defaults to None
    :type stream_previews: bool, optional
    :param should_enhance: Whether to enhance the voice description using AI to add more detail and improve voice generation quality. When enabled, the system will automatically expand simple prompts into more detailed voice descriptions. Defaults to False, defaults to None
    :type should_enhance: bool, optional
    :param remixing_session_id: The remixing session id., defaults to None
    :type remixing_session_id: str, optional
    :param remixing_session_iteration_id: The id of the remixing session iteration where these generations should be attached to. If not provided, a new iteration will be created., defaults to None
    :type remixing_session_iteration_id: str, optional
    :param quality: Higher quality results in better voice output but less variety., defaults to None
    :type quality: float, optional
    :param reference_audio_base_64: Reference audio to use for the voice generation. The audio should be base64 encoded. Only supported when using the eleven_ttv_v3 model., defaults to None
    :type reference_audio_base_64: str, optional
    :param prompt_strength: Controls the balance of prompt versus reference audio when generating voice samples. 0 means almost no prompt influence, 1 means almost no reference audio influence. Only supported when using the eleven_ttv_v3 model., defaults to None
    :type prompt_strength: float, optional
    """

    voice_description: str = Field(
        description="Description to use for the created voice."
    )
    model_id: Optional[VoiceDesignRequestModelModelId] = Field(
        default=None,
        description="Model to use for the voice generation. Possible values: eleven_multilingual_ttv_v2, eleven_ttv_v3.",
    )
    text: Optional[str] = Field(
        default=None,
        description="Text to generate, text length has to be between 100 and 1000.",
    )
    auto_generate_text: Optional[bool] = Field(
        default=None,
        description="Whether to automatically generate a text suitable for the voice description.",
    )
    loudness: Optional[float] = Field(
        default=None,
        description="Controls the volume level of the generated voice. -1 is quietest, 1 is loudest, 0 corresponds to roughly -24 LUFS.",
    )
    seed: Optional[int] = Field(
        default=None,
        description="Random number that controls the voice generation. Same seed with same inputs produces same voice.",
    )
    guidance_scale: Optional[float] = Field(
        default=None,
        description="Controls how closely the AI follows the prompt. Lower numbers give the AI more freedom to be creative, while higher numbers force it to stick more to the prompt. High numbers can cause voice to sound artificial or robotic. We recommend to use longer, more detailed prompts at lower Guidance Scale.",
    )
    stream_previews: Optional[bool] = Field(
        default=None,
        description="Determines whether the Text to Voice previews should be included in the response. If true, only the generated IDs will be returned which can then be streamed via the /v1/text-to-voice/:generated_voice_id/stream endpoint.",
    )
    should_enhance: Optional[bool] = Field(
        default=None,
        description="Whether to enhance the voice description using AI to add more detail and improve voice generation quality. When enabled, the system will automatically expand simple prompts into more detailed voice descriptions. Defaults to False",
    )
    remixing_session_id: Optional[str] = Field(
        default=None, description="The remixing session id."
    )
    remixing_session_iteration_id: Optional[str] = Field(
        default=None,
        description="The id of the remixing session iteration where these generations should be attached to. If not provided, a new iteration will be created.",
    )
    quality: Optional[float] = Field(
        default=None,
        description="Higher quality results in better voice output but less variety.",
    )
    reference_audio_base_64: Optional[str] = Field(
        alias="reference_audio_base64",
        serialization_alias="reference_audio_base64",
        default=None,
        description="Reference audio to use for the voice generation. The audio should be base64 encoded. Only supported when using the eleven_ttv_v3 model.",
    )
    prompt_strength: Optional[float] = Field(
        default=None,
        description="Controls the balance of prompt versus reference audio when generating voice samples. 0 means almost no prompt influence, 1 means almost no reference audio influence. Only supported when using the eleven_ttv_v3 model.",
    )
