"""Laravel like notifications blueprint."""

from abc import ABC, abstractmethod


class Notification(ABC):
    """
    The concrete class should define relevant message building
    methods, e.g to_mail.
    """

    @abstractmethod
    def via(self, notifiable: Notifiable) -> list[DeliveryChannel]:
        """Return a list of delivery channels.

        Determines which delivery channels the notification will be
        delivered to.
        """
        return [AfricasTalkingChannel]

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

    def to_sms(self, notifiable: Notifiable):
        """Convert the notification to a message tailored for sms."""
        pass

    def database_type(self, notifiable: Notifiable):
        pass

    def initial_database_read_at_value(self):
        pass

    def mark_as_read(self):
        pass


class Notifiable(ABC):
    """
    Inherited by a class that notifications can be sent to. e.g.
    a User class.
    """

    def notify(self, notification: Notification):
        """Send the notification to the notifiable."""
        delivery_channels = notification.via()

        for channel in delivery_channels:
            channel.send()

        # Speculative approach 1.
        if "email" in delivery_channels:
            mail_message = notification.to_mail()

            # Get email from email property of notifiable entity.
            email = getattr(self, "email") or getattr(self, "email_address")

            # The notifiable entity can decide which email address to use.
            # by defining the `route_notification_for_email` method.
            if hasattr(self, "route_notification_for_email"):
                email = self.route_notification_for_email()

            # TODO: Send the message to email

        if "sms" in delivery_channels:
            sms_message = notification.to_sms()
            phone_number = getattr(self, "phone_number") or getattr(self, "phone")
            if hasattr(self, "route_notification_for_sms"):
                phone_number = self.route_notification_for_sms()
            # TODO: Send the message to sms

        if "telegram" in delivery_channels:
            telegram_message = notification.to_telegram()
            telegram_handle = self.telegram_handle
            # TODO: Send the message to sms

        if "database" in delivery_channels:
            database_message = notification.to_database()
            # models.Notification.objects.create()
            # TODO: Save the message to the database

    def notifications(self):
        pass

    def unread_notifications(self):
        pass

    def read_notifications(self):
        pass


class BaseRoute(ABC):
    def notify(self, notification: Notification):
        """Send a notification to all the route entries."""

        routes: list[tuple[str, str]] = self.routes

        for r in routes:
            # TODO: send the notification to the route.
            pass


class Route(BaseRoute):
    def __init__(self, channel, address):
        self.routes = [(channel, address)]

    def route(self, channel, address):
        """Add a rout to the list of routes and return self for chaining."""
        self.routes.append((channel, address))
        return self


class Routes(BaseRoute):
    def __init__(self, routes: list[tuple[str, str]]):
        self.routes = routes


class NotificationFacade(ABC):
    @classmethod
    def send(cls, notifiables: list[Notifiable], notification: Notification):
        """
        Sends the notification to the notifiables synchronously,
        using queues etc.

        Probably invokes the notify method of the notifiable.
        """
        for n in notifiables:
            # TODO: send asynchronously.
            n.notify(notification)

    @classmethod
    def send_now(cls, notifiables: list[Notifiable], notification: Notification):
        """Sends the notification to the notifiables synchronously.

        Probably invokes the notify method of the notifiable.
        """
        for n in notifiables:
            n.notify(notification)

    @classmethod
    def route(cls, delivery_channel, address):
        """
        Send an notification on demand.

        email, email_address
        sms, phone_number
        """
        return Route(delivery_channel, address)

    @classmethod
    def routes(cls, routes: list[tuple[str, str]]):
        """
        Send a notification on demand.
        [
            (email, email_address),
            (sms, phone_number),
        ]
        """
        return Routes(routes)


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

# Get user's notifications
user1.notifications()
user1.unread_notifications()
user1.read_notifications()


# TODO: Come up with an interface for plug and play delivery channels.
class DeliveryChannel(ABC):

    @abstractmethod
    def send(self, notifiable: Notifiable, notification: Notification):
        """Method"""
        pass


class AfricasTalkingChannel(DeliveryChannel):
    def send(self, notifiable, notification):
        message = notification.to_sms(notifiable)
        phone_number = notifiable.route_notification_for_sms()
        # TODO: send the message to africas talking
        return


# Message builders for various channels
class ChannelMessage(ABC):
    pass
