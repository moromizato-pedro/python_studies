#!/usr/bin/python3

from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = [
        "Liam", "Noah", "Oliver", "James", "Elijah", "William", "Henry",
        "Lucas", "Benjamin", "Theodore", "Mateo", "Levi", "Sebastian",
        "Daniel", "Jack", "Wyatt", "Ezra", "Owen", "Ethan", "Asher", "Leo",
        "Jackson", "Mason", "Hudson", "Gabriel", "Samuel", "Anthony",
        "Grayson", "Maverick", "Dylan", "Christopher", "Isaac", "Miles",
        "Andrew", "Thomas", "Joshua", "Josiah", "Charles", "Caleb", "Adrian",
        "Nolan", "Easton", "Brooks", "Axel", "Walker", "Lincoln", "Christian",
        "Dominic", "Everett", "Amelia", "Olivia", "Emma", "Charlotte",
        "Sophia", "Mia", "Isabella", "Ava", "Evelyn", "Luna", "Harper",
        "Sofia", "Scarlett", "Eleanor", "Hazel", "Elizabeth", "Gianna",
        "Willow", "Alice", "Violet", "Aurora", "Penelope", "Abigail",
        "Chloe", "Layla", "Nora", "Zoey", "Riley", "Lily", "Iris", "Emilia",
        "Eliana", "Serenity", "Stella", "Maya", "Victoria", "Hannah",
        "Bella", "Quinn", "Nova", "Ivy", "Grace", "Zoe", "Emery", "Kinsley",
        "Delilah", "Madeline", "Sophie"
    ]
    actions = [
        "jumped", "sprinted", "dodged", "climbed", "ducked", "swam", "looted",
        "crafted", "healed", "drove", "flew", "crawled", "teleported",
        "kicked", "punched", "blocked", "parried", "countered", "shouted",
        "whispered", "danced", "waved", "bowed", "saluted", "slept", "ate",
        "drank", "built", "destroyed", "mined", "fished", "hunted", "trapped",
        "sneaked", "hid", "searched", "inspected", "read", "wrote", "cast",
        "chanted", "summoned", "banished", "charged", "retreated",
        "surrendered", "laughed", "cried", "sighed", "blinked", "stared",
        "pointed", "grabbed", "threw", "caught", "rolled", "slid", "vaulted",
        "leaped", "dashed", "waited", "rested", "meditated", "prayed",
        "donated", "traded", "bought", "sold", "equipped", "dropped",
        "ignited", "extinguished", "pushed", "pulled", "rotated", "flipped",
        "locked", "unlocked", "opened", "closed", "scanned", "hacked",
        "repaired", "upgraded", "dismantled", "scavenged", "planted",
        "harvested", "cooked", "brewed", "smelted", "sharpened", "polished",
        "cleaned", "painted", "decorated", "tamed", "mounted", "whistled",
        "clapped"
    ]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events: list) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        selected = random.choice(events)
        events.remove(selected)
        yield selected


def main():
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        player, action = next(gen)
        print(f"Event {i}: Player {player} did action {action}")
    events_10 = [next(gen) for _ in range(10)]
    print(f"Built list of 10 events: {events_10}")
    for event in consume_event(events_10):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_10}")


if __name__ == "__main__":
    main()
