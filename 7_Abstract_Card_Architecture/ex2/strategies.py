from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import HealCapability, TransformCapability
from typing import Any, cast


class StrategyError(Exception):
    def __init__(self, message: str = "Unknown BattleError") -> None:
        super().__init__(message)


# Abstract Product
class BattleStrategy(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def act(self, creature: Any) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        pass


# Concrete Products
class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("Normal")

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError("Invalid creature "
                                f"'{creature.name}' for this "
                                "normal strategy")
        print(creature.attack())

    def is_valid(self, creature: Any) -> bool:
        if isinstance(creature, Creature):
            return True
        return False


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("Aggressive")

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError("Invalid creature "
                                f"'{creature.__class__.__name__}' for this"
                                " aggressive strategy")
        tc = cast(TransformCapability, creature)
        print(tc.transform())
        print(creature.attack())
        print(tc.revert())

    def is_valid(self, creature: Any) -> bool:
        classes = [Creature, TransformCapability]
        if all(isinstance(creature, clas) for clas in classes):
            return True
        return False


class DeffensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("Defensive")

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError("Invalid creature "
                                f"'{creature.__class__.__name__}' for this"
                                " deffensive strategy")
        tc = cast(HealCapability, creature)
        print(creature.attack())
        print(tc.heal())

    def is_valid(self, creature: Any) -> bool:
        classes = [Creature, HealCapability]
        if all(isinstance(creature, clas) for clas in classes):
            return True
        return False
