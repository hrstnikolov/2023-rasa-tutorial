from enum import Enum, auto
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# See https://docs.python.org/3/howto/enum.html#using-automatic-values
class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()


class Weekday(Enum):
    Monday = auto()
    Tuesday = auto()
    Wednesday = auto()
    Thursday = auto()
    Friday = auto()
    Saturday = auto()
    Sunday = auto()


class ActionCheckDateAvailability(Action):
    def name(self) -> Text:
        return "check_date_availability"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        weekday = tracker.get_slot("weekday")
        if weekday in [Weekday.Saturday, Weekday.Sunday]:
            dispatcher.utter_message(response="utter_fully_booked")
        else:
            dispatcher.utter_message(response="utter_confirm_availability")

        return []
