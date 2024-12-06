# Advent of Code 2024 - Day 6 - Part 2
# https://adventofcode.com/2024/day/6#part2

import enum
from multiprocessing import Pool
import numpy as np

class Direction(enum.Enum):
    """
    Direction enum.
    """
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Map:
    """
    Map class.
    """
    def __init__(self, file_name: str):
        self.data = self.get_map(file_name)

    def get_map(self, file_name: str) -> np.ndarray[list[str]]:
        """
        Get the map from the file.
        """
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        lines = np.array([list(line.strip()) for line in lines])

        return lines

    def set_obstacle(self, position: tuple[int, int]) -> bool:
        """
        Set an obstacle on the map.
        """
        if self.data[position[0]][position[1]] == "^":
            return False

        self.data[position[0]][position[1]] = "#"
        return True

class Guard:
    """
    Guard class.
    """
    def __init__(self, map_object: Map):
        self.map_object = map_object
        self.position = self.get_position(self.map_object.data)
        self.direction = Direction.NORTH

    def get_position(self, map_data: np.ndarray[list[str]]) -> tuple[int, int]:
        """
        Find the guard's position on the map.
        """
        position = np.argwhere(map_data == "^")

        if position.size > 0:
            return (position[0][0].item(), position[0][1].item())
        raise ValueError("Guard not found")

    def switch_direction(self):
        """
        Switch the guard's direction.
        """
        self.direction = Direction((self.direction.value + 1) % 4)

    def move(self) -> tuple[tuple[int, int], Direction] | None:
        """
        Move the guard.
        """
        while True:
            match self.direction:
                case Direction.NORTH:
                    if self.position[0] <= 0:
                        return None

                    if self.map_object.data[self.position[0] - 1][self.position[1]] == "#":
                        self.switch_direction()
                        continue

                    new_position = (self.position[0] - 1, self.position[1])

                case Direction.EAST:
                    if self.position[1] >= self.map_object.data.shape[1] - 1:
                        return None

                    if self.map_object.data[self.position[0]][self.position[1] + 1] == "#":
                        self.switch_direction()
                        continue

                    new_position = (self.position[0], self.position[1] + 1)

                case Direction.SOUTH:
                    if self.position[0] >= self.map_object.data.shape[0] - 1:
                        return None

                    if self.map_object.data[self.position[0] + 1][self.position[1]] == "#":
                        self.switch_direction()
                        continue

                    new_position = (self.position[0] + 1, self.position[1])

                case Direction.WEST:
                    if self.position[1] <= 0:
                        return None

                    if self.map_object.data[self.position[0]][self.position[1] - 1] == "#":
                        self.switch_direction()
                        continue

                    new_position = (self.position[0], self.position[1] - 1)

            self.position = new_position
            return self.position, self.direction

def get_original_path(map_object: Map) -> set[tuple[int, int]]:
    """
    Get the original path.
    """
    path = set()
    guard = Guard(map_object)

    while True:
        move = guard.move()
        if move is None:
            break
        position, _ = move
        path.add(position)

    return path

def is_circular_path(args) -> bool:
    """
    Check if the path is a loop.
    """
    position, map_object = args

    if map_object.set_obstacle(position):
        moves = set()
        guard = Guard(map_object)

        while True:
            move = guard.move()

            if move is None:
                return False
            if move in moves:
                return True

            moves.add(move)

    return False

def simulate_obstructed_paths(map_object: Map, original_path: set[tuple[int, int]]) -> int:
    """
    Parallel simulation of obstructed paths.
    """
    args = [(pos, map_object) for pos in original_path]

    with Pool() as pool:
        results = pool.imap_unordered(is_circular_path, args)
        count = sum(1 for is_circular in results if is_circular)

    return count

def main():
    """
    Main function.
    """
    map_object = Map("input.txt")
    original_path = get_original_path(map_object)
    number_of_obstructed_paths = simulate_obstructed_paths(map_object, original_path)

    print(number_of_obstructed_paths)

if __name__ == "__main__":
    main()
