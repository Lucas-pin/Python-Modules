from ex0 import CreatureFactory, FlameFactory, AquaFactory


def create_creature(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def base_creature_fight(creature_a: CreatureFactory,
                        creature_b: CreatureFactory) -> None:
    base_a = creature_a.create_base()
    base_b = creature_b.create_base()
    print(base_a.describe())
    print(" vs.")
    print(base_b.describe())
    print(" fight!")
    print(base_a.attack())
    print(base_b.attack())


def main() -> None:
    print("Testing factory")
    flame_factory = FlameFactory()
    create_creature(flame_factory)

    print("\nTesting factory")
    aqua_factory = AquaFactory()
    create_creature(aqua_factory)

    print("\nTesting battle")
    base_creature_fight(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
