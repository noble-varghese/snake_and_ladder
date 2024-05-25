# from src.board import Board
# from src.dice import Dice


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.position = 0
        self.win_status = False
        self.turns_held = 0

    def get_player_name(self):
        return self.name

    def set_turns_held(self, turns_held):
        # If the turns have been held in a position, then decrement. Otherwise set it.
        if self.turns_held > 0:
            self.turns_held -= 1
            return
        self.turns_held = turns_held

    def decrement_turns_held(self):
        self.turns_held = max(0, self.turns_held-1)

    def can_move(self):
        return self.turns_held == 0

    def get_win_status(self):
        return self.win_status

    def get_position(self):
        return self.position

    def set_position(self, pos):
        self.position = pos

    def reset_position(self):
        self.position = 0

    def set_win_status(self, status):
        self.win_status = status

    def object_type(self):
        return "Player"
