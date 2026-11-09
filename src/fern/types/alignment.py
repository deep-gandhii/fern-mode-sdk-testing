from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class Alignment(BaseModel):
    """Alignment information for the generated audio given the input text sequence.

    :param char_start_times_ms: A list of starting times (in milliseconds) for each character in the text as it corresponds to the audio. For instance, the character 'H' starts at time 0 ms in the audio. Note these times are relative to the returned chunk from the model, and not the full audio response., defaults to None
    :type char_start_times_ms: List[int], optional
    :param char_durations_ms: A list of durations (in milliseconds) for each character in the text as it corresponds to the audio. For instance, the character 'H' lasts for 3 ms in the audio. Note these times are relative to the returned chunk from the model, and not the full audio response., defaults to None
    :type char_durations_ms: List[int], optional
    :param chars: A list of characters in the text sequence. For instance, the first character is 'H'. Note that this list may contain spaces, punctuation, and other special characters. The length of this list should be the same as the lengths of `charStartTimesMs` and `charDurationsMs`., defaults to None
    :type chars: List[str], optional
    """

    char_start_times_ms: Optional[List[int]] = Field(
        alias="charStartTimesMs",
        serialization_alias="charStartTimesMs",
        default=None,
        description="A list of starting times (in milliseconds) for each character in the text as it corresponds to the audio. For instance, the character 'H' starts at time 0 ms in the audio. Note these times are relative to the returned chunk from the model, and not the full audio response.",
    )
    char_durations_ms: Optional[List[int]] = Field(
        alias="charDurationsMs",
        serialization_alias="charDurationsMs",
        default=None,
        description="A list of durations (in milliseconds) for each character in the text as it corresponds to the audio. For instance, the character 'H' lasts for 3 ms in the audio. Note these times are relative to the returned chunk from the model, and not the full audio response.",
    )
    chars: Optional[List[str]] = Field(
        default=None,
        description="A list of characters in the text sequence. For instance, the first character is 'H'. Note that this list may contain spaces, punctuation, and other special characters. The length of this list should be the same as the lengths of `charStartTimesMs` and `charDurationsMs`.",
    )
