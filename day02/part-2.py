# Advent of Code 2024 - Day 2 - Part 2
# https://adventofcode.com/2024/day/2#part2

def get_lines(file_name: str) -> list:
    with open(file_name, "r") as file:
        lines = file.readlines()

    return lines

def get_lists(lines: str) -> list[list]:
    lists = []

    for line in lines:
        lists.append(line.strip().split(' '))

    return lists

def is_safe(list: list) -> bool:
    decrease = True if int(list[0]) > int(list[1]) else False
    safe = True

    for i in range(len(list) - 1):
        n1 = int(list[i])
        n2 = int(list[i + 1])
        s = abs(n1 - n2)

        if decrease and n1 > n2 and s <= 3 and s >= 1:
            continue
        elif not decrease and n1 < n2 and s <= 3 and s >=1:
            continue
        else:
            safe = False
            break

    return safe

def build_lists(list: list) -> list[list]:
    lists = []

    lists.append(list)

    for i in range(len(list)):
        new_list = list.copy()
        new_list.pop(i)
        lists.append(new_list)

    return lists

def get_safe(lists: list[list]) -> int:
    result = 0

    for list in lists:
        new_lists = build_lists(list)
        for new_list in new_lists:
            if is_safe(new_list):
                result += 1
                break

    return result

def main():
    lines = get_lines("input.txt")
    lists = get_lists(lines)
    safe = get_safe(lists)

    print(safe)

if __name__ == "__main__":
    main()
