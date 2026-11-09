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
from .whats_app_template_text_param import WhatsAppTemplateTextParam
from .whats_app_template_image_param import WhatsAppTemplateImageParam
from .whats_app_template_document_param import WhatsAppTemplateDocumentParam
from .whats_app_template_location_param import WhatsAppTemplateLocationParam

WhatsAppTemplateHeaderComponentParamsType = typing.Union[
    typing.Literal["header"], typing.Any
]


# fernMode variant type for a shared-component member of WhatsAppTemplateHeaderComponentParamsParametersItem
class WhatsAppTemplateHeaderComponentParamsParametersItem_Text(
    WhatsAppTemplateTextParam
):
    pass


# fernMode variant type for a shared-component member of WhatsAppTemplateHeaderComponentParamsParametersItem
class WhatsAppTemplateHeaderComponentParamsParametersItem_Image(
    WhatsAppTemplateImageParam
):
    pass


# fernMode variant type for a shared-component member of WhatsAppTemplateHeaderComponentParamsParametersItem
class WhatsAppTemplateHeaderComponentParamsParametersItem_Document(
    WhatsAppTemplateDocumentParam
):
    pass


# fernMode variant type for a shared-component member of WhatsAppTemplateHeaderComponentParamsParametersItem
class WhatsAppTemplateHeaderComponentParamsParametersItem_Location(
    WhatsAppTemplateLocationParam
):
    pass


# Union type for WhatsAppTemplateHeaderComponentParamsParametersItem
# Pydantic will attempt to validate against each type in order
WhatsAppTemplateHeaderComponentParamsParametersItem = Union[
    WhatsAppTemplateTextParam,
    WhatsAppTemplateImageParam,
    WhatsAppTemplateDocumentParam,
    WhatsAppTemplateLocationParam,
]
# TypeAdapter for runtime validation of WhatsAppTemplateHeaderComponentParamsParametersItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WhatsAppTemplateHeaderComponentParamsParametersItem_adapter = TypeAdapter(
    WhatsAppTemplateHeaderComponentParamsParametersItem
)


class WhatsAppTemplateHeaderComponentParams(BaseModel):
    """WhatsAppTemplateHeaderComponentParams

    :param type: type, defaults to None
    :type type: WhatsAppTemplateHeaderComponentParamsType, optional
    :param parameters: parameters
    :type parameters: List[WhatsAppTemplateHeaderComponentParamsParametersItem]
    """

    type: Optional[WhatsAppTemplateHeaderComponentParamsType] = Field(default=None)
    parameters: List[WhatsAppTemplateHeaderComponentParamsParametersItem]
