from aocd import get_data
from aocd import submit
from itertools import product
day = 7
year = 2024
data = get_data(day=day, year=year).split('\n')
# print(data[:10])

# Part 1

def calculate(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '$':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def is_valid_equation(value, numbers):
    num_positions = len(numbers) - 1
    for ops in product('+*', repeat=num_positions):
        if calculate(numbers, ops) == value:
            return True
    return False


def part1():
    total = 0

    for line in data:
        value, numbers = line.split(':')
        value = int(value.strip())
        numbers = [int(i) for i in numbers.split()]

        if is_valid_equation(value, numbers):
            total += value

    return total


print("Part 1:", part1())
# submit(part1(), part="a", day=day, year=year)

# Part 2

def is_valid_equation_concat(value, numbers):
    num_positions = len(numbers) - 1
    for ops in product('+$*', repeat=num_positions):
        if calculate(numbers, ops) == value:
            return True
    return False

def part2():
    total = 0

    for line in data:
        value, numbers = line.split(':')
        value = int(value.strip())
        numbers = [int(i) for i in numbers.split()]

        if is_valid_equation_concat(value, numbers):
            total += value

    return total

from time import perf_counter
start = perf_counter()
print("Part 2:", part2())
end = perf_counter()
print(end - start)
# submit(part2(), part="b", day=day, year=year)


