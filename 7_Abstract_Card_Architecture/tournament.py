from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import HealCapability, TransformCapability


class BattleStrategy(ABC):

    @abstractmethod
    def act(self) -> None:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self) -> None:
        if self.is_valid():
            if isinstance(self, Creature):
                self.attack()

    def is_valid(self) -> bool:
        if isinstance(self, Creature):
            return True
        return False


class AggressiveStrategy(BattleStrategy):
    def act(self) -> None:
        if self.is_valid():
            if isinstance(self, Creature):
                if isinstance(self, TransformCapability):
                    self.transform()
                    self.attack()
                    self.revert()

    def is_valid(self) -> bool:
        if isinstance(self, (Creature, TransformCapability)):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def act(self) -> None:
        if self.is_valid():
            if isinstance(self, Creature):
                if isinstance(self, HealCapability):
                    self.attack()
                    self.heal()

    def is_valid(self) -> bool:
        if isinstance(self, (Creature, HealCapability)):
            return True
        return False
