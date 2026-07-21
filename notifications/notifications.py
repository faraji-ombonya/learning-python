"""Laravel like notifications blueprint."""

from abc import ABC


class Notification(ABC):
    """
    The concrete class should define relevant message building
    methods, e.g to_mail.
    """

    def via(self, notifiable):
        """Return a list of delivery channels.

        Determines which delivery channels the notification will be
        delivered to.
        """
        return ["mail", "database"]

    def to_mail(self, notifiable: Notifiable):
        """Convert the notification to a message tailored for email."""
        pass

    def to_database(self, notifiable: Notifiable):
        """
        Convert the notification to a message that can be stored
        in the database.
        """
        pass

    def to_telegram(self, notifiable: Notifiable):
        """Convert the notification to a message tailored for telegram."""
        pass

    def to_slack(self, notifiable: Notifiable):
        """Convert the notification to a message tailored for slack."""
        pass


class Notifiable(ABC):
    """
    Inherited by a class that notifications can be sent to. e.g.
    a User class.
    """

    def notify(notification: Notification):
        """Send the notification to the notifiable."""
        pass


class NotificationFacade(ABC):
    @classmethod
    def send(cls, notifiables: list[Notifiable], notification: Notification):
        """
        Sends the notification to the notifiables synchronously,
        using queues etc.

        Probably invokes the notify method of the notifiable.
        """
        pass

    @classmethod
    def send_now(cls, notifiables: list[Notifiable], notification: Notification):
        """Sends the notification to the notifiables synchronously.

        Probably invokes the notify method of the notifiable.
        """
        pass

    @classmethod
    def route(cls, delivery_channel, address):
        """
        email, email_address
        sms, phone_number
        """
        return cls

    @classmethod
    def routes(cls, routes: list[tuple[str, str]]):
        """
        [
            (email, email_address),
            (sms, phone_number),
        ]
        """
        return cls

    def notify(self, notification: Notification):
        """Called after a route chain.

        E.g NotificationFacade.route().route().notify()
        or NotificationFacade.routes().notify()

        gets routes, populated by route() or routes()
        and sends them the Notification
        """
        pass


# Example usage


# Initial setup
# We define a notifiable class, make this relationship explicit by
# inheriting the Notifiable
class User(Notifiable):
    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email


# Prepare users
user1 = User(name="Faraji", email="test@example.com", phone="111111111")
user2 = User(name="Shikanda", email="test2@example.com", phone="222222222")
user3 = User(name="Faraji", email="test@example.com", phone="111111111")
all_users = [user1, user2, user3]


# Generating notifications
# We define revelant notifications
class WelcomeNotification(Notification):
    """Notification sent to a new user."""

    def via(self, notifiable):
        """This notification will only be sent via email."""
        return ["email"]

    def to_mail(self, notifiable):
        return f"Welcome {notifiable.name}"


class PromoNotification(Notification):
    """Promo Notification sent to all users."""

    def via(self, notifiable):
        """This notification will only be sent via email."""
        return ["email"]

    def to_mail(self, notifiable):
        return f"Hi {notifiable.name}. New offer for you!"


# Sending notifications
# Send a single notification to a user using notifiable.notify
welcome_notification = WelcomeNotification()
user1.notify(welcome_notification)

# Send multiple marketing notifications to all users asynchronously
promo_notification = PromoNotification()
NotificationFacade.send(all_users, promo_notification)

# Send multiple marketing notifications to all users synchronously
promo_notification = PromoNotification()
NotificationFacade.send_now(all_users, promo_notification)

# Ondemand notifications
# using chained route
NotificationFacade.route("email", user1.email).route("sms", user1.phone).notify(
    welcome_notification
)

# Using routes
NotificationFacade.routes([("email", user2.email), ("sms", user2.phone)]).notify(
    welcome_notification
)
