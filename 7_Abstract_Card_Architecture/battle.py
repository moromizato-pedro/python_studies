#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex0 import Creature, FactoryError


class InvalidFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__("Invalid")

    def create_base(self) -> Creature:
        return None  # type: ignore

    def create_evolved(self) -> Creature:
        return None  # type: ignore


def test_factory(factory: CreatureFactory) -> None:
    ident = "    "
    creation_function = {"Base": factory.create_base,
                         "Evolved": factory.create_evolved}
    for creature_type, function in creation_function.items():
        try:
            creature = function()
            if not isinstance(creature, Creature):
                print(f"{ident}", end='')
                raise FactoryError(f"Couldn't create '{creature_type} "
                                   f"Creature' for '{type(factory).__name__}'")
            print(creature.describe())
            print(creature.attack())
        except FactoryError as err:
            print(f"FactoryError found: {err}")


def test_battle(fire_factory: FlameFactory, aqua_factory: AquaFactory) -> None:
    base_fire = fire_factory.create_base()
    base_water = aqua_factory.create_base()
    print(base_fire.describe())
    print(" vs.")
    print(base_water.describe())
    print(" fight!")
    print(base_fire.attack())
    print(base_water.attack())


def main() -> None:
    fire_factory = FlameFactory()
    water_factory = AquaFactory()
    t_factory = InvalidFactory()

    print("Testing factory")
    test_factory(fire_factory)
    print()
    print("Testing factory")
    test_factory(water_factory)
    print()
    print("Testing invalid factory:")
    test_factory(t_factory)

    print("------------------------")
    print()

    print("Testing battle")
    test_battle(fire_factory, water_factory)
    print()


if __name__ == "__main__":
    main()
