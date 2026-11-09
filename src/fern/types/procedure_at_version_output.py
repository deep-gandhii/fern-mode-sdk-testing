from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .procedure_type import ProcedureType
from .custom_guardrail_config import CustomGuardrailConfig


class ProcedureAtVersionOutput(BaseModel):
    """ProcedureAtVersionOutput

    :param procedure_id: Procedure ID
    :type procedure_id: str
    :param name: Procedure name
    :type name: str
    :param type: type, defaults to None
    :type type: ProcedureType, optional
    :param trigger: When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it., defaults to None
    :type trigger: str, optional
    :param referenced_tool_ids: Tool IDs referenced in the procedure content, defaults to None
    :type referenced_tool_ids: List[str], optional
    :param referenced_kb_ids: Knowledge base IDs referenced in the procedure content, defaults to None
    :type referenced_kb_ids: List[str], optional
    :param referenced_procedure_ids: Procedure IDs referenced in the procedure content, defaults to None
    :type referenced_procedure_ids: List[str], optional
    :param referenced_dynamic_variables: Dynamic variable names used in the procedure content, defaults to None
    :type referenced_dynamic_variables: List[str], optional
    :param content: Procedure content
    :type content: str
    :param guardrails: guardrails, defaults to None
    :type guardrails: List[CustomGuardrailConfig], optional
    :param agent_id: Agent ID of the procedure
    :type agent_id: str
    :param version_id: Version ID of a version of the procedure. None for a procedure never versioned., defaults to None
    :type version_id: str, optional
    """

    procedure_id: str = Field(description="Procedure ID")
    name: str = Field(description="Procedure name")
    type: Optional[ProcedureType] = Field(default=None)
    trigger: Optional[str] = Field(
        default=None,
        description="When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it.",
    )
    referenced_tool_ids: Optional[List[str]] = Field(
        default=None, description="Tool IDs referenced in the procedure content"
    )
    referenced_kb_ids: Optional[List[str]] = Field(
        default=None,
        description="Knowledge base IDs referenced in the procedure content",
    )
    referenced_procedure_ids: Optional[List[str]] = Field(
        default=None, description="Procedure IDs referenced in the procedure content"
    )
    referenced_dynamic_variables: Optional[List[str]] = Field(
        default=None, description="Dynamic variable names used in the procedure content"
    )
    content: str = Field(description="Procedure content")
    guardrails: Optional[List[CustomGuardrailConfig]] = Field(default=None)
    agent_id: str = Field(description="Agent ID of the procedure")
    version_id: Optional[str] = Field(
        default=None,
        description="Version ID of a version of the procedure. None for a procedure never versioned.",
    )
