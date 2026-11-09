from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .subscription_response import SubscriptionResponse
from .seat_type import SeatType


class User(BaseModel):
    """User

    :param user_id: The unique identifier of the user.
    :type user_id: str
    :param subscription: subscription
    :type subscription: SubscriptionResponse
    :param is_new_user: Whether the user is new. This field is deprecated and will be removed in the future. Use 'created_at' instead.
    :type is_new_user: bool
    :param xi_api_key: The API key of the user., defaults to None
    :type xi_api_key: str, optional
    :param can_use_delayed_payment_methods: This field is deprecated and will be removed in a future major version. Instead use subscription.trust_on_invoice_creation.
    :type can_use_delayed_payment_methods: bool
    :param is_onboarding_completed: Whether the user's onboarding is completed.
    :type is_onboarding_completed: bool
    :param is_onboarding_checklist_completed: Whether the user's onboarding checklist is completed.
    :type is_onboarding_checklist_completed: bool
    :param show_compliance_terms: Whether to show compliance terms (ToS, Privacy Policy, biometric consent) during onboarding. Set for users signing up from the marketing site., defaults to None
    :type show_compliance_terms: bool, optional
    :param first_name: First name of the user., defaults to None
    :type first_name: str, optional
    :param is_api_key_hashed: Whether the user's API key is hashed., defaults to None
    :type is_api_key_hashed: bool, optional
    :param xi_api_key_preview: The preview of the user's API key., defaults to None
    :type xi_api_key_preview: str, optional
    :param referral_link_code: The referral link code of the user., defaults to None
    :type referral_link_code: str, optional
    :param partnerstack_partner_default_link: The Partnerstack partner default link of the user., defaults to None
    :type partnerstack_partner_default_link: str, optional
    :param created_at: The unix timestamp of the user's creation. 0 if the user was created before the unix timestamp was added.
    :type created_at: int
    :param seat_type: Seat types for workspace members.
    :type seat_type: SeatType
    """

    user_id: str = Field(description="The unique identifier of the user.")
    subscription: SubscriptionResponse
    is_new_user: bool = Field(
        description="Whether the user is new. This field is deprecated and will be removed in the future. Use 'created_at' instead."
    )
    xi_api_key: Optional[str] = Field(
        default=None, description="The API key of the user."
    )
    can_use_delayed_payment_methods: bool = Field(
        description="This field is deprecated and will be removed in a future major version. Instead use subscription.trust_on_invoice_creation."
    )
    is_onboarding_completed: bool = Field(
        description="Whether the user's onboarding is completed."
    )
    is_onboarding_checklist_completed: bool = Field(
        description="Whether the user's onboarding checklist is completed."
    )
    show_compliance_terms: Optional[bool] = Field(
        default=None,
        description="Whether to show compliance terms (ToS, Privacy Policy, biometric consent) during onboarding. Set for users signing up from the marketing site.",
    )
    first_name: Optional[str] = Field(
        default=None, description="First name of the user."
    )
    is_api_key_hashed: Optional[bool] = Field(
        default=None, description="Whether the user's API key is hashed."
    )
    xi_api_key_preview: Optional[str] = Field(
        default=None, description="The preview of the user's API key."
    )
    referral_link_code: Optional[str] = Field(
        default=None, description="The referral link code of the user."
    )
    partnerstack_partner_default_link: Optional[str] = Field(
        default=None, description="The Partnerstack partner default link of the user."
    )
    created_at: int = Field(
        description="The unix timestamp of the user's creation. 0 if the user was created before the unix timestamp was added."
    )
    seat_type: SeatType = Field(description="Seat types for workspace members.")
