#!/usr/bin/python3

import sys


def validate_args() -> list[int]:
    args = []
    for arg in sys.argv[1:]:
        try:
            args.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return args


def main() -> None:
    print("=== Player Score Analytics ==")
    try:
        args = validate_args()
        if len(args) == 0:
            raise ValueError
        print(f"Scores processed: {args}")
        print(f"Total players: {len(args)}")
        print(f"Total score: {sum(args)}")
        print(f"Average score: {sum(args)/len(args)}")
        print(f"High score: {max(args)}")
        print(f"Low score: {min(args)}")
        print(f"Score range: {max(args) - min(args)}\n")
    except ValueError:
        print("No scores provided. Usage python3 "
              "ft_score_analytics.py <score1> <score2> ...\n")


if __name__ == "__main__":
    main()
