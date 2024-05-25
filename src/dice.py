import random
from src.movement_strategy import MovementStrategy


class Dice:
    def __init__(self, faces=6, num_of_dice=1, strategy: MovementStrategy = None) -> None:
        if num_of_dice == 0:
            raise Exception("There must be atleast one dice!")

        self.faces = faces
        self.num_of_dice = num_of_dice
        self.movement_strategy = strategy

    def roll_dice(self) -> int:
        scores = []
        count = 0

        while True:
            if count >= self.num_of_dice:
                break

            rand_val = random.randint(1, self.faces)
            count += 1
            scores.append(rand_val)

        return self.get_score(scores)

    def get_score(self, scores) -> int:
        return self.movement_strategy.calculate_score(scores)
