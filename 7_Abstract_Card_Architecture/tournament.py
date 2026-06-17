from ex0 import Creature, CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy
from ex2 import DeffensiveStrategy, StrategyError


def get_teams(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    FACT, STRAT = 0, 1
    name_strat = [f"({opponent[FACT].name}+{opponent[STRAT].name})"
                  for opponent in opponents]
    formatted = ', '.join([str(tupl).replace("'", "") for tupl in name_strat])
    print(f" [ {formatted} ]")


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    get_teams(opponents)
    creatures: list[tuple[Creature, BattleStrategy]] = []
    for factory, strategy in opponents:
        creatures.append((factory.create_base(), strategy))
    print("*** Tournament ***")
    print(f"{len(creatures)} opponents involved")
    print()

    while creatures:
        creature, strategy = creatures.pop(0)
        for opponent_creature, opponent_strategy in creatures:
            print("* Battle *")
            print(creature.describe())
            print(" vs.")
            print(opponent_creature.describe())
            print(" now fight!")
            try:
                strategy.act(creature)
                opponent_strategy.act(opponent_creature)
            except StrategyError as err:
                print(f"Battle error, aborting tournament: {err}")
                print()
                return
            print()


def main() -> None:
    fire_factory = FlameFactory()
    water_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strat = NormalStrategy()
    aggr_strat = AggressiveStrategy()
    deff_strat = DeffensiveStrategy()
    opponents: list[tuple[CreatureFactory, BattleStrategy]] = []

    opponents = [(fire_factory, normal_strat), (heal_factory, deff_strat)]
    print("Tournament 0 (basic)")
    battle(opponents)

    # No transform + Aggressive
    opponents = [(heal_factory, aggr_strat), (heal_factory, deff_strat)]
    print("Tournament 1.1 (error)")
    battle(opponents)

    # No heal + Deffensive
    opponents = [(transform_factory, deff_strat), (heal_factory, deff_strat)]
    print("Tournament 1.2 (error)")
    battle(opponents)

    opponents = [(water_factory, normal_strat), (heal_factory, deff_strat),
                 (transform_factory, aggr_strat)]
    print("Tournament 2 (multiple)")
    battle(opponents)


if __name__ == "__main__":
    main()
