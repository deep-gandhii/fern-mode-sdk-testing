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
from .currency import Currency
from .price import Price
from .subscription_status_type import SubscriptionStatusType
from .billing_period import BillingPeriod
from .character_refresh_period import CharacterRefreshPeriod
from .invoice_response import InvoiceResponse
from .pending_subscription_switch_response_model import (
    PendingSubscriptionSwitchResponseModel,
)
from .pending_cancellation_response_model import PendingCancellationResponseModel


class Subscription(BaseModel):
    """Subscription

    :param tier: The tier of the user's subscription.
    :type tier: str
    :param character_count: The number of characters used by the user.
    :type character_count: int
    :param character_limit: The maximum number of characters allowed in the current billing period.
    :type character_limit: int
    :param max_character_limit_extension: Deprecated: use `max_credit_limit_extension`. Maximum number of characters that the character limit can be exceeded by. Managed by the workspace admin.
    :type max_character_limit_extension: int
    :param max_credit_limit_extension: Maximum number of credits that the credit limit can be exceeded by. Managed by the workspace admin. `"unlimited"` means no cap, `0` means usage-based billing is disabled.
    :type max_credit_limit_extension: SubscriptionMaxCreditLimitExtension
    :param can_extend_character_limit: Whether the workspace is entitled to enter overages (usage-based billing).
    :type can_extend_character_limit: bool
    :param allowed_to_extend_character_limit: Deprecated: use `max_credit_limit_extension != 0`. Whether the user is allowed to extend their character limit.
    :type allowed_to_extend_character_limit: bool
    :param next_character_count_reset_unix: The Unix timestamp of the next character count reset., defaults to None
    :type next_character_count_reset_unix: int, optional
    :param voice_slots_used: The number of voice slots used by the user.
    :type voice_slots_used: int
    :param professional_voice_slots_used: The number of professional voice slots used. For consolidated billing this is the group-wide count across all workspaces in the group; see professional_voice_slots_used_in_workspace for the current workspace only.
    :type professional_voice_slots_used: int
    :param professional_voice_slots_used_in_workspace: The number of professional voice slots used in the current workspace. For consolidated billing, professional_voice_slots_used counts across all workspaces in the group, while this counts only the current workspace.
    :type professional_voice_slots_used_in_workspace: int
    :param voice_limit: The maximum number of voice slots allowed for the user.
    :type voice_limit: int
    :param max_voice_add_edits: The maximum number of voice add/edits allowed for the user., defaults to None
    :type max_voice_add_edits: int, optional
    :param voice_add_edit_counter: The number of voice add/edits used by the user.
    :type voice_add_edit_counter: int
    :param professional_voice_limit: The maximum number of professional voices allowed for the user.
    :type professional_voice_limit: int
    :param can_extend_voice_limit: Whether the user can extend their voice limit.
    :type can_extend_voice_limit: bool
    :param can_use_instant_voice_cloning: Whether the user can use instant voice cloning.
    :type can_use_instant_voice_cloning: bool
    :param can_use_professional_voice_cloning: Whether the user can use professional voice cloning.
    :type can_use_professional_voice_cloning: bool
    :param currency: The currency of the user's subscription., defaults to None
    :type currency: Currency, optional
    :param current_overage: Currency/amount pair.
    :type current_overage: Price
    :param status: status
    :type status: SubscriptionStatusType
    :param billing_period: The billing period of the user's subscription., defaults to None
    :type billing_period: BillingPeriod, optional
    :param character_refresh_period: The character refresh period of the user's subscription., defaults to None
    :type character_refresh_period: CharacterRefreshPeriod, optional
    :param next_invoice: The next invoice for the user., defaults to None
    :type next_invoice: InvoiceResponse, optional
    :param open_invoices: The open invoices for the user.
    :type open_invoices: List[InvoiceResponse]
    :param has_open_invoices: Whether the user has open invoices.
    :type has_open_invoices: bool
    :param pending_change: The pending change for the user., defaults to None
    :type pending_change: SubscriptionPendingChange, optional
    :param has_used_starter_coupon_on_account: True if any workspace owned by this user's auth account has redeemed the starter first-month discount coupon., defaults to None
    :type has_used_starter_coupon_on_account: bool, optional
    :param has_used_creator_coupon_on_account: True if any workspace owned by this user's auth account has redeemed the creator first-month discount coupon., defaults to None
    :type has_used_creator_coupon_on_account: bool, optional
    """

    tier: str = Field(description="The tier of the user's subscription.")
    character_count: int = Field(
        description="The number of characters used by the user."
    )
    character_limit: int = Field(
        description="The maximum number of characters allowed in the current billing period."
    )
    max_character_limit_extension: Optional[int] = Field(
        description="Deprecated: use `max_credit_limit_extension`. Maximum number of characters that the character limit can be exceeded by. Managed by the workspace admin."
    )
    max_credit_limit_extension: SubscriptionMaxCreditLimitExtension = Field(
        description='Maximum number of credits that the credit limit can be exceeded by. Managed by the workspace admin. `"unlimited"` means no cap, `0` means usage-based billing is disabled.'
    )
    can_extend_character_limit: bool = Field(
        description="Whether the workspace is entitled to enter overages (usage-based billing)."
    )
    allowed_to_extend_character_limit: bool = Field(
        description="Deprecated: use `max_credit_limit_extension != 0`. Whether the user is allowed to extend their character limit."
    )
    next_character_count_reset_unix: Optional[int] = Field(
        default=None,
        description="The Unix timestamp of the next character count reset.",
    )
    voice_slots_used: int = Field(
        description="The number of voice slots used by the user."
    )
    professional_voice_slots_used: int = Field(
        description="The number of professional voice slots used. For consolidated billing this is the group-wide count across all workspaces in the group; see professional_voice_slots_used_in_workspace for the current workspace only."
    )
    professional_voice_slots_used_in_workspace: int = Field(
        description="The number of professional voice slots used in the current workspace. For consolidated billing, professional_voice_slots_used counts across all workspaces in the group, while this counts only the current workspace."
    )
    voice_limit: int = Field(
        description="The maximum number of voice slots allowed for the user."
    )
    max_voice_add_edits: Optional[int] = Field(
        default=None,
        description="The maximum number of voice add/edits allowed for the user.",
    )
    voice_add_edit_counter: int = Field(
        description="The number of voice add/edits used by the user."
    )
    professional_voice_limit: int = Field(
        description="The maximum number of professional voices allowed for the user."
    )
    can_extend_voice_limit: bool = Field(
        description="Whether the user can extend their voice limit."
    )
    can_use_instant_voice_cloning: bool = Field(
        description="Whether the user can use instant voice cloning."
    )
    can_use_professional_voice_cloning: bool = Field(
        description="Whether the user can use professional voice cloning."
    )
    currency: Optional[Currency] = Field(
        default=None, description="The currency of the user's subscription."
    )
    current_overage: Price = Field(description="Currency/amount pair.")
    status: SubscriptionStatusType
    billing_period: Optional[BillingPeriod] = Field(
        default=None, description="The billing period of the user's subscription."
    )
    character_refresh_period: Optional[CharacterRefreshPeriod] = Field(
        default=None,
        description="The character refresh period of the user's subscription.",
    )
    next_invoice: Optional[InvoiceResponse] = Field(
        default=None, description="The next invoice for the user."
    )
    open_invoices: List[InvoiceResponse] = Field(
        description="The open invoices for the user."
    )
    has_open_invoices: bool = Field(description="Whether the user has open invoices.")
    pending_change: Optional[SubscriptionPendingChange] = Field(
        default=None, description="The pending change for the user."
    )
    has_used_starter_coupon_on_account: Optional[bool] = Field(
        default=None,
        description="True if any workspace owned by this user's auth account has redeemed the starter first-month discount coupon.",
    )
    has_used_creator_coupon_on_account: Optional[bool] = Field(
        default=None,
        description="True if any workspace owned by this user's auth account has redeemed the creator first-month discount coupon.",
    )


