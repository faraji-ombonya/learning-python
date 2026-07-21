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

    def database_type(self, notifiable: Notifiable):
        pass

    def initial_database_read_at_value(self):
        pass

    def mark_as_read(self):
        pass


class NotificationCollection:
    def __init__(self, query_set):
        pass

    def mark_as_read(self):
        pass

    def delete(self):
        pass

    def get_query_set(self):
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

    def notifications(self):
        """Return all notifications for the notifiable entity."""
        pass

    def unread_notifications(self) -> NotificationCollection:
        """Return all unread notifications for the notifiable entity."""
        pass

    def read_notifications(self) -> NotificationCollection:
        """Return all unread notifications for the notifiable entity."""
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


class NotificationFacade(object):
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
    def route(cls, channel, address):
        """
        Send an notification on demand.

        email, email_address
        sms, phone_number
        """
        return Route(channel, address)

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
class Message(ABC):
    """Abstract message builder class."""

    @abstractmethod
    def get_message(self):
        return getattr(self, "message", None)


class AfricasTalkingMessage(Message):
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

# Get user's notifications
user1.notifications()
user1.unread_notifications()
user1.read_notifications()
