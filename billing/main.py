config = {
    # Stripe keys or any other payment provider.
    "STRIPE_KEY": "your-stripe-key",
    "STRIPE_SECRET": "your-stripe-secret",
    "STRIPE_WEBHOOK_SECRET": "your-stripe-webhook-secret",
    # Currency configuration
    "BILLING_CURRENCY": "eur",
    "CASHIER_CURRENCY_LOCALE": "nl_BE",
}


class Billing:

    @classmethod
    def calculate_taxes(cls):
        """Enables tax calculations, should be called when the app boots."""
        pass

    @classmethod
    def use_customer_model(cls, model):
        """
        Used to specify a custom billable model. Should be called when the
        app boots.
        """
        pass

    @classmethod
    def use_subscription_model(cls, model):
        """
        Tells the billing system to use a custom subscription model.
        """
        pass

    @classmethod
    def use_subscription_item_model(cls, model):
        """
        Tells the billing system to use a custom subscription item model.
        """
        pass

    @classmethod
    def find_billable(cls, id) -> User:
        """Retrieve a custmer by the id"""
        return User(name="james")


class Billable:
    """Billable trait, inherited by a billable model like User."""

    def checkout(self):
        pass

    def new_subscription(self, a: str, b: str):
        return Subscription()

    def subscribed(self):
        """Determine a user's current subscription status"""
        pass

    def balance(self):
        """
        Return a formatted string representation of the balance
        in the customer's currency.
        """
        pass

    def credit_balance(self, amount, description):
        """Credit a customers balance."""
        pass

    def debit_balance(self, amount, description):
        """Debit the customer's balance"""
        pass

    def balance_transactions(self):
        """Return transactions"""
        return [BalanceTransaction(), BalanceTransaction()]

    def tax_ids(self):
        """Retrieve all of the tax ids that are assigned to a customer"""
        return [TaxId(), TaxId()]

    def create_tax_id(self, type, value):
        """Adds the VAT ID to the customer's account."""
        return TaxId(type, value, user=self)

    def delete_tax_id(txi_belgium):
        """Delete a tax id"""
        pass


class TaxId:
    def __init__(self):
        self.type = "ue_vat"
        self.value = "BE0123456789"
        self.user = None


class BalanceTransaction:
    def __init__(self):
        self.amount = 100
        self.invoice = Invoice()


class Invoice:
    pass


class User(Billable):
    def __init__(self, name):
        self.name = name


class Subscription:

    def trial_days(self, n: int):
        self.n = n
        return self

    def allow_promotion_codes(self):
        return self

    def checkout(self):
        """Not sure if this checkout method should be here or Billable"""
        pass


class SubscriptionItem:
    pass


class Order:
    def __init__(self, cart_id, price_ids, status):
        self.cart_id = cart_id
        self.price_ids = price_ids
        self.status = status

    @classmethod
    def create(cls, data):
        """Create an order"""
        return Order(cart_id=data.cart_id, price_ids=data.cart_ids, status=data.status)


class Cart:
    def __init__(self, id, price_ids):
        self.id = id
        self.price_ids = price_ids


# Charging customers for non-recurring, single-charde products.
price_id = "price_deluxe_album"
quantity = 1

user1 = User(name="faraji")

# Redirect customer to checkout for a given price identifier
user1.checkout(
    {price_id: quantity},
    {
        "success_url": "/home/success",
        "cancel_url": "/home/cancel",
    },
)


# Providing metadata to checkout
cart = Cart(id=1, price_ids=["price_deluxe_album", "price_standard_album"])
order = Order.create(
    {
        "cart_id": cart.id,
        "price_ids": cart.price_ids,
        "status": "incomplete",
    }
)

user1.checkout(
    order.price_ids,
    {
        "success_url": "/home/success",
        "cancel_url": "/home/cancel",
        # We provide metadata to checkout
        "metadata": {"order_id": order.id},
    },
)

# Selling subscriptions

# pro_basic (price_basic_monthly, price_basic_yearly)
# pro_expert (price_expert_monthly, price_expert_yearly)


# How a user might subscribe
user1.new_subscription("default", "price_basic_monthly").trial_days(
    5
).allow_promotion_codes().checkout(
    {
        "success_url": "/home/success",
        "cancel_url": "/home/cancel",
    }
)


# Check subscription status
user1.subscribed()

# Check if a user is subscribed to a specific product or price
user1.subscribed("pro_basic")


# Retrieve all transactions
transactions = user1.balance_transactions()

for transaction in transactions:
    # Transaction amaount
    amount = transaction.amount()

    # Retrieve the related invoice when available
    invoice = transaction.invoice()
