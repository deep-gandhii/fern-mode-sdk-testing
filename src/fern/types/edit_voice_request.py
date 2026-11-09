from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel

# Union type for EditVoiceRequestLabels
# Pydantic will attempt to validate against each type in order
EditVoiceRequestLabels = Union[Dict[str, str], str]
# TypeAdapter for runtime validation of EditVoiceRequestLabels
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

EditVoiceRequestLabels_adapter = TypeAdapter(EditVoiceRequestLabels)


class EditVoiceRequest(BaseModel):
    """EditVoiceRequest

    :param name: The name that identifies this voice. This will be displayed in the dropdown of the website.
    :type name: str
    :param files: Audio files to add to the voice, defaults to None
    :type files: List[bytes], optional
    :param remove_background_noise: If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse., defaults to None
    :type remove_background_noise: bool, optional
    :param description: A description of the voice., defaults to None
    :type description: str, optional
    :param labels: Labels for the voice. Keys can be language, accent, gender, or age., defaults to None
    :type labels: EditVoiceRequestLabels, optional
    :param moderate_metadata: Run synchronous LLM moderation over the voice name and description when they change. Has no effect unless the voice_library_metadata_moderation feature flag is enabled for the user., defaults to None
    :type moderate_metadata: bool, optional
    """

    name: str = Field(
        description="The name that identifies this voice. This will be displayed in the dropdown of the website."
    )
    files: Optional[List[bytes]] = Field(
        default=None, description="Audio files to add to the voice"
    )
    remove_background_noise: Optional[bool] = Field(
        default=None,
        description="If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.",
    )
    description: Optional[str] = Field(
        default=None, description="A description of the voice."
    )
    labels: Optional[EditVoiceRequestLabels] = Field(
        default=None,
        description="Labels for the voice. Keys can be language, accent, gender, or age.",
    )
    moderate_metadata: Optional[bool] = Field(
        default=None,
        description="Run synchronous LLM moderation over the voice name and description when they change. Has no effect unless the voice_library_metadata_moderation feature flag is enabled for the user.",
    )
