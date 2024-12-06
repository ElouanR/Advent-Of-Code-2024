# Advent of Code 2024 - Day 6 - Part 1
# https://adventofcode.com/2024/day/6#part1

import numpy as np

def get_map(file_name: str) -> np.ndarray[list[str]]:
    """
    Get the map from the file.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = np.array([list(line.strip()) for line in lines])

    return lines

def find_guard_position(map_data: np.ndarray[list[str]]) -> tuple:
    """
    Find the guard's position on the map.
    """
    for i, row in enumerate(map_data):
        for j, value in enumerate(row):
            if value == "^":
                return (j, i)

    return None

def patrol_path(map_data: np.ndarray[list[str]]) -> np.ndarray[list[str]]:
    """
    Simulate the guard's patrol on the map, marking the path taken.
    """
    x, y = find_guard_position(map_data)

    while y >= 0:
        while map_data[y - 1][x] == "#":
            map_data[y][x] = "^"
            map_data = np.rot90(map_data)
            x, y = find_guard_position(map_data)

        map_data[y][x] = "X"
        y -= 1

    return map_data

def main():
    """
    Main function.
    """
    map_data = get_map("input.txt")
    map_data = patrol_path(map_data)
    result = np.count_nonzero(map_data == "X")

    print(result)

if __name__ == "__main__":
    main()
