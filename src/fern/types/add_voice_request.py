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

# Union type for AddVoiceRequestLabels
# Pydantic will attempt to validate against each type in order
AddVoiceRequestLabels = Union[Dict[str, str], str]
# TypeAdapter for runtime validation of AddVoiceRequestLabels
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AddVoiceRequestLabels_adapter = TypeAdapter(AddVoiceRequestLabels)


class AddVoiceRequest(BaseModel):
    """AddVoiceRequest

    :param name: The name that identifies this voice. This will be displayed in the dropdown of the website.
    :type name: str
    :param files: A list of file paths to audio recordings intended for voice cloning.
    :type files: List[bytes]
    :param remove_background_noise: If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse., defaults to None
    :type remove_background_noise: bool, optional
    :param description: A description of the voice., defaults to None
    :type description: str, optional
    :param labels: Labels for the voice. Keys can be language, accent, gender, or age., defaults to None
    :type labels: AddVoiceRequestLabels, optional
    """

    name: str = Field(
        description="The name that identifies this voice. This will be displayed in the dropdown of the website."
    )
    files: List[bytes] = Field(
        description="A list of file paths to audio recordings intended for voice cloning."
    )
    remove_background_noise: Optional[bool] = Field(
        default=None,
        description="If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.",
    )
    description: Optional[str] = Field(
        default=None, description="A description of the voice."
    )
    labels: Optional[AddVoiceRequestLabels] = Field(
        default=None,
        description="Labels for the voice. Keys can be language, accent, gender, or age.",
    )
