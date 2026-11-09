from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .conv_ai_secret_locator import ConvAiSecretLocator
from .conv_ai_dynamic_variable import ConvAiDynamicVariable

# Union type for SpeechEngineConfigRequestHeadersValue
# Pydantic will attempt to validate against each type in order
SpeechEngineConfigRequestHeadersValue = Union[
    str, ConvAiSecretLocator, ConvAiDynamicVariable
]
# TypeAdapter for runtime validation of SpeechEngineConfigRequestHeadersValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

SpeechEngineConfigRequestHeadersValue_adapter = TypeAdapter(
    SpeechEngineConfigRequestHeadersValue
)


class SpeechEngineConfig(BaseModel):
    """SpeechEngineConfig

    :param ws_url: The WebSocket URL for the transcript server
    :type ws_url: str
    :param request_headers: Headers to include in the WebSocket connection request, defaults to None
    :type request_headers: Dict[str, SpeechEngineConfigRequestHeadersValue], optional
    """

    ws_url: str = Field(description="The WebSocket URL for the transcript server")
    request_headers: Optional[Dict[str, SpeechEngineConfigRequestHeadersValue]] = Field(
        default=None,
        description="Headers to include in the WebSocket connection request",
    )
