import random

print("== Game Data Alchemist ===")

players = ['bob', 'Alice', 'dylan', 'Charlie',
           'Emma', 'Gregory', 'john', 'kevin', 'Liam']
print(f"Initial list of players: {players}")

all_capitalized = [player.capitalize() for player in players]
already_capitalized = [player for player in players if player.istitle()]
print(f"New list with all names capitalized: {all_capitalized}")
print(f"New list of capitalized names only: {already_capitalized}\n")

scores = {player: random.randint(0, 999) for player in all_capitalized}
print(f"Score dict: {scores}")

avg = round(sum(scores.values()) / len(scores.keys()), 2)
print(f"Score average is {avg}")

high_scores = {key: value for key, value in scores.items() if value > avg}
print(f"High scores: {high_scores}")
