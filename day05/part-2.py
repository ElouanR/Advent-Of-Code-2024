# Advent of Code 2024 - Day 5 - Part 2
# https://adventofcode.com/2024/day/5#part2

def get_rules(file_name: str) -> tuple[list[str], list[list[int]]]:
    with open(file_name, "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    page_order = lines[:lines.index('')]
    updates = lines[lines.index('') + 1:]
    updates = [list(map(int, line.split(','))) for line in updates]

    return page_order, updates

def page_order_dict(page_order: list) -> dict[int, list[int]]:
    page_order_dict = {}

    for page in page_order:
        page = page.split('|')
        nb1 = int(page[0])
        nb2 = int(page[1])

        if nb1 not in page_order_dict:
            page_order_dict[nb1] = []

        page_order_dict[nb1].append(nb2)

    return page_order_dict

def get_incorrect_updates(page_order: dict[int, list[int]], updates: list[list[int]]) -> list[list[int]]:
    incorrect_updates = []

    for update in updates:
        correct_update = True
        for page in update:
            i = update.index(page)
            if not all(p in page_order.get(page, []) for p in update[i + 1:]):
                correct_update = False
                break

        if not correct_update:
            incorrect_updates.append(update)

    return incorrect_updates

def sort_incorrect_updates(page_order: dict[int, list[int]], incorrect_updates: list[list[int]]) -> int:
    result = 0

    for update in incorrect_updates:
        corrected_update = []
        while len(update) > 0:
            for page in update:
                i = update.index(page)
                if all(p in page_order.get(page, []) for p in update[i + 1:]):
                    corrected_update.append(page)
                    update.remove(page)
                    break

        result += corrected_update[len(corrected_update) // 2]

    return result

def main():
    page_order, updates = get_rules("input.txt")
    page_order = page_order_dict(page_order)
    incorrect_updates = get_incorrect_updates(page_order, updates)
    result = sort_incorrect_updates(page_order, incorrect_updates)

    print(result)

if __name__ == "__main__":
    main()
