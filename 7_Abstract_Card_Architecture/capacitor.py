from ex0 import FactoryError, Creature, CreatureFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1 import HealCapability, TransformCapability


class InvalidFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__("Invalid")

    def create_base(self) -> Creature:
        return None  # type: ignore

    def create_evolved(self) -> Creature:
        return None  # type: ignore


def test_creature(creature: Creature, creature_type: str) -> None:
    print(f" {creature_type}:")
    print(creature.describe())
    if isinstance(creature, HealCapability):
        print(creature.attack())
        print(creature.heal())
    elif isinstance(creature, TransformCapability):
        print(creature.attack())
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
    else:
        raise FactoryError(f"{creature_type} Creature has no capabilities")


def test_factory(factory: CreatureFactory) -> None:
    creation_function = {"base": factory.create_base,
                         "evolved": factory.create_evolved}
    for creature_type, function in creation_function.items():
        try:
            creature = function()
            if not isinstance(creature, Creature):
                raise FactoryError(f"Couldn't create "
                                   f"'{creature_type.capitalize()} Creature' "
                                   f"for '{type(factory).__name__}'")
            test_creature(creature, creature_type)
        except FactoryError as err:
            print(f"FactoryError found: {err}")


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    t_creature = InvalidFactory()
    water_factory = AquaFactory()

    print("=Testing Creature with healing capability")
    test_factory(healing_factory)
    print()
    print("=Testing Creature with transform capability")
    test_factory(transform_factory)
    print()
    print("=Testing invalid Creature")
    test_factory(t_creature)
    test_factory(water_factory)
    print()


if __name__ == "__main__":
    main()
