from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BatchCallWhatsAppParams(BaseModel):
    """BatchCallWhatsAppParams

    :param whatsapp_phone_number_id: whatsapp_phone_number_id, defaults to None
    :type whatsapp_phone_number_id: str, optional
    :param whatsapp_call_permission_request_template_name: whatsapp_call_permission_request_template_name
    :type whatsapp_call_permission_request_template_name: str
    :param whatsapp_call_permission_request_template_language_code: whatsapp_call_permission_request_template_language_code
    :type whatsapp_call_permission_request_template_language_code: str
    """

    whatsapp_phone_number_id: Optional[str] = Field(default=None)
    whatsapp_call_permission_request_template_name: str
    whatsapp_call_permission_request_template_language_code: str
