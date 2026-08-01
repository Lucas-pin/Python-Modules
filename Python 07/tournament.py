from ex0 import FlameFactory, AquaFactory, CreatureFactory, Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy
from ex2 import AggressiveStrategy, DefensiveStrategy


def create_factories(factory: CreatureFactory) -> Creature:
    return factory.create_base()


def single_battle(opponents: list[tuple[Creature, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()
    try:
        for creature, strategy in opponents:
            others = opponents
            for other_creature, other_strategy in others:
                if creature is other_creature:
                    continue
                print("* Battle *")
                print(other_creature.describe())
                print(" vs")
                print(creature.describe())
                print(" now fight!")
                other_strategy.act(other_creature)
                strategy.act(creature)
                print()
    except Exception as ex:
        print(f"Battle error, aborting tournament: {ex}")


def main() -> None:
    flameling = create_factories(FlameFactory())
    aquabub = create_factories(AquaFactory())
    sproutling = create_factories(HealingCreatureFactory())
    shiftling = create_factories(TransformCreatureFactory())

    normal = NormalStrategy()
    agressive = AggressiveStrategy()
    defensive = DefensiveStrategy()
    single_battle([(flameling, normal), (sproutling, defensive)])
    single_battle([(flameling, agressive), (sproutling, defensive)])
    single_battle([(aquabub, normal),
                   (sproutling, defensive),
                   (shiftling, agressive)])


if __name__ == "__main__":
    main()
