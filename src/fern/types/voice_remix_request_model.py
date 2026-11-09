from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class VoiceRemixRequestModel(BaseModel):
    """VoiceRemixRequestModel

    :param voice_description: Description of the changes to make to the voice.
    :type voice_description: str
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
    :param remixing_session_id: The remixing session id., defaults to None
    :type remixing_session_id: str, optional
    :param remixing_session_iteration_id: The id of the remixing session iteration where these generations should be attached to. If not provided, a new iteration will be created., defaults to None
    :type remixing_session_iteration_id: str, optional
    :param prompt_strength: Controls the balance of prompt versus reference audio when generating voice samples. 0 means almost no prompt influence, 1 means almost no reference audio influence. Only supported when using the eleven_ttv_v3 model., defaults to None
    :type prompt_strength: float, optional
    """

    voice_description: str = Field(
        description="Description of the changes to make to the voice."
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
    remixing_session_id: Optional[str] = Field(
        default=None, description="The remixing session id."
    )
    remixing_session_iteration_id: Optional[str] = Field(
        default=None,
        description="The id of the remixing session iteration where these generations should be attached to. If not provided, a new iteration will be created.",
    )
    prompt_strength: Optional[float] = Field(
        default=None,
        description="Controls the balance of prompt versus reference audio when generating voice samples. 0 means almost no prompt influence, 1 means almost no reference audio influence. Only supported when using the eleven_ttv_v3 model.",
    )
