import random
from enum import Enum, auto
from typing import Text, Any, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class Moves(Enum):
    Rock = auto()
    Paper = auto()
    Scissors = auto()


class ActionPlayRPS(Action):
    def name(self) -> Text:
        return "action_play_rps"

    @staticmethod
    def choose_random_move():
        return random.choice(list(Moves))

    @staticmethod
    def get_move_from_str(choice: str):
        return getattr(Moves, choice.capitalize(), None)

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # get moves
        player_choice = tracker.get_slot("choice")
        player_move = self.get_move_from_str(player_choice)
        dispatcher.utter_message(text=f"You chose {player_move.name}")
        computer_move = self.choose_random_move()
        dispatcher.utter_message(text=f"The computer chose {computer_move.name}")

        # decide the outcome
        # player wins
        if any(
            [
                player_move is Moves.Rock and computer_move is Moves.Scissors,
                player_move is Moves.Scissors and computer_move is Moves.Paper,
                player_move is Moves.Paper and computer_move is Moves.Rock,
            ]
        ):
            dispatcher.utter_message(text="Congrats, you won!")
        # computer wins
        elif any(
            [
                computer_move is Moves.Rock and player_move is Moves.Scissors,
                computer_move is Moves.Scissors and player_move is Moves.Paper,
                computer_move is Moves.Paper and player_move is Moves.Rock,
            ]
        ):
            dispatcher.utter_message(text="The computer won this round.")
        # tie
        elif computer_move is player_move:
            dispatcher.utter_message(text="It was a tie!")

        return []
