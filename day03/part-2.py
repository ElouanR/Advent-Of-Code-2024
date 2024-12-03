# Advent of Code 2024 - Day 3 - Part 2
# https://adventofcode.com/2024/day/3#part2

import re

def get_file(file_name: str) -> str:
    file_content = ""

    with open(file_name, "r") as file:
        lines = file.readlines()

    for line in lines:
        file_content += line.strip()

    return file_content

def get_instructions(file: str) -> list:
    patterns = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
    matches = re.findall(patterns, file)
    instructions = []

    for match in matches:
        if match[0] and match[1]:
            instructions.append((match[0], match[1]))
        elif match[2]:
            instructions.append("do()")
        elif match[3]:
            instructions.append("don't()")

    return instructions

def compute_instructions(instructions: list) -> int:
    do = True
    total = 0

    for instruction in instructions:
        if instruction == "do()":
            do = True
        elif instruction == "don't()":
            do = False
        elif do:
            total += int(instruction[0]) * int(instruction[1])

    return total

def main():
    file = get_file("input.txt")
    instructions = get_instructions(file)
    result = compute_instructions(instructions)

    print(result)

if __name__ == "__main__":
    main()
