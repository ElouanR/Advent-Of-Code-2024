# Advent of Code 2024 - Day 8 - Part 2
# https://adventofcode.com/2024/day/8#part2

import numpy as np

def get_grid(file_name: str) -> np.ndarray:
    """
    Get the grid from the input file.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        grid = file.readlines()

    grid = [list(line.strip()) for line in grid]

    return np.array(grid)

def get_unique_frequencies(grid: np.ndarray) -> np.ndarray:
    """
    Get the unique frequencies from the grid.
    """
    unique_elements = np.unique(grid)
    unique_frequencies = unique_elements[unique_elements != '.']
    return unique_frequencies

def find_antinodes(grid: np.ndarray, unique_frequencies: np.ndarray) -> set[tuple[int, int]]:
    """
    Find the antinodes for each unique frequency.
    """
    antinodes = set()

    for freq in unique_frequencies:
        positions = np.argwhere(grid == freq)

        antinodes.update(map(tuple, positions))

        for i, pos1 in enumerate(positions):
            for pos2 in positions[i + 1:]:
                vector = pos1 - pos2
                antinode1 = pos1 + vector
                antinode2 = pos2 - vector

                while 0 <= antinode1[0] < grid.shape[0] and 0 <= antinode1[1] < grid.shape[1]:
                    antinodes.add(tuple(antinode1))
                    antinode1 += vector

                while 0 <= antinode2[0] < grid.shape[0] and 0 <= antinode2[1] < grid.shape[1]:
                    antinodes.add(tuple(antinode2))
                    antinode2 -= vector

    return antinodes

def main():
    """
    Main function.
    """
    grid = get_grid("input.txt")
    unique_frequencies = get_unique_frequencies(grid)
    antinodes = find_antinodes(grid, unique_frequencies)

    print(len(antinodes))

if __name__ == "__main__":
    main()
