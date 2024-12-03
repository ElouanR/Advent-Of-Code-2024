# Advent of Code 2024 - Day 3 - Part 1
# https://adventofcode.com/2024/day/3#part1

import re

def get_file(file_name: str) -> str:
    file_content = ""

    with open(file_name, "r") as file:
        lines = file.readlines()

    for line in lines:
        file_content += line.strip()

    return file_content

def get_valid_pairs(file: str) -> list:
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, file)
    return matches

def multiply_pairs(pairs: list[tuple]) -> int:
    total = 0

    for pair in pairs:
        total += int(pair[0]) * int(pair[1])

    return total

def main():
    file = get_file("input.txt")
    pairs = get_valid_pairs(file)
    result = multiply_pairs(pairs)

    print(result)

if __name__ == "__main__":
    main()
