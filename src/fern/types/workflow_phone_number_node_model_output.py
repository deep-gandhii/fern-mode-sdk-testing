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
from .position_output import PositionOutput
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


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem
class WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem_Static(CustomSipHeader):
    pass


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem
class WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem_Dynamic(
    CustomSipHeaderWithDynamicVariable
):
    pass


# Union type for WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem
# Pydantic will attempt to validate against each type in order
WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem = Union[
    CustomSipHeader, CustomSipHeaderWithDynamicVariable
]
# TypeAdapter for runtime validation of WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem_adapter = TypeAdapter(
    WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem
)


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelOutputTransferDestination
class WorkflowPhoneNumberNodeModelOutputTransferDestination_Phone(
    PhoneNumberTransferDestination
):
    pass


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelOutputTransferDestination
class WorkflowPhoneNumberNodeModelOutputTransferDestination_SipUri(
    SipUriTransferDestination
):
    pass


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelOutputTransferDestination
class WorkflowPhoneNumberNodeModelOutputTransferDestination_PhoneDynamicVariable(
    PhoneNumberDynamicVariableTransferDestination
):
    pass


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelOutputTransferDestination
class WorkflowPhoneNumberNodeModelOutputTransferDestination_SipUriDynamicVariable(
    SipUriDynamicVariableTransferDestination
):
    pass


# Union type for WorkflowPhoneNumberNodeModelOutputTransferDestination
# Pydantic will attempt to validate against each type in order
WorkflowPhoneNumberNodeModelOutputTransferDestination = Union[
    PhoneNumberTransferDestination,
    SipUriTransferDestination,
    PhoneNumberDynamicVariableTransferDestination,
    SipUriDynamicVariableTransferDestination,
]
# TypeAdapter for runtime validation of WorkflowPhoneNumberNodeModelOutputTransferDestination
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkflowPhoneNumberNodeModelOutputTransferDestination_adapter = TypeAdapter(
    WorkflowPhoneNumberNodeModelOutputTransferDestination
)


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelOutputPostDialDigits
class WorkflowPhoneNumberNodeModelOutputPostDialDigits_Static(PostDialDigitsStatic):
    pass


# fernMode variant type for a shared-component member of WorkflowPhoneNumberNodeModelOutputPostDialDigits
class WorkflowPhoneNumberNodeModelOutputPostDialDigits_Dynamic(
    PostDialDigitsDynamicVariable
):
    pass


# Union type for WorkflowPhoneNumberNodeModelOutputPostDialDigits
# Pydantic will attempt to validate against each type in order
WorkflowPhoneNumberNodeModelOutputPostDialDigits = Union[
    PostDialDigitsStatic, PostDialDigitsDynamicVariable
]
# TypeAdapter for runtime validation of WorkflowPhoneNumberNodeModelOutputPostDialDigits
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkflowPhoneNumberNodeModelOutputPostDialDigits_adapter = TypeAdapter(
    WorkflowPhoneNumberNodeModelOutputPostDialDigits
)


WorkflowPhoneNumberNodeModelOutputType = typing.Union[
    typing.Literal["phone_number"], typing.Any
]


class WorkflowPhoneNumberNodeModelOutput(BaseModel):
    """WorkflowPhoneNumberNodeModelOutput

    :param custom_sip_headers: Custom SIP headers to include when transferring the call. Each header can be either a static value or a dynamic variable reference.
    :type custom_sip_headers: List[WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem]
    :param transfer_destination: transfer_destination
    :type transfer_destination: WorkflowPhoneNumberNodeModelOutputTransferDestination
    :param transfer_type: transfer_type
    :type transfer_type: TransferTypeEnum
    :param uui: User-to-User Information (RFC 7433) to attach to SIP REFER transfers. Carries call context such as CRM identifiers or escalation reason across the transfer boundary.
    :type uui: UuiTransferConfig
    :param post_dial_digits: DTMF digits to send after call connects (e.g., 'ww1234' for extension). Can be either a static value or a dynamic variable reference. Use 'w' for 0.5s pause. Only supported for Twilio transfers.
    :type post_dial_digits: WorkflowPhoneNumberNodeModelOutputPostDialDigits
    :param type: type
    :type type: WorkflowPhoneNumberNodeModelOutputType
    :param position: position
    :type position: PositionOutput
    :param edge_order: The ids of outgoing edges in the order they should be evaluated.
    :type edge_order: List[str]
    """

    custom_sip_headers: List[WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem] = (
        Field(
            description="Custom SIP headers to include when transferring the call. Each header can be either a static value or a dynamic variable reference."
        )
    )
    transfer_destination: WorkflowPhoneNumberNodeModelOutputTransferDestination
    transfer_type: TransferTypeEnum
    uui: UuiTransferConfig = Field(
        description="User-to-User Information (RFC 7433) to attach to SIP REFER transfers. Carries call context such as CRM identifiers or escalation reason across the transfer boundary."
    )
    post_dial_digits: Optional[WorkflowPhoneNumberNodeModelOutputPostDialDigits] = (
        Field(
            description="DTMF digits to send after call connects (e.g., 'ww1234' for extension). Can be either a static value or a dynamic variable reference. Use 'w' for 0.5s pause. Only supported for Twilio transfers."
        )
    )
    type: WorkflowPhoneNumberNodeModelOutputType = Field(default="phone_number")
    position: PositionOutput
    edge_order: List[str] = Field(
        description="The ids of outgoing edges in the order they should be evaluated."
    )
