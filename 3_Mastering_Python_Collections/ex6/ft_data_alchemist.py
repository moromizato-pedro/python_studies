#!/usr/bin/python3

import random


def main():
    print("=== Game Data Alchemist ===")
    players = [
            "liam", "Noah", "oliver", "James", "elijah", "William", "henry",
            "Lucas", "benjamin", "Theodore", "mateo", "Levi", "sebastian",
            "Daniel", "jack", "Wyatt", "ezra", "Owen", "ethan", "Asher", "leo",
            "Jackson", "mason", "Hudson", "gabriel", "Samuel", "anthony",
            "Grayson", "maverick", "Dylan", "christopher", "Isaac", "miles",
            "Andrew", "thomas", "Joshua", "josiah", "Charles", "caleb",
            "adrian", "Nolan", "easton", "Brooks", "axel", "Walker", "lincoln",
            "Christian", "dominic", "Everett", "amelia", "Olivia", "emma",
            "Charlotte", "sophia", "Mia", "isabella", "Ava", "evelyn", "Luna",
            "harper", "Sofia", "scarlett", "Eleanor", "hazel", "Elizabeth",
            "gianna", "Willow", "alice", "Violet", "aurora", "Penelope",
            "abigail", "Chloe", "layla", "Nora", "zoey", "Riley", "lily",
            "Iris", "emilia", "Eliana", "serenity", "Stella", "maya",
            "Victoria", "hannah", "Bella", "quinn", "Nova", "ivy", "Grace",
            "zoe", "Emery", "kinsley", "Delilah", "madeline", "Sophie"
        ]
    print(f"\nInitial list of players: {players}")
    capitalize_all = [x.capitalize() for x in players]
    print(f"New list with all names capitalized: {capitalize_all}")
    only_capitalized = [x for x in players if x.istitle()]
    print(f"New list of capitalized names only: {only_capitalized}")
    scored_dict = {name: random.randrange(1000) for name in capitalize_all}
    print(f"Score dict: {scored_dict}")
    avg_score = sum(scored_dict.values())/len(scored_dict)
    print(f"Score average is {avg_score:.2f}")
    high_scores = {name: score for name, score in scored_dict.items()
                   if score > avg_score}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
