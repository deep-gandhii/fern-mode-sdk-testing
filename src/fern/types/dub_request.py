from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

DubRequestMode = typing.Union[typing.Literal["automatic", "manual"], typing.Any]


class DubRequest(BaseModel):
    """DubRequest

    :param file: A list of file paths to audio recordings intended for voice cloning, defaults to None
    :type file: bytes, optional
    :param csv_file: CSV file containing transcription/translation metadata, defaults to None
    :type csv_file: bytes, optional
    :param foreground_audio_file: For use only with csv input, defaults to None
    :type foreground_audio_file: bytes, optional
    :param background_audio_file: For use only with csv input, defaults to None
    :type background_audio_file: bytes, optional
    :param name: Name of the dubbing project., defaults to None
    :type name: str, optional
    :param source_url: URL of the source video/audio file., defaults to None
    :type source_url: str, optional
    :param source_lang: Source language. Expects a valid iso639-1 or iso639-3 language code., defaults to None
    :type source_lang: str, optional
    :param target_lang: The Target language to dub the content into. Expects a valid iso639-1 or iso639-3 language code.
    :type target_lang: str
    :param target_accent: [Experimental] An accent to apply when selecting voices from the library and to use to inform translation of the dialect to prefer., defaults to None
    :type target_accent: str, optional
    :param num_speakers: Number of speakers to use for the dubbing. Set to 0 to automatically detect the number of speakers, defaults to None
    :type num_speakers: int, optional
    :param watermark: Whether to apply watermark to the output video., defaults to None
    :type watermark: bool, optional
    :param start_time: Start time of the source video/audio file., defaults to None
    :type start_time: int, optional
    :param end_time: End time of the source video/audio file., defaults to None
    :type end_time: int, optional
    :param highest_resolution: Whether to use the highest resolution available., defaults to None
    :type highest_resolution: bool, optional
    :param drop_background_audio: An advanced setting. Whether to drop background audio from the final dub. This can improve dub quality where it's known that audio shouldn't have a background track such as for speeches or monologues., defaults to None
    :type drop_background_audio: bool, optional
    :param use_profanity_filter: [BETA] Whether transcripts should have profanities censored with the words '[censored]', defaults to None
    :type use_profanity_filter: bool, optional
    :param dubbing_studio: Whether to prepare dub for edits in dubbing studio or edits as a dubbing resource., defaults to None
    :type dubbing_studio: bool, optional
    :param disable_voice_cloning: Instead of using a voice clone in dubbing, use a similar voice from the ElevenLabs Voice Library. Voices used from the library will contribute towards a workspace's custom voices limit, and if there aren't enough available slots the dub will fail. Using this feature requires the caller to have the 'add_voice_from_voice_library' permission on their workspace to access new voices., defaults to None
    :type disable_voice_cloning: bool, optional
    :param mode: The mode in which to run this Dubbing job. Defaults to automatic, use manual if specifically providing a CSV transcript to use. Note that manual mode is experimental and production use is strongly discouraged., defaults to None
    :type mode: DubRequestMode, optional
    :param csv_fps: Frames per second to use when parsing a CSV file for dubbing. If not provided, FPS will be inferred from timecodes., defaults to None
    :type csv_fps: float, optional
    """

    file: Optional[bytes] = Field(
        default=None,
        description="A list of file paths to audio recordings intended for voice cloning",
    )
    csv_file: Optional[bytes] = Field(
        default=None,
        description="CSV file containing transcription/translation metadata",
    )
    foreground_audio_file: Optional[bytes] = Field(
        default=None, description="For use only with csv input"
    )
    background_audio_file: Optional[bytes] = Field(
        default=None, description="For use only with csv input"
    )
    name: Optional[str] = Field(
        default=None, description="Name of the dubbing project."
    )
    source_url: Optional[str] = Field(
        default=None, description="URL of the source video/audio file."
    )
    source_lang: Optional[str] = Field(
        default=None,
        description="Source language. Expects a valid iso639-1 or iso639-3 language code.",
    )
    target_lang: Optional[str] = Field(
        description="The Target language to dub the content into. Expects a valid iso639-1 or iso639-3 language code."
    )
    target_accent: Optional[str] = Field(
        default=None,
        description="[Experimental] An accent to apply when selecting voices from the library and to use to inform translation of the dialect to prefer.",
    )
    num_speakers: Optional[int] = Field(
        default=None,
        description="Number of speakers to use for the dubbing. Set to 0 to automatically detect the number of speakers",
    )
    watermark: Optional[bool] = Field(
        default=None, description="Whether to apply watermark to the output video."
    )
    start_time: Optional[int] = Field(
        default=None, description="Start time of the source video/audio file."
    )
    end_time: Optional[int] = Field(
        default=None, description="End time of the source video/audio file."
    )
    highest_resolution: Optional[bool] = Field(
        default=None, description="Whether to use the highest resolution available."
    )
    drop_background_audio: Optional[bool] = Field(
        default=None,
        description="An advanced setting. Whether to drop background audio from the final dub. This can improve dub quality where it's known that audio shouldn't have a background track such as for speeches or monologues.",
    )
    use_profanity_filter: Optional[bool] = Field(
        default=None,
        description="[BETA] Whether transcripts should have profanities censored with the words '[censored]'",
    )
    dubbing_studio: Optional[bool] = Field(
        default=None,
        description="Whether to prepare dub for edits in dubbing studio or edits as a dubbing resource.",
    )
    disable_voice_cloning: Optional[bool] = Field(
        default=None,
        description="Instead of using a voice clone in dubbing, use a similar voice from the ElevenLabs Voice Library. Voices used from the library will contribute towards a workspace's custom voices limit, and if there aren't enough available slots the dub will fail. Using this feature requires the caller to have the 'add_voice_from_voice_library' permission on their workspace to access new voices.",
    )
    mode: Optional[DubRequestMode] = Field(
        default=None,
        description="The mode in which to run this Dubbing job. Defaults to automatic, use manual if specifically providing a CSV transcript to use. Note that manual mode is experimental and production use is strongly discouraged.",
    )
    csv_fps: Optional[float] = Field(
        default=None,
        description="Frames per second to use when parsing a CSV file for dubbing. If not provided, FPS will be inferred from timecodes.",
    )
