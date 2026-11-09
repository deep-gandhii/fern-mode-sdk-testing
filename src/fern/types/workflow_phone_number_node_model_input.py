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
from .transfer_type_enum import TransferTypeEnum
from .uui_transfer_config import UuiTransferConfig
from .position_input import PositionInput
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


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem
class WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem_Static(CustomSipHeader):
    pass


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem
class WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem_Dynamic(
    CustomSipHeaderWithDynamicVariable
):
    pass


# Union type for WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem
# Pydantic will attempt to validate against each type in order
WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem = Union[
    CustomSipHeader, CustomSipHeaderWithDynamicVariable
]
# TypeAdapter for runtime validation of WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem_adapter = TypeAdapter(
    WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem
)


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelInputTransferDestination
class WorkflowPhoneNumberNodeModelInputTransferDestination_Phone(
    PhoneNumberTransferDestination
):
    pass


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelInputTransferDestination
class WorkflowPhoneNumberNodeModelInputTransferDestination_SipUri(
    SipUriTransferDestination
):
    pass


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelInputTransferDestination
class WorkflowPhoneNumberNodeModelInputTransferDestination_PhoneDynamicVariable(
    PhoneNumberDynamicVariableTransferDestination
):
    pass


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelInputTransferDestination
class WorkflowPhoneNumberNodeModelInputTransferDestination_SipUriDynamicVariable(
    SipUriDynamicVariableTransferDestination
):
    pass


# Union type for WorkflowPhoneNumberNodeModelInputTransferDestination
# Pydantic will attempt to validate against each type in order
WorkflowPhoneNumberNodeModelInputTransferDestination = Union[
    PhoneNumberTransferDestination,
    SipUriTransferDestination,
    PhoneNumberDynamicVariableTransferDestination,
    SipUriDynamicVariableTransferDestination,
]
# TypeAdapter for runtime validation of WorkflowPhoneNumberNodeModelInputTransferDestination
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkflowPhoneNumberNodeModelInputTransferDestination_adapter = TypeAdapter(
    WorkflowPhoneNumberNodeModelInputTransferDestination
)


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelInputPostDialDigits
class WorkflowPhoneNumberNodeModelInputPostDialDigits_Static(PostDialDigitsStatic):
    pass


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelInputPostDialDigits
class WorkflowPhoneNumberNodeModelInputPostDialDigits_Dynamic(
    PostDialDigitsDynamicVariable
):
    pass


# Union type for WorkflowPhoneNumberNodeModelInputPostDialDigits
# Pydantic will attempt to validate against each type in order
WorkflowPhoneNumberNodeModelInputPostDialDigits = Union[
    PostDialDigitsStatic, PostDialDigitsDynamicVariable
]
# TypeAdapter for runtime validation of WorkflowPhoneNumberNodeModelInputPostDialDigits
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkflowPhoneNumberNodeModelInputPostDialDigits_adapter = TypeAdapter(
    WorkflowPhoneNumberNodeModelInputPostDialDigits
)


WorkflowPhoneNumberNodeModelInputType = typing.Union[
    typing.Literal["phone_number"], typing.Any
]


class WorkflowPhoneNumberNodeModelInput(BaseModel):
    """WorkflowPhoneNumberNodeModelInput

    :param custom_sip_headers: Custom SIP headers to include when transferring the call. Each header can be either a static value or a dynamic variable reference., defaults to None
    :type custom_sip_headers: List[WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem], optional
    :param transfer_destination: transfer_destination
    :type transfer_destination: WorkflowPhoneNumberNodeModelInputTransferDestination
    :param transfer_type: transfer_type, defaults to None
    :type transfer_type: TransferTypeEnum, optional
    :param uui: User-to-User Information (RFC 7433) to attach to SIP REFER transfers. Carries call context such as CRM identifiers or escalation reason across the transfer boundary., defaults to None
    :type uui: UuiTransferConfig, optional
    :param post_dial_digits: DTMF digits to send after call connects (e.g., 'ww1234' for extension). Can be either a static value or a dynamic variable reference. Use 'w' for 0.5s pause. Only supported for Twilio transfers., defaults to None
    :type post_dial_digits: WorkflowPhoneNumberNodeModelInputPostDialDigits, optional
    :param type: type, defaults to None
    :type type: WorkflowPhoneNumberNodeModelInputType, optional
    :param position: position, defaults to None
    :type position: PositionInput, optional
    :param edge_order: The ids of outgoing edges in the order they should be evaluated., defaults to None
    :type edge_order: List[str], optional
    """

    custom_sip_headers: Optional[
        List[WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem]
    ] = Field(
        default=None,
        description="Custom SIP headers to include when transferring the call. Each header can be either a static value or a dynamic variable reference.",
    )
    transfer_destination: WorkflowPhoneNumberNodeModelInputTransferDestination
    transfer_type: Optional[TransferTypeEnum] = Field(default=None)
    uui: Optional[UuiTransferConfig] = Field(
        default=None,
        description="User-to-User Information (RFC 7433) to attach to SIP REFER transfers. Carries call context such as CRM identifiers or escalation reason across the transfer boundary.",
    )
    post_dial_digits: Optional[WorkflowPhoneNumberNodeModelInputPostDialDigits] = Field(
        default=None,
        description="DTMF digits to send after call connects (e.g., 'ww1234' for extension). Can be either a static value or a dynamic variable reference. Use 'w' for 0.5s pause. Only supported for Twilio transfers.",
    )
    type: Optional[WorkflowPhoneNumberNodeModelInputType] = Field(default=None)
    position: Optional[PositionInput] = Field(default=None)
    edge_order: Optional[List[str]] = Field(
        default=None,
        description="The ids of outgoing edges in the order they should be evaluated.",
    )
