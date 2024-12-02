from aocd import get_data
from aocd import submit
day = 2
year = 2024
data = get_data(day=day, year=year).split('\n')
data = [[int(i) for i in line.split()] for line in data]


# Part 1
def is_safe(line):
    differences = [line[i + 1] - line[i] for i in range(len(line) - 1)]

    increasing = all(1 <= diff <= 3 for diff in differences)
    decreasing = all(-3 <= diff <= -1 for diff in differences)
    return increasing or decreasing

def part1():
    total = 0
    for item in data:
        if is_safe(item):
            total += 1
    return total

print("Part 1:", part1())
# submit(part1(), part="a", day=day, year=year)

# Part 2

def is_safe_special(line):
    if is_safe(line):
        return True
    for i in range(len(line)):
        changed_line = line[:i] + line[i+1:]
        if is_safe(changed_line):
            return True

    return False

def part2():
    total = 0
    for item in data:
        if is_safe_special(item):
            total += 1
    return total

print("Part 2:", part2())

# better solution p2

# :(



# print("Part 2 better:", part2_better())

# submit(part2(), part="b", day=day, year=year)


