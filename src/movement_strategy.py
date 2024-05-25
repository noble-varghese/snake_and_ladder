from __future__ import annotations
from abc import abstractmethod
from enum import Enum


class StrategyOption(Enum):
    SUM = 1
    MAX = 2
    MIN = 3

    def get_strategy(self) -> MovementStrategy:
        if self == StrategyOption.SUM:
            return Sum()
        elif self == StrategyOption.MAX:
            return Max()
        elif self == StrategyOption.MIN:
            return Min()
        else:
            raise ValueError("Invalid strategy option selected")


class MovementStrategy:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def calculate_score(self, values) -> int:
        """"""


class Sum(MovementStrategy):
    def __init__(self) -> None:
        super().__init__()

    def calculate_score(self, values) -> int:
        return sum(values)


class Max(MovementStrategy):
    def __init__(self) -> None:
        super().__init__()

    def calculate_score(self, values) -> int:
        return max(values)


class Min(MovementStrategy):
    def __init__(self) -> None:
        super().__init__()

    def calculate_score(self, values) -> int:
        return min(values)
