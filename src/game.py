from src.player import Player
from src.dice import Dice
from src.board import Board
from src.snake import Snake
from src.ladder import Ladder
from src.crocodile import Crocodile
from src.mine import Mine
from src.movement_strategy import MovementStrategy
from typing import List, Dict
import sys


class Game:
    def __init__(self, board_size, num_of_dice, movement_strategy: MovementStrategy) -> None:
        self.players: Dict[str, Player] = {}
        self.active_players = 0
        self.dice = Dice(6, num_of_dice=num_of_dice,
                         strategy=movement_strategy)
        self.board = Board(board_size)
        self.curr_win_position = 0

    def set_players(self, players: List[str]):
        self.active_players = len(players)
        if self.active_players < 2:
            raise Exception(
                'Not enough players. At least 2 players are required.'
            )

        for player in players:
            self.players[player] = Player(player)

    def get_player(self, player_name):
        return self.players[player_name]

    def update_player(self, player: Player):
        self.players[player.name] = player

    def set_special_objects(self, ladders, snakes, crocodiles=[], mines=[]):
        # set Snakes
        for head, tail in snakes:
            snake = Snake(head, tail)
            self.board.set_snake(snake)

        # set Ladders
        for start, end in ladders:
            ladder = Ladder(start, end)
            self.board.set_ladder(ladder)

        # set Crocs
        for pos in crocodiles:
            croc = Crocodile(pos)
            self.board.set_crocodile(croc)

        # set Mines
        for location in mines:
            mine = Mine(location)
            self.board.set_mine(mine)

    # Function to manually input dice_val for testing.
    def start_game(self):
        while True:
            for _, player in self.players.items():
                dice_val = self.dice.roll_dice()
                self.play_game(player, dice_val)

    def play_game(self, player: Player, dice_val: int):
        if not player.get_win_status():
            # Unset the player from the board.
            self.board.unset_player(player)

            # Play the player if not a winner.
            init_pos = player.get_position()
            final_pos = self.board.get_next_position(
                player,
                dice_val,
                init_pos,
            )
            # If the curr position has mine, then decrement the turns_held
            if not player.can_move():
                player.decrement_turns_held()
            else:
                player.set_position(final_pos)
                curr_pos = player.get_position()

                if self.board.check_mine(curr_pos):
                    turns_held = self.board.get_mine_turns_held(curr_pos)
                    player.set_turns_held(turns_held)

                if self.board.check_player_status(curr_pos):
                    self.curr_win_position += 1
                    player.set_win_status(True)
                    player.set_player_position(self.curr_win_position)
                    self.active_players -= 1

                if self.board.check_other_players(curr_pos):
                    other_player = self.board.get_player_in_pos(curr_pos)
                    other_player.reset_position()
                    self.update_player(other_player)

            # Setting a player in the curr position.
            self.board.set_player(player)
            self.update_player(player)

        if self.active_players < 2:
            print('\nGame Over! Game positions are:')
            sorted_players = sorted(self.players.values(), key=lambda x: (
                x.get_player_position() if x.get_player_position() != -1 else float('inf')))

            for player in sorted_players:
                if player.get_player_position() == -1:
                    print(f"Loser: {player.get_player_name()}")
                else:
                    print(f"{player.get_player_position()}. {player.get_player_name()}")

            sys.exit(1)
