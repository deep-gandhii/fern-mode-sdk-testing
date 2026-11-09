from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .billing_period import BillingPeriod

PendingSubscriptionSwitchResponseModelKind = typing.Union[
    typing.Literal["change"], typing.Any
]

PendingSubscriptionSwitchResponseModelNextTier = typing.Union[
    typing.Literal[
        "free",
        "starter",
        "creator",
        "pro",
        "growing_business",
        "scale_2024_08_10",
        "grant_tier_1_2025_07_23",
        "grant_tier_2_2025_07_23",
        "trial",
        "enterprise",
    ],
    typing.Any,
]


class PendingSubscriptionSwitchResponseModel(BaseModel):
    """PendingSubscriptionSwitchResponseModel

    :param kind: kind, defaults to None
    :type kind: PendingSubscriptionSwitchResponseModelKind, optional
    :param next_tier: The tier to change to.
    :type next_tier: PendingSubscriptionSwitchResponseModelNextTier
    :param next_billing_period: next_billing_period
    :type next_billing_period: BillingPeriod
    :param timestamp_seconds: The timestamp of the change.
    :type timestamp_seconds: int
    """

    kind: Optional[PendingSubscriptionSwitchResponseModelKind] = Field(default=None)
    next_tier: PendingSubscriptionSwitchResponseModelNextTier = Field(
        description="The tier to change to."
    )
    next_billing_period: BillingPeriod
    timestamp_seconds: int = Field(description="The timestamp of the change.")
