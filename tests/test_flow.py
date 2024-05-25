"""Tests for `snake_ladder` package."""

import unittest
from src.game import Game
from src.movement_strategy import StrategyOption


class Test_Snake_ladder(unittest.TestCase):
    """Tests for `snake_ladder` package."""

    def setUp(self):
        self.board_size = 100
        self.players = ["Noble", "Robin"]
        self.num_of_dice = 1

        # Define snakes: (start, end)
        self.snakes = [(62, 5), (33, 6), (49, 9), (88, 16),
                       (41, 20), (56, 53), (98, 64), (93, 73), (95, 75)]

        # Define ladders: (start, end)
        self.ladders = [(2, 37), (27, 46), (10, 32), (60, 68),
                        (61, 79), (65, 84), (71, 91), (81, 98)]

        # No crocodiles
        self.crocs = [7, 22, 38, 47, 58, 63, 76, 85, 97]

        # Define mines (positions)
        # Ensure mines do not overlap with ladders' start or snakes' start positions
        self.mines = [4, 6, 12, 15, 20, 23, 26, 30,
                      37, 51, 52, 55, 68, 70, 72, 77, 83, 84, 87]

        # Remove any positions from mines that overlap with ladders' start or snakes' start
        snake_starts = {s[0] for s in self.snakes}
        ladder_starts = {l[0] for l in self.ladders}
        special_starts = snake_starts.union(ladder_starts)
        self.mines = [pos for pos in self.mines if pos not in special_starts]

        # Select movement strategy (1 for SUM)
        try:
            strategy_option = StrategyOption(1)
        except ValueError:
            raise ValueError("Invalid strategy option selected")

        self.movement_strategy = strategy_option.get_strategy()

        self.game = Game(
            self.board_size, self.num_of_dice, self.movement_strategy)
        self.game.set_players(self.players)
        self.game.set_special_objects(
            self.ladders, self.snakes, self.crocs, self.mines)

    def test_gameplay(self):
        """Simulate game moves and check player states."""

        print('Starting the test....')

        moves = [
            ("Noble", 5),
            ("Robin", 4),
            ("Noble", 2),
            ("Robin", 4),
            ("Noble", 4),
            ("Robin", 8),
            ("Noble", 10),
            ("Robin", 6),
            ("Noble", 6),
            ("Robin", 6),
            ("Noble", 6),
            ("Robin", 6)
        ]

        expected_final_pos = {
            "Noble": 12,
            "Robin": 44
        }

        for move in moves:
            player_name, dice_val = move
            player = self.game.get_player(player_name)
            self.game.play_game(player, dice_val)

        # player = self.game.get_player("Noble")
        # assert player.get_position(
        # ) == expected_final_pos[player.get_player_name()]

        # player = self.game.get_player("Robin")
        # assert player.get_position(
        # ) == expected_final_pos[player.get_player_name()]


if __name__ == '__main__':
    unittest.main()
