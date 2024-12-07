# Advent of Code 2024 - Day 7 - Part 1
# https://adventofcode.com/2024/day/7#part1

from itertools import product

def get_equations(file_name: str) -> list[tuple[int, list[int]]]:
    """
    Get the equations from the file.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        equations = file.readlines()

    equations = [line.strip() for line in equations]
    equations = [equation.split(": ") for equation in equations]
    equations = [
        (int(equation[0]),
        [int(num) for num in equation[1].split(" ")]) for equation in equations
    ]

    return equations

def get_operator_combinations(length: int) -> list[list[str]]:
    """
    Get the operator combinations for the equation.
    """
    operators = ["+", "*"]
    operator_combinations = list(product(operators, repeat=length - 1))
    return operator_combinations

def check_equation(equation: tuple[int, list[int]]) -> bool:
    """
    Check if the equation is valid.
    """
    target = equation[0]
    numbers = equation[1]
    operator_combinations = get_operator_combinations(len(numbers))

    for operator_combination in operator_combinations:
        result = numbers[0]

        for i, op in enumerate(operator_combination):
            num = numbers[i + 1]
            if op == "+":
                result += num
            elif op == "*":
                result *= num

        if result == target:
            return True

    return False

def get_calibration_value(equations: list[tuple[int, list[int]]]) -> int:
    """
    Get the calibration value for the equations.
    """
    result = 0

    for equation in equations:
        if check_equation(equation):
            result += equation[0]

    return result

def main():
    """
    Main function.
    """
    equations = get_equations("input.txt")
    calibration_value = get_calibration_value(equations)

    print(calibration_value)

if __name__ == "__main__":
    main()
