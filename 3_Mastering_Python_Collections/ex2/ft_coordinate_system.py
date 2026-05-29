#!/usr/bin/python3

import math


def pow(base: float, power: int) -> float:
    while power > 1:
        base *= base
    return base


def parse_arguments(coord_str: str) -> list[float]:
    coords: list[float] = []
    for coord in coord_str.split(','):
        try:
            coords.append(float(coord))
        except ValueError as err:
            print(f"Error on parameter '{coord}': {err}")
            coords.clear()
            break
    return coords


def get_player_pos() -> tuple[float, float, float]:
    coords: list[float] = []
    while len(coords) < 3:
        try:
            coord_str = input("Enter new coordinates as floats "
                              "in format 'x,y,z': ")
            if len(coord_str.split(',')) != 3:
                raise ValueError("Invalid syntax")
            coords = parse_arguments(coord_str)
        except ValueError as err:
            print(err)
    return (coords[0], coords[1], coords[2])


def print_coords(coords: tuple[float, float, float]) -> None:
    print(f"It includes: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")


def main() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    coords = get_player_pos()
    print(f"Got a first tuple: {coords}")
    x1, y1, z1 = coords
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: "
          f"{round(math.sqrt((x1-0)**2 + (y1-0)**2 + (z1-0)**2), 4)}")

    print("\nGet a second set of coordinates")
    x2, y2, z2 = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{round(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 4)}")


if __name__ == "__main__":
    main()
