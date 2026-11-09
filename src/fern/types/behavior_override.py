from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .verbosity import Verbosity
from .output_format import OutputFormat
from .interaction_budget import InteractionBudget


class BehaviorOverride(BaseModel):
    """BehaviorOverride

    :param verbosity: Verbosity override. Underlying default applies when unset., defaults to None
    :type verbosity: Verbosity, optional
    :param output_format: Output format override. Underlying default applies when unset., defaults to None
    :type output_format: OutputFormat, optional
    :param interaction_budget: Interaction budget override. Underlying default applies when unset., defaults to None
    :type interaction_budget: InteractionBudget, optional
    """

    verbosity: Optional[Verbosity] = Field(
        default=None,
        description="Verbosity override. Underlying default applies when unset.",
    )
    output_format: Optional[OutputFormat] = Field(
        default=None,
        description="Output format override. Underlying default applies when unset.",
    )
    interaction_budget: Optional[InteractionBudget] = Field(
        default=None,
        description="Interaction budget override. Underlying default applies when unset.",
    )
