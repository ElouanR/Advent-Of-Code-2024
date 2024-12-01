# Advent of Code 2024 - Day 1 - Part 2
# https://adventofcode.com/2024/day/1#part2

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

def get_similarity_score(list1: list, list2: list) -> int:
    similarity_score = 0

    for i in range(len(list1)):
        nb = list1[i]
        similarity_score += nb * list2.count(nb)

    return similarity_score

def main():
    lines = get_lines("input.txt")
    list1, list2 = get_lists(lines)
    similarity_score = get_similarity_score(list1, list2)

    print(similarity_score)

if __name__ == "__main__":
    main()
