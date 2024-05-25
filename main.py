import argparse
import os
import json
from src.game import Game
from src.movement_strategy import StrategyOption


def read_file(file_path):
    if not os.path.isfile(file_path):
        raise Exception(f"Error: The file '{file_path}' does not exist.")

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError:
        raise Exception(
            f"Error: The file '{file_path}' is not a valid JSON file.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process a file or take user input if no file is provided.")
    parser.add_argument('-f', '--file', type=str,
                        help="Path to the input file")

    args = parser.parse_args()

    if args.file:
        data = read_file(args.file)
        if data is not None:
            print(f"Data from file:\n {data}")
        board_size = data["board_size"]
        num_players = data["num_players"]
        num_snakes = data["num_snakes"]
        num_ladders = data["num_ladders"]
        num_dice = data["num_dice"]
        num_crocs = data["num_crocs"]
        num_mines = data["num_mines"]
        movement_strategy = data["movement_strategy"]
    else:
        board_size = input("Enter the size of the board (BS): ")
        print(board_size)

        num_dice = input("Enter the number of dice (D): ")
        print(num_dice)

        num_snakes = input("Enter the Number of Snakes (S): ")
        print(num_snakes)
        snakes = []
        for i in range(int(num_snakes)):
            snakes.append(tuple(map(int, input().split())))

        num_ladders = input("Enter the Number of Ladders (L): ")
        print(num_ladders)
        ladders = []
        for i in range(int(num_ladders)):
            ladders.append(tuple(map(int, input().split())))

        num_crocs = input("Enter the number of Crocodiles (C): ")
        print(num_crocs)
        crocs = []
        for i in range(int(num_crocs)):
            crocs.append(int(input()))

        num_mines = input("Enter the Number of mines (M): ")
        print(num_mines)
        mines = []
        for i in range(int(num_mines)):
            mines.append(int(input()))

        num_players = input("Enter the Number of players (N): ")
        print(num_players)
        players = []
        for i in range(int(num_players)):
            players.append(input())

        strategy_option_input = input(
            "Select the movement strategy (MS): \n1.SUM (sum of numbers on dice)\n2.MAX (max of numbers on dice)\n3.MIN (min of number on dice)")
        print("\n")
        try:
            strategy_option = StrategyOption(int(strategy_option_input))
        except ValueError:
            raise ValueError("Invalid strategy option selected")

    game = Game(int(board_size), int(num_dice), strategy_option.get_strategy())
    game.set_players(players)
    game.set_special_objects(ladders, snakes, crocs, mines)
    game.start_game()
