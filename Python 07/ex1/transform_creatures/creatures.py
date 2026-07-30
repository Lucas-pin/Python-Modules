from ex0 import Creature
from ..abstract import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type: str):
        Creature.__init__(self, name, type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally."

    def transform(self) -> str:
        if not self.transformed:
            self.transformed = True
            return "Shiftling shifts into a sharper form!"
        else:
            return "Shiftling it's already transformed"

    def revert(self) -> str:
        if self.transformed:
            self.transformed = False
            return "Shiftling returns to normal."
        else:
            return "Shiftling it's already reverted"


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type: str):
        Creature.__init__(self, name, type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return "Morphagon performs a boosted strike!"
        else:
            return "Morphagon unleashes a devastating morph strike!"

    def transform(self) -> str:
        if not self.transformed:
            self.transformed = True
            return "Morphagon morphs into a dragonic battle form!"
        else:
            return "Morphagon it's already transformed"

    def revert(self) -> str:
        if self.transformed:
            self.transformed = False
            return "Morphagon stabilizes its form."
        else:
            return "Morphagon it's already reverted"
