from ex1 import HealingCreatureFactory, TransformCreatureFactory


def healing_creature_factory(factory: HealingCreatureFactory) -> None:
    print(" base:")
    sproutling = factory.create_base()
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal("itself"))

    print(" evolved:")
    bloomelle = factory.create_evolved()
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal("itself"))


def transform_creature_factory(factory: TransformCreatureFactory) -> None:
    print(" base:")
    shiftling = factory.create_base()
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())

    print(" evolved:")
    morphagon = factory.create_evolved()
    print(morphagon.describe())
    print(morphagon.attack())
    print(morphagon.transform())
    print(morphagon.attack())
    print(morphagon.revert())


def main() -> None:
    print("Testing Creature with healing capability")
    healing_creature_factory(HealingCreatureFactory())

    print("Testing Creature with transform capability")
    transform_creature_factory(TransformCreatureFactory())


if __name__ == "__main__":
    main()
