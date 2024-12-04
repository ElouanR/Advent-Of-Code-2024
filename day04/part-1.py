# Advent of Code 2024 - Day 4 - Part 1
# https://adventofcode.com/2024/day/4#part1

import numpy as np

def get_lines(file_name: str) -> list[list]:
    with open(file_name, "r") as file:
        lines = file.readlines()

    lines = [(line.strip()) for line in lines]
    board = np.array([list(line) for line in lines])

    lines = board.tolist()
    lines.extend(board.T.tolist())

    for offset in range(-board.shape[0] + 1, board.shape[1]):
        lines.append(np.diagonal(board, offset=offset).tolist())

    flipped_board = np.fliplr(board)
    for offset in range(-flipped_board.shape[0] + 1, flipped_board.shape[1]):
        lines.append(np.diagonal(flipped_board, offset=offset).tolist())

    return lines

def count_xmas(lines: list[list]) -> int:
    count = 0

    patterns = ["XMAS", "SAMX"]

    for line in lines:
        line_str = "".join(map(str, line))
        for pattern in patterns:
            count += line_str.count(pattern)

    return count

def main():
    lines = get_lines("input.txt")
    count = count_xmas(lines)

    print(count)

if __name__ == "__main__":
    main()
