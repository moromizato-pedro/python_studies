from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


class FactoryError(Exception):
    def __init__(self, message: str = "Unknown FactoryError") -> None:
        super().__init__(message)


#   Abstract Factory
class CreatureFactory(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


#   Concrete Factories
class FlameFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__("Flame")

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__("Aqua")

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
