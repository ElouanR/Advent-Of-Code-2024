# Advent of Code 2024 - Day 4 - Part 2
# https://adventofcode.com/2024/day/4#part2

import numpy as np

def get_lines(file_name: str) -> list[list]:
    with open(file_name, "r") as file:
        lines = file.readlines()

    lines = [(line.strip()) for line in lines]
    lines = np.array([list(line) for line in lines])

    return lines

def check_mas_x(lines: list[list], x: int, y: int) -> bool:
    if y <= 0 or y >= len(lines) - 1 or x <= 0 or x >= len(lines[y]) - 1:
        return False

    if lines[y - 1][x - 1] == "M" and lines[y + 1][x + 1] == "S" and lines[y - 1][x + 1] == "M" and lines[y + 1][x - 1] == "S":
        return True

    if lines[y - 1][x - 1] == "S" and lines[y + 1][x + 1] == "M" and lines[y - 1][x + 1] == "S" and lines[y + 1][x - 1] == "M":
        return True

    if lines[y - 1][x - 1] == "M" and lines[y + 1][x + 1] == "S" and lines[y - 1][x + 1] == "S" and lines[y + 1][x - 1] == "M":
        return True

    if lines[y - 1][x - 1] == "S" and lines[y + 1][x + 1] == "M" and lines[y - 1][x + 1] == "M" and lines[y + 1][x - 1] == "S":
        return True

    return False

def count_mas_x(lines: list[list]) -> int:
    count = 0

    for y in range(len(lines)):
        for x in range(len(lines[y]) - 1):
            if lines[y][x] == "A":
                if check_mas_x(lines, x, y):
                    count += 1

    return count

def main():
    lines = get_lines("input.txt")
    count = count_mas_x(lines)

    print(count)

if __name__ == "__main__":
    main()
