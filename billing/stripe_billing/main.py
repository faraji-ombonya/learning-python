"""Billing system modelled from stripe"""


class Product:
    """A product can have many prices"""
    id = "1234"

    active = True
    """Whether the product is available for purchase"""

    created_at = ""
    default_price = None
    description = None
    images = []
    marketing_features = None
    livemode = False
    metadata = {}
    name = ""



class Price:
    """
    Prices define the unit cost, currency and (optional) billing
    cycle.

    A price belongs to a product
    """

    id = "45464"
    """Unique identifier for the object."""

    active = True
    """Whether the price can be used for new purchases"""

    currency = ""
    """
    Three-letter ISO currency code, in lowercase. Must be a
    supported currency.
    """

    product = ""
    """The ID of the product this price is associated with."""

    recurring = {
        "interval": "day",
        "interval_count": 1,
        "meter": None,
        "usage_type": "licensed",
    }
    """
    The recurring components of a price such as `interval` and
    `usage_type`

    recurring.**interval** `enum`: 
        The frequency at which a subscription is
        billed. One of `day`, `week`, `month` or `year`.
    """

    type = "one_time"
    """
    One of `one_time` or `recurring` depending on whether the
    price is for a one-time purchase or a recurring (subscription)
    purchase.
    """


class Subscription:
    id = ""
    """Unique identifier for the object."""

    currency = ""
    """
    Three-letter ISO currency code, in lowercase.
    Must be a supported currency.
    """

    customer = ""
    """ID of the customer who owns the subscription."""

    default_payment_method = ""
    """ID of the default payment method for the subscription."""

    items = []
    """List of subscription items, each with an attached price.
    
    items.object:

    """
