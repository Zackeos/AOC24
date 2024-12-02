from aocd import get_data
from aocd import submit
from datetime import datetime
today = datetime.today()
day = 2
year = 2024
data = get_data(day=day, year=year).split('\n')
data = [[int(i) for i in line.split()] for line in data]


# Part 1
def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

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

def is_safe_special(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        changed_report = report[:i] + report[i+1:]
        if is_safe(changed_report):
            return True

    return False

def part2():
    total = 0
    for item in data:
        if is_safe_special(item):
            total += 1
    return total
    
    

print("Part 2:", part2())
# submit(part2(), part="b", day=day, year=year)


