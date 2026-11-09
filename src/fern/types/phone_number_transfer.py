from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .transfer_type_enum import TransferTypeEnum
from .uui_transfer_config import UuiTransferConfig
from .custom_sip_header import CustomSipHeader
from .custom_sip_header_with_dynamic_variable import CustomSipHeaderWithDynamicVariable
from .phone_number_transfer_destination import PhoneNumberTransferDestination
from .sip_uri_transfer_destination import SipUriTransferDestination
from .phone_number_dynamic_variable_transfer_destination import (
    PhoneNumberDynamicVariableTransferDestination,
)
from .sip_uri_dynamic_variable_transfer_destination import (
    SipUriDynamicVariableTransferDestination,
)
from .post_dial_digits_static import PostDialDigitsStatic
from .post_dial_digits_dynamic_variable import PostDialDigitsDynamicVariable


class PhoneNumberTransfer(BaseModel):
    """PhoneNumberTransfer

    :param custom_sip_headers: Custom SIP headers to include when transferring the call. Each header can be either a static value or a dynamic variable reference., defaults to None
    :type custom_sip_headers: List[PhoneNumberTransferCustomSipHeadersItem], optional
    :param transfer_destination: transfer_destination
    :type transfer_destination: PhoneNumberTransferTransferDestination
    :param transfer_type: transfer_type, defaults to None
    :type transfer_type: TransferTypeEnum, optional
    :param uui: User-to-User Information (RFC 7433) to attach to SIP REFER transfers. Carries call context such as CRM identifiers or escalation reason across the transfer boundary., defaults to None
    :type uui: UuiTransferConfig, optional
    :param post_dial_digits: DTMF digits to send after call connects (e.g., 'ww1234' for extension). Can be either a static value or a dynamic variable reference. Use 'w' for 0.5s pause. Only supported for Twilio transfers., defaults to None
    :type post_dial_digits: PhoneNumberTransferPostDialDigits, optional
    :param phone_number: phone_number, defaults to None
    :type phone_number: str, optional
    :param condition: condition
    :type condition: str
    """

    custom_sip_headers: Optional[List[PhoneNumberTransferCustomSipHeadersItem]] = Field(
        default=None,
        description="Custom SIP headers to include when transferring the call. Each header can be either a static value or a dynamic variable reference.",
    )
    transfer_destination: PhoneNumberTransferTransferDestination
    transfer_type: Optional[TransferTypeEnum] = Field(default=None)
    uui: Optional[UuiTransferConfig] = Field(
        default=None,
        description="User-to-User Information (RFC 7433) to attach to SIP REFER transfers. Carries call context such as CRM identifiers or escalation reason across the transfer boundary.",
    )
    post_dial_digits: Optional[PhoneNumberTransferPostDialDigits] = Field(
        default=None,
        description="DTMF digits to send after call connects (e.g., 'ww1234' for extension). Can be either a static value or a dynamic variable reference. Use 'w' for 0.5s pause. Only supported for Twilio transfers.",
    )
    phone_number: Optional[str] = Field(default=None)
    condition: str


# fernMode variant type for a shared-component member of PhoneNumberTransferCustomSipHeadersItem
class PhoneNumberTransferCustomSipHeadersItem_Static(CustomSipHeader):
    pass


# fernMode variant type for a shared-component member of PhoneNumberTransferCustomSipHeadersItem
class PhoneNumberTransferCustomSipHeadersItem_Dynamic(
    CustomSipHeaderWithDynamicVariable
):
    pass


# Union type for PhoneNumberTransferCustomSipHeadersItem
# Pydantic will attempt to validate against each type in order
PhoneNumberTransferCustomSipHeadersItem = Union[
    CustomSipHeader, CustomSipHeaderWithDynamicVariable
]
# TypeAdapter for runtime validation of PhoneNumberTransferCustomSipHeadersItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

PhoneNumberTransferCustomSipHeadersItem_adapter = TypeAdapter(
    PhoneNumberTransferCustomSipHeadersItem
)


# fernMode variant type for a shared-component member of PhoneNumberTransferTransferDestination
class PhoneNumberTransferTransferDestination_Phone(PhoneNumberTransferDestination):
    pass


# fernMode variant type for a shared-component member of PhoneNumberTransferTransferDestination
class PhoneNumberTransferTransferDestination_SipUri(SipUriTransferDestination):
    pass


# fernMode variant type for a shared-component member of PhoneNumberTransferTransferDestination
class PhoneNumberTransferTransferDestination_PhoneDynamicVariable(
    PhoneNumberDynamicVariableTransferDestination
):
    pass


# fernMode variant type for a shared-component member of PhoneNumberTransferTransferDestination
class PhoneNumberTransferTransferDestination_SipUriDynamicVariable(
    SipUriDynamicVariableTransferDestination
):
    pass


# Union type for PhoneNumberTransferTransferDestination
# Pydantic will attempt to validate against each type in order
PhoneNumberTransferTransferDestination = Union[
    PhoneNumberTransferDestination,
    SipUriTransferDestination,
    PhoneNumberDynamicVariableTransferDestination,
    SipUriDynamicVariableTransferDestination,
]
# TypeAdapter for runtime validation of PhoneNumberTransferTransferDestination
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

PhoneNumberTransferTransferDestination_adapter = TypeAdapter(
    PhoneNumberTransferTransferDestination
)


# fernMode variant type for a shared-component member of PhoneNumberTransferPostDialDigits
class PhoneNumberTransferPostDialDigits_Static(PostDialDigitsStatic):
    pass


# fernMode variant type for a shared-component member of PhoneNumberTransferPostDialDigits
class PhoneNumberTransferPostDialDigits_Dynamic(PostDialDigitsDynamicVariable):
    pass


# Union type for PhoneNumberTransferPostDialDigits
# Pydantic will attempt to validate against each type in order
PhoneNumberTransferPostDialDigits = Union[
    PostDialDigitsStatic, PostDialDigitsDynamicVariable
]
# TypeAdapter for runtime validation of PhoneNumberTransferPostDialDigits
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

PhoneNumberTransferPostDialDigits_adapter = TypeAdapter(
    PhoneNumberTransferPostDialDigits
)


# Rebuild model to resolve forward references from submodels
PhoneNumberTransfer.model_rebuild()
