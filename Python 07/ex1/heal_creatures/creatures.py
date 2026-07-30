from ex0 import Creature
from ..abstract import HealCapability


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self, target: str) -> str:
        return f"Sproutling heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self, target: str) -> str:
        return f"Bloomelle heals {target} and others for a large amount"
