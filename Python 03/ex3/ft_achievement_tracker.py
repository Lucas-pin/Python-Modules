import random

ACHIEVEMENTS = ['Crafting Genius', 'Strategist', 'World Savior',
                'Speed Runner', 'Survivor', 'Master Explorer',
                'Treasure Hunter', 'Unstoppable', 'First Steps',
                'Collector Supreme', 'Untouchable', 'Sharp Mind',
                'Boss Slayer']


def gen_player_achievements() -> set[str]:
    k = random.randint(1, len(ACHIEVEMENTS))
    return set(random.choices(ACHIEVEMENTS, k=k))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print(f"\nAll distintct achievements: "
          f"{set.union(alice, bob, charlie, dylan)}\n")

    print(f"Common achievements: "
          f"{set.intersection(alice, bob, charlie, dylan)}\n")

    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Only Dylan has: {dylan.difference(bob, charlie, alice)}\n")

    print(f"Alice is missing: {set(ACHIEVEMENTS).difference(alice)}")
    print(f"Bob is missing: {set(ACHIEVEMENTS).difference(bob)}")
    print(f"Charlie is missing: {set(ACHIEVEMENTS).difference(charlie)}")
    print(f"Dylan is missing: {set(ACHIEVEMENTS).difference(dylan)}")


if __name__ == "__main__":
    main()
