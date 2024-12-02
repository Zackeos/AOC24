from aocd import get_data
from aocd import submit
from datetime import datetime
today = datetime.today()
day = 15
year = 2024
data = get_data(day=day, year=year).split('\n')
print(data[:10])

# Part 1

def part1():
    pass


print("Part 1:", part1())
# submit(part1(), part="a", day=day, year=year)

# Part 2

def part2():
    pass
    

print("Part 2:", part2())
# submit(part2(), part="b", day=day, year=year)


