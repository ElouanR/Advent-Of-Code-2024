# Advent of Code 2024 - Day 1 - Part 1
# https://adventofcode.com/2024/day/1#part1

def get_lines(file_name: str) -> list:
    with open(file_name, "r") as file:
        lines = file.readlines()

    return lines

def get_lists(lines: list) -> tuple[list, list]:
    list1 = []
    list2 = []

    for line in lines:
        pair = line.strip().split("   ")
        list1.append(int(pair[0]))
        list2.append(int(pair[1]))

    return list1, list2

def get_distance(list1: list, list2: list) -> int:
    distance = 0

    while list1 and list2:
        nb1 = min(list1)
        nb2 = min(list2)
        distance += max(nb1, nb2) - min(nb1, nb2)
        list1.remove(nb1)
        list2.remove(nb2)

    return distance

def main():
    lines = get_lines("input.txt")
    list1, list2 = get_lists(lines)
    distance = get_distance(list1, list2)

    print(distance)

if __name__ == "__main__":
    main()
