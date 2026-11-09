from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .guardrail_execution_mode import GuardrailExecutionMode
from .content_config import ContentConfig
from .end_call_trigger_action import EndCallTriggerAction
from .retry_trigger_action import RetryTriggerAction


# fernMode variant type for a shared-component member of ContentGuardrailInputTriggerAction
class ContentGuardrailInputTriggerAction_EndCall(EndCallTriggerAction):
    pass


# fernMode variant type for a shared-component member of ContentGuardrailInputTriggerAction
class ContentGuardrailInputTriggerAction_Retry(RetryTriggerAction):
    pass


# Union type for ContentGuardrailInputTriggerAction
# Pydantic will attempt to validate against each type in order
ContentGuardrailInputTriggerAction = Union[EndCallTriggerAction, RetryTriggerAction]
# TypeAdapter for runtime validation of ContentGuardrailInputTriggerAction
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ContentGuardrailInputTriggerAction_adapter = TypeAdapter(
    ContentGuardrailInputTriggerAction
)


class ContentGuardrailInput(BaseModel):
    """ContentGuardrailInput

    :param execution_mode: execution_mode, defaults to None
    :type execution_mode: GuardrailExecutionMode, optional
    :param config: config, defaults to None
    :type config: ContentConfig, optional
    :param trigger_action: trigger_action, defaults to None
    :type trigger_action: ContentGuardrailInputTriggerAction, optional
    """

    execution_mode: Optional[GuardrailExecutionMode] = Field(default=None)
    config: Optional[ContentConfig] = Field(default=None)
    trigger_action: Optional[ContentGuardrailInputTriggerAction] = Field(default=None)
