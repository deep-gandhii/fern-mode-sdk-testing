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
from .tool_interruption_mode import ToolInterruptionMode
from .pre_tool_speech_mode import PreToolSpeechMode
from .dynamic_variable_assignment import DynamicVariableAssignment
from .tool_call_sound_type import ToolCallSoundType
from .tool_call_sound_behavior import ToolCallSoundBehavior
from .tool_error_handling_mode import ToolErrorHandlingMode
from .end_call_tool_config import EndCallToolConfig
from .language_detection_tool_config import LanguageDetectionToolConfig
from .transfer_to_agent_tool_config_input import TransferToAgentToolConfigInput
from .transfer_to_number_tool_config_input import TransferToNumberToolConfigInput
from .skip_turn_tool_config import SkipTurnToolConfig
from .play_dtmf_tool_config import PlayDtmfToolConfig
from .voicemail_detection_tool_config import VoicemailDetectionToolConfig
from .knowledge_base_rag_tool_config import KnowledgeBaseRagToolConfig
from .knowledge_base_tool_config import KnowledgeBaseToolConfig
from .start_procedure_tool_config_input import StartProcedureToolConfigInput
from .end_procedure_tool_config_input import EndProcedureToolConfigInput
from .run_subagent_tool_config_input import RunSubagentToolConfigInput

SystemToolConfigInputType = typing.Union[typing.Literal["system"], typing.Any]


# fernMode variant type for a shared-component member of SystemToolConfigInputParams
class SystemToolConfigInputParams_EndCall(EndCallToolConfig):
    pass


# fernMode variant type for a shared-component member of SystemToolConfigInputParams
class SystemToolConfigInputParams_LanguageDetection(LanguageDetectionToolConfig):
    pass


# fernMode variant type for a shared-component member of SystemToolConfigInputParams
class SystemToolConfigInputParams_TransferToAgent(TransferToAgentToolConfigInput):
    pass


# fernMode variant type for a shared-component member of SystemToolConfigInputParams
class SystemToolConfigInputParams_TransferToNumber(TransferToNumberToolConfigInput):
    pass


# fernMode variant type for a shared-component member of SystemToolConfigInputParams
class SystemToolConfigInputParams_SkipTurn(SkipTurnToolConfig):
    pass


# fernMode variant type for a shared-component member of SystemToolConfigInputParams
class SystemToolConfigInputParams_PlayKeypadTouchTone(PlayDtmfToolConfig):
    pass


# fernMode variant type for a shared-component member of SystemToolConfigInputParams
class SystemToolConfigInputParams_VoicemailDetection(VoicemailDetectionToolConfig):
    pass


# fernMode variant type for a shared-component member of SystemToolConfigInputParams
class SystemToolConfigInputParams_KnowledgeBaseRag(KnowledgeBaseRagToolConfig):
    pass


# fernMode variant type for a shared-component member of SystemToolConfigInputParams
class SystemToolConfigInputParams_KnowledgeBase(KnowledgeBaseToolConfig):
    pass


# fernMode variant type for a shared-component member of SystemToolConfigInputParams
class SystemToolConfigInputParams_StartProcedure(StartProcedureToolConfigInput):
    pass


# fernMode variant type for a shared-component member of SystemToolConfigInputParams
class SystemToolConfigInputParams_EndProcedure(EndProcedureToolConfigInput):
    pass


# fernMode variant type for a shared-component member of SystemToolConfigInputParams
class SystemToolConfigInputParams_RunSubagent(RunSubagentToolConfigInput):
    pass


# Union type for SystemToolConfigInputParams
# Pydantic will attempt to validate against each type in order
SystemToolConfigInputParams = Union[
    EndCallToolConfig,
    LanguageDetectionToolConfig,
    TransferToAgentToolConfigInput,
    TransferToNumberToolConfigInput,
    SkipTurnToolConfig,
    PlayDtmfToolConfig,
    VoicemailDetectionToolConfig,
    KnowledgeBaseRagToolConfig,
    KnowledgeBaseToolConfig,
    StartProcedureToolConfigInput,
    EndProcedureToolConfigInput,
    RunSubagentToolConfigInput,
]
# TypeAdapter for runtime validation of SystemToolConfigInputParams
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

SystemToolConfigInputParams_adapter = TypeAdapter(SystemToolConfigInputParams)


class SystemToolConfigInput(BaseModel):
    """A system tool is a tool that is used to call a system method in the server

    :param type: The type of tool, defaults to None
    :type type: SystemToolConfigInputType, optional
    :param name: name
    :type name: str
    :param description: Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type., defaults to None
    :type description: str, optional
    :param response_timeout_secs: The maximum time in seconds to wait for the tool call to complete., defaults to None
    :type response_timeout_secs: int, optional
    :param disable_interruptions: DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running., defaults to None
    :type disable_interruptions: bool, optional
    :param interruption_mode: interruption_mode, defaults to None
    :type interruption_mode: ToolInterruptionMode, optional
    :param force_pre_tool_speech: DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call., defaults to None
    :type force_pre_tool_speech: bool, optional
    :param pre_tool_speech: pre_tool_speech, defaults to None
    :type pre_tool_speech: PreToolSpeechMode, optional
    :param assignments: Configuration for extracting values from tool responses and assigning them to dynamic variables, defaults to None
    :type assignments: List[DynamicVariableAssignment], optional
    :param tool_call_sound: Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played., defaults to None
    :type tool_call_sound: ToolCallSoundType, optional
    :param tool_call_sound_behavior: Determines how the tool call sound should be played., defaults to None
    :type tool_call_sound_behavior: ToolCallSoundBehavior, optional
    :param tool_error_handling_mode: Controls how tool errors are processed before being shared with the agent., defaults to None
    :type tool_error_handling_mode: ToolErrorHandlingMode, optional
    :param params: params
    :type params: SystemToolConfigInputParams
    """

    type: Optional[SystemToolConfigInputType] = Field(
        default=None, description="The type of tool"
    )
    name: str
    description: Optional[str] = Field(
        default=None,
        description="Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.",
    )
    response_timeout_secs: Optional[int] = Field(
        default=None,
        description="The maximum time in seconds to wait for the tool call to complete.",
    )
    disable_interruptions: Optional[bool] = Field(
        default=None,
        description="DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.",
    )
    interruption_mode: Optional[ToolInterruptionMode] = Field(default=None)
    force_pre_tool_speech: Optional[bool] = Field(
        default=None,
        description="DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.",
    )
    pre_tool_speech: Optional[PreToolSpeechMode] = Field(default=None)
    assignments: Optional[List[DynamicVariableAssignment]] = Field(
        default=None,
        description="Configuration for extracting values from tool responses and assigning them to dynamic variables",
    )
    tool_call_sound: Optional[ToolCallSoundType] = Field(
        default=None,
        description="Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.",
    )
    tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = Field(
        default=None, description="Determines how the tool call sound should be played."
    )
    tool_error_handling_mode: Optional[ToolErrorHandlingMode] = Field(
        default=None,
        description="Controls how tool errors are processed before being shared with the agent.",
    )
    params: SystemToolConfigInputParams
