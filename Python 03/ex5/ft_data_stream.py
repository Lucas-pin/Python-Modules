import random
import typing

ACTIONS = ['eat', 'run', 'sleep', 'climb', 'grab', 'move', 'swim']
PLAYERS = ['bob', 'alice', 'dylan', 'charlie']


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield random.choice(PLAYERS), random.choice(ACTIONS)


def consume_event(events: list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        random_event = random.choice(events)
        events.remove(random_event)
        yield random_event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    events = gen_event()
    for n in range(1000):
        try:
            player, action = next(events)
            print(f"Event {n}: Player {player} did action {action}")
        except (StopIteration):
            print("There are no more events to generate.")

    list_events = [next(events) for _ in range(10)]
    print(f"Built list of {len(list_events)} events: {list_events}")

    for event in consume_event(list_events):
        print(f"Got event from list: {event}")
        print(f"Remain in list: {list_events}")


if __name__ == "__main__":
    main()
