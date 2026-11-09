from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DynamicVariableAssignmentSource = typing.Union[typing.Literal["response"], typing.Any]


class DynamicVariableAssignment(BaseModel):
    """Configuration for extracting values from tool responses and assigning them to dynamic variables.

    :param source: The source to extract the value from. Currently only 'response' is supported., defaults to None
    :type source: DynamicVariableAssignmentSource, optional
    :param dynamic_variable: The name of the dynamic variable to assign the extracted value to
    :type dynamic_variable: str
    :param value_path: Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
    :type value_path: str
    :param sanitize: If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment., defaults to None
    :type sanitize: bool, optional
    :param preserve_native_type: If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables., defaults to None
    :type preserve_native_type: bool, optional
    """

    source: Optional[DynamicVariableAssignmentSource] = Field(
        default=None,
        description="The source to extract the value from. Currently only 'response' is supported.",
    )
    dynamic_variable: str = Field(
        description="The name of the dynamic variable to assign the extracted value to"
    )
    value_path: str = Field(
        description="Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')"
    )
    sanitize: Optional[bool] = Field(
        default=None,
        description="If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.",
    )
    preserve_native_type: Optional[bool] = Field(
        default=None,
        description="If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.",
    )
