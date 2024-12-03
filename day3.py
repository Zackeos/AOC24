from aocd import get_data
from aocd import submit
day = 3
year = 2024
data = get_data(day=day, year=year)
# print(data[:10])
import re
# Part 1

    


def part1():
    pattern = r"mul\((-?\d+),(-?\d+)\)"
    matches = re.findall(pattern, data)
    return sum(int(a) * int(b) for a, b in matches)




print("Part 1:", part1())
# submit(part1(), part="a", day=day, year=year)

# Part 2

def part2():
    mul_pattern = r"mul\((-?\d+),(-?\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    mul_matches = [(m.start(), m.end(), "mul", m) for m in re.finditer(mul_pattern, data)]
    do_matches = [(m.start(), m.end(), "do") for m in re.finditer(do_pattern, data)]
    dont_matches = [(m.start(), m.end(), "don't") for m in re.finditer(dont_pattern, data)]
    all_matches = sorted(mul_matches + do_matches + dont_matches, key=lambda x: x[0])

    mul_enabled = True
    total = 0
    for match in all_matches:
        if match[2] == "mul":
            if mul_enabled:
                mul_text = data[match[0]:match[1]]
                numbers = mul_text[4:-1].split(",")
                a, b = int(numbers[0].strip()), int(numbers[1].strip())
                total += a * b
        elif match[2] == "do":
            mul_enabled = True
        elif match[2] == "don't":
            mul_enabled = False
    return total

print("Part 2:", part2())
# submit(part2(), part="b", day=day, year=year)


