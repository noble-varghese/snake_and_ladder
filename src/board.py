from src.snake import Snake
from src.crocodile import Crocodile
from src.mine import Mine
from src.ladder import Ladder
from src.player import Player
from typing import Optional, Union, Dict


class Board:
    def __init__(self, size) -> None:
        self.board: Dict[
            int,
            Union[
                Snake, Ladder, Crocodile, Mine
            ]
        ] = {}
        self.players: Dict[int, Player] = {}
        self._size = size

    def set_snake(self, snake: Snake):
        if snake.head in self.board:
            obj = self.board[snake.head]
            raise Exception(
                f"Position {snake.head} already occupied by {obj.object_type()}")

        self.board[snake.head] = snake

    def set_ladder(self, ladder: Ladder):
        if ladder.start in self.board:
            obj = self.board[ladder.start]
            raise Exception(
                f"Position {ladder.start} already occupied by {obj.object_type()}")

        self.board[ladder.start] = ladder

    def set_crocodile(self, crocodile: Crocodile):
        if crocodile.position in self.board:
            obj = self.board[crocodile.position]
            raise Exception(
                f"Position {crocodile.position} already occupied by {obj.object_type()}")

        self.board[crocodile.position] = crocodile

    def set_mine(self, mine: Mine):
        if mine.location in self.board:
            obj = self.board[mine.location]
            raise Exception(
                f"Position {mine.location} already occupied by {obj.object_type()}")

        self.board[mine.location] = mine

    def set_player(self, player: Player):
        self.players[player.get_position()] = player

    def unset_player(self, player: Player):
        if player.get_position() in self.players:
            del self.players[player.get_position()]

    def get_player_in_pos(self, pos) -> Optional[Player]:
        if self.check_other_players(pos):
            return self.players[pos]

        return None

    def check_mine(self, position):
        return position in self.board and self.board[position].object_type() == "Mine"

    def get_mine_turns_held(self, position):
        if self.check_mine(position):
            return self.board[position].turns_held
        return 0

    def check_other_players(self, pos):
        if pos == self._size:
            return False
        return pos in self.players

    def get_next_position(self, player: Player, dice_val, curr_position):
        new_position = curr_position + dice_val

        if new_position > self._size:
            print(
                f"{player.get_player_name()} rolled a {dice_val} at {curr_position} but can't move!")
            return curr_position

        if new_position in self.board:
            obj = self.board[new_position]
            pos = obj.next_position(new_position)
            self.print_message(player, obj.object_type(),
                               dice_val, curr_position, pos)
            return pos

        self.print_message(player, None, dice_val,
                           curr_position, new_position)
        return new_position

    def check_player_status(self, pos):
        return self._size == pos

    def print_message(self, player: Player, object_type, dice_val, curr_pos, new_pos):
        player_name = player.get_player_name()

        if player.turns_held > 0:
            print(
                f"{player_name} rolled a {dice_val} and hit by mine at {curr_pos}. Held for {player.turns_held} moves")

        elif object_type == "Snake":
            print(f"{player_name} rolled a {dice_val} and bitten by snake at {curr_pos + dice_val} and moved from {curr_pos + dice_val} to {new_pos} ")
        elif object_type == "Ladder":
            print(f"{player_name} rolled a {dice_val} and climbed the ladder at {curr_pos + dice_val} and moved from {curr_pos + dice_val} to {new_pos}")
        elif object_type == "Crocodile":
            print(f"{player_name} rolled a {dice_val} and bitten by crocodile at {curr_pos + dice_val} and moved from {curr_pos + dice_val} to {new_pos}")
        else:
            print(
                f"{player_name} rolled a {dice_val} and moved from {curr_pos} to {new_pos}")
