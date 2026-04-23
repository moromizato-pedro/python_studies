#!/usr/bin/python3

import sys


def main():
    args = []
    print("=== Player Score Analytics ==")
    try:
        for arg in sys.argv[1:]:
            try:
                args.append(int(arg))
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
        if (len(args) == 0):
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

#   Using time.sleep()
# import time

# def print_output(output: str, res: int | float) -> None:
#     out_str = str(res)
#     prog_out = ""
#     for c in out_str:
#         if not str.isdigit(c):
#             print(output + prog_out + c, end='\r')
#         else:
#             for i in range(10):
#                 print(output + prog_out + str(i), end='\r')
#                 time.sleep(0.1)
#                 if i == int(c):
#                     break
#         prog_out += c
#         if len(prog_out) == len(out_str):
#             print(output + prog_out)

    #   print_output("Total score: ", sum(args))
    #   print_output("Average score: ", sum(args)/len(args))
    #   print_output("High score: ", max(args))
    #   print_output("Low score: ", min(args))
    #   print_output("Score range: ", max(args) - min(args))
