"""
This example illustrates the builder and the strategy pattern
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Save(ABC):
    @abstractmethod
    def save(self, calendar: "Calendar"):
        pass


@dataclass
class Creator:
    id: str

    email: str
    """The email of the creator"""

    displayName: str
    _self: bool


@dataclass
class Calendar:

    description: str | None = None
    """Description of the event. Can contain HTML. Optional."""

    kind: str | None = None
    """Type of the resource ("calendar#event")"""

    summary: str | None = None

    creator: Creator | None = None

    save_strategy: Save | None = None

    def set_save_strategy(self, strategy: Save):
        self.save_strategy = strategy

    def save(self):
        if not self.save_strategy:
            raise ValueError("Save strategy not set")
        self.save_strategy.save(calendar=self)


class CalendarBuilder:
    def __init__(self):
        self.calendar = Calendar()

    def set_kind(self, kind: str):
        """Set kind

        Args:
            kind (str): Type of the resource ("calendar#event").
        """
        self.calendar.kind = kind
        return self

    def set_creator(self, creator: Creator):
        self.calendar.creator = creator
        return self

    def set_description(self, description: str):
        """
        Args:
            description (str):
        """
        self.calendar.description = description
        return self

    def build(self) -> Calendar:
        if not self.calendar.kind:
            raise ValueError("Kind is required")

        return self.calendar


class SaveToDB(Save):
    def save(self, calendar: Calendar):
        print("saving to db")


class SaveToCloud(Save):
    def save(self, calendar):
        return super().save(calendar)


class WhatsappSaver(Save):
    def save(self, calendar):
        return super().save(calendar)


if __name__ == "__main__":
    calendar_builder = CalendarBuilder()

    creator = Creator(
        id="fff", email="faraji@gmail.com", displayName="faraji", _self="false"
    )

    calendar = (
        calendar_builder.set_kind("ccc#asa")
        .set_creator(creator)
        .set_description("This is a very fancy description")
        .build()
    )

    for saver in [SaveToCloud(), SaveToDB(), WhatsappSaver()]:
        calendar.set_save_strategy(saver)
        calendar.save()
