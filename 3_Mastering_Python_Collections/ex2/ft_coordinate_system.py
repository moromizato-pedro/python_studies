#!/usr/bin/python3

import math


def get_player_pos() -> tuple[float, ...]:
    coords: list[float] = []
    while len(coords) < 3:
        try:
            coord_str = input("Enter new coordinates as floats "
                              "in format 'x,y,z': ")
            if len(coord_str.split(',')) != 3:
                raise SyntaxError("Invalid syntax")
            for coord in coord_str.split(','):
                try:
                    coords.append(float(coord))
                except ValueError as err:
                    print(f"Error on parameter '{coord}': {err}")
                    coords.clear()
                    break
        except SyntaxError as err:
            print(err)
    return (coords[0], coords[1], coords[2])


def euclidian_distance(orig: tuple[float, ...],
                       dist: tuple[float, ...]) -> float:
    dim_orig = len(orig)
    dim_dist = len(dist)
    if dim_orig != dim_dist:
        raise ValueError("Both coordinates must have same dimension!")
    res = 0.0
    for i in range(dim_orig):
        res += math.pow(dist[i] - orig[i], 2)
    return math.sqrt(res)


def print_coord(coord: tuple[float, ...]) -> None:
    coords_label = ('X', 'Y', 'Z')
    print("It includes: ", end='')
    for i in range(len(coord)):
        if i > 0 and i < len(coord):
            print(", ", end='')
        print(f"{coords_label[i]}={coord[i]}", end='')


def main():
    print("=== Game Coordinate System ===")
    center = (0.0, 0.0, 0.0)
    coords = []

#   First set
    print("\nGet a first set of coordinates")
    coords.append(get_player_pos())
    print(f"Got a first tuple: {coords[0]}")
    print_coord(coords[0])
    print(f"\nDistance to center: {euclidian_distance(coords[0], center):.4f}")

#   Second set
    print("\nGet a second set of coordinates")
    coords.append(get_player_pos())
    print("Distance between the 2 sets of coordinates: "
          f"{euclidian_distance(coords[0], coords[1]):.4f}")


if __name__ == "__main__":
    main()