MaxCreditLimitExtension22 = typing.Union[typing.Literal["unlimited"], typing.Any]


# Union type for SubscriptionMaxCreditLimitExtension
# Pydantic will attempt to validate against each type in order
SubscriptionMaxCreditLimitExtension = Union[int, str]
# TypeAdapter for runtime validation of SubscriptionMaxCreditLimitExtension
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

SubscriptionMaxCreditLimitExtension_adapter = TypeAdapter(
    SubscriptionMaxCreditLimitExtension
)


# fernMode variant type for a shared-component member of SubscriptionPendingChange
class SubscriptionPendingChange_Change(PendingSubscriptionSwitchResponseModel):
    pass


# fernMode variant type for a shared-component member of SubscriptionPendingChange
class SubscriptionPendingChange_Cancellation(PendingCancellationResponseModel):
    pass


# Union type for SubscriptionPendingChange
# Pydantic will attempt to validate against each type in order
SubscriptionPendingChange = Union[
    PendingSubscriptionSwitchResponseModel, PendingCancellationResponseModel
]
# TypeAdapter for runtime validation of SubscriptionPendingChange
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

SubscriptionPendingChange_adapter = TypeAdapter(SubscriptionPendingChange)


# Rebuild model to resolve forward references from submodels
Subscription.model_rebuild()
