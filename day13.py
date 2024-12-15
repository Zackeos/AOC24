from aocd import get_data
from aocd import submit
day = 13
year = 2024
data = get_data(day=day, year=year).split('\n')
# print(data[:10])

# Part 1

import re


def part1(puzzle_input):
    total = 0
    tolerance = 0.0001
    for machine in puzzle_input.split('\n\n'):
        ax, ay, bx, by, x, y = map(int, re.findall(r'(\d+)', machine))
        A = (bx*y - by*x) / (bx*ay - by*ax)
        B = (x-ax*A) / bx
        if abs(A - round(A)) < tolerance and abs(B - round(B)) < tolerance:
            total += 3*A + B


print("Part 1:", part1())
# submit(part1(), part="a", day=day, year=year)

# Part 2

def part2():
    pass
    

print("Part 2:", part2())
# submit(part2(), part="b", day=day, year=year)


