from ex2 import BattleStrategy
from ex0 import Creature
import typing


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        required_methods = ['attack']
        return all(callable(getattr(creature, method, None))
                   for method in required_methods)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(f"Invalid Creature '{creature._name}' "
                            "for this normal strategy")
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        required_methods = ['attack', 'transform', 'revert']
        return all(callable(getattr(creature, method, None))
                   for method in required_methods)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(f"Invalid Creature '{creature._name}' "
                            "for this agressive strategy")

        casted_creature = typing.cast(typing.Any, creature)
        print(casted_creature.transform())
        print(casted_creature.attack())
        print(casted_creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        required_methods = ['attack', 'heal']
        return all(callable(getattr(creature, method, None))
                   for method in required_methods)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(f"Invalid Creature '{creature._name}' "
                            "for this defensive strategy")

        casted_creature = typing.cast(typing.Any, creature)
        print(casted_creature.attack())
        print(casted_creature.heal("itself"))
