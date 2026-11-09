from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .discount_response_model import DiscountResponseModel

InvoiceResponsePaymentIntentStatus = typing.Union[
    typing.Literal[
        "canceled",
        "processing",
        "requires_action",
        "requires_capture",
        "requires_confirmation",
        "requires_payment_method",
        "succeeded",
    ],
    typing.Any,
]

InvoiceResponsePaymentIntentStatussesItem = typing.Union[
    typing.Literal[
        "canceled",
        "processing",
        "requires_action",
        "requires_capture",
        "requires_confirmation",
        "requires_payment_method",
        "succeeded",
    ],
    typing.Any,
]


class InvoiceResponse(BaseModel):
    """InvoiceResponse

    :param amount_due_cents: The amount due in cents.
    :type amount_due_cents: int
    :param subtotal_cents: The subtotal amount in cents before tax (exclusive of tax and discounts)., defaults to None
    :type subtotal_cents: int, optional
    :param tax_cents: The tax amount in cents., defaults to None
    :type tax_cents: int, optional
    :param discount_percent_off: Deprecated. Use [discounts] instead. The discount applied to the invoice. E.g. [20.0f] for 20% off., defaults to None
    :type discount_percent_off: float, optional
    :param discount_amount_off: Deprecated. Use [discounts] instead. The discount applied to the invoice. E.g. [20.0f] for 20 cents off., defaults to None
    :type discount_amount_off: float, optional
    :param discounts: The discounts applied to the invoice.
    :type discounts: List[DiscountResponseModel]
    :param next_payment_attempt_unix: The Unix timestamp of the next payment attempt. -1 when there is no next payment attempt.
    :type next_payment_attempt_unix: int
    :param payment_intent_status: Deprecated. Use [payment_intent_statusses] instead. The status of this invoice's first payment intent. None when there is no payment intent.
    :type payment_intent_status: InvoiceResponsePaymentIntentStatus
    :param payment_intent_statusses: The statuses of this invoice's payment intents. Empty list when there are no payment intents.
    :type payment_intent_statusses: List[InvoiceResponsePaymentIntentStatussesItem]
    """

    amount_due_cents: int = Field(description="The amount due in cents.")
    subtotal_cents: Optional[int] = Field(
        default=None,
        description="The subtotal amount in cents before tax (exclusive of tax and discounts).",
    )
    tax_cents: Optional[int] = Field(
        default=None, description="The tax amount in cents."
    )
    discount_percent_off: Optional[float] = Field(
        default=None,
        description="Deprecated. Use [discounts] instead. The discount applied to the invoice. E.g. [20.0f] for 20% off.",
    )
    discount_amount_off: Optional[float] = Field(
        default=None,
        description="Deprecated. Use [discounts] instead. The discount applied to the invoice. E.g. [20.0f] for 20 cents off.",
    )
    discounts: List[DiscountResponseModel] = Field(
        description="The discounts applied to the invoice."
    )
    next_payment_attempt_unix: int = Field(
        description="The Unix timestamp of the next payment attempt. -1 when there is no next payment attempt."
    )
    payment_intent_status: Optional[InvoiceResponsePaymentIntentStatus] = Field(
        description="Deprecated. Use [payment_intent_statusses] instead. The status of this invoice's first payment intent. None when there is no payment intent."
    )
    payment_intent_statusses: List[InvoiceResponsePaymentIntentStatussesItem] = Field(
        description="The statuses of this invoice's payment intents. Empty list when there are no payment intents."
    )
