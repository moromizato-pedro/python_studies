from ex0 import CreatureFactory, Creature
from .capabilities import Sproutling, Bloomelle, Shiftling, Morphagon


#   Concrete Factories
class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__("Healing")

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__("Transform")

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
