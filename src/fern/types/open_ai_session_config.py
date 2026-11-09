from __future__ import annotations
import typing
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .open_ai_audio_config import OpenAiAudioConfig
from .open_ai_function_tool import OpenAiFunctionTool
from .open_aimcp_tool import OpenAimcpTool
from .open_ai_tool_choice_function import OpenAiToolChoiceFunction

OpenAiSessionConfigType = typing.Union[typing.Literal["realtime"], typing.Any]


# fernMode variant type for a shared-component member of OpenAiSessionConfigToolsItem
class OpenAiSessionConfigToolsItem_Function(OpenAiFunctionTool):
    pass


# fernMode variant type for a shared-component member of OpenAiSessionConfigToolsItem
class OpenAiSessionConfigToolsItem_Mcp(OpenAimcpTool):
    pass


# Union type for OpenAiSessionConfigToolsItem
# Pydantic will attempt to validate against each type in order
OpenAiSessionConfigToolsItem = Union[OpenAiFunctionTool, OpenAimcpTool]
# TypeAdapter for runtime validation of OpenAiSessionConfigToolsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

OpenAiSessionConfigToolsItem_adapter = TypeAdapter(OpenAiSessionConfigToolsItem)


# Union type for OpenAiSessionConfigToolChoice
# Pydantic will attempt to validate against each type in order
OpenAiSessionConfigToolChoice = Union[str, OpenAiToolChoiceFunction]
# TypeAdapter for runtime validation of OpenAiSessionConfigToolChoice
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

OpenAiSessionConfigToolChoice_adapter = TypeAdapter(OpenAiSessionConfigToolChoice)


MaxResponseOutputTokensOne = typing.Union[typing.Literal["inf"], typing.Any]


# Union type for OpenAiSessionConfigMaxResponseOutputTokens
# Pydantic will attempt to validate against each type in order
OpenAiSessionConfigMaxResponseOutputTokens = Union[int, str]
# TypeAdapter for runtime validation of OpenAiSessionConfigMaxResponseOutputTokens
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

OpenAiSessionConfigMaxResponseOutputTokens_adapter = TypeAdapter(
    OpenAiSessionConfigMaxResponseOutputTokens
)


class OpenAiSessionConfig(BaseModel):
    """OpenAiSessionConfig

    :param type: type, defaults to None
    :type type: OpenAiSessionConfigType, optional
    :param model: model, defaults to None
    :type model: str, optional
    :param instructions: instructions, defaults to None
    :type instructions: str, optional
    :param modalities: modalities, defaults to None
    :type modalities: List[str], optional
    :param audio: audio, defaults to None
    :type audio: OpenAiAudioConfig, optional
    :param tools: tools, defaults to None
    :type tools: List[OpenAiSessionConfigToolsItem], optional
    :param tool_choice: tool_choice, defaults to None
    :type tool_choice: OpenAiSessionConfigToolChoice, optional
    :param temperature: temperature, defaults to None
    :type temperature: float, optional
    :param max_response_output_tokens: max_response_output_tokens, defaults to None
    :type max_response_output_tokens: OpenAiSessionConfigMaxResponseOutputTokens, optional
    :param output_modalities: output_modalities, defaults to None
    :type output_modalities: List[str], optional
    """

    type: Optional[OpenAiSessionConfigType] = Field(default=None)
    model: Optional[str] = Field(default=None)
    instructions: Optional[str] = Field(default=None)
    modalities: Optional[List[str]] = Field(default=None)
    audio: Optional[OpenAiAudioConfig] = Field(default=None)
    tools: Optional[List[OpenAiSessionConfigToolsItem]] = Field(default=None)
    tool_choice: Optional[OpenAiSessionConfigToolChoice] = Field(default=None)
    temperature: Optional[float] = Field(default=None)
    max_response_output_tokens: Optional[OpenAiSessionConfigMaxResponseOutputTokens] = (
        Field(default=None)
    )
    output_modalities: Optional[List[str]] = Field(default=None)
