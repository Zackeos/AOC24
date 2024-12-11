from aocd import get_data
from aocd import submit
day = 10
year = 2024
data = get_data(day=day, year=year).split('\n')
# print(data[:10])

map = []

for line in data:
    map_row = []
    for char in line.strip():
        map_row.append(int(char))
    map.append(map_row)
# Part 1

def basictrail(x, y, end_positions):
    height = map[y][x]
    if height == 9:
        end_positions.add((x, y))
        return
    if x > 0 and map[y][x - 1] == height + 1:
        basictrail(x - 1, y, end_positions)
    if y > 0 and map[y - 1][x] == height + 1:
        basictrail(x, y - 1, end_positions)
    if x < len(map[y]) - 1 and map[y][x + 1] == height + 1:
        basictrail(x + 1, y, end_positions)
    if y < len(map) - 1 and map[y + 1][x] == height + 1:
        basictrail(x, y + 1, end_positions)

def part1():
    total_score = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                end_positions = set()
                basictrail(x, y, end_positions)
                total_score += len(end_positions)
    return total_score


print("Part 1:", part1())
# submit(part1(), part="a", day=day, year=year)

# Part 2

def hardtrail(x, y):
    height = map[y][x]
    if height == 9:
        return 1
    score = 0
    if x > 0 and map[y][x - 1] == height + 1:
        score += hardtrail(x - 1, y)
    if y > 0 and map[y - 1][x] == height + 1:
        score += hardtrail(x, y - 1)
    if x < len(map[y]) - 1 and map[y][x + 1] == height + 1:
        score += hardtrail(x + 1, y)
    if y < len(map) - 1 and map[y + 1][x] == height + 1:
        score += hardtrail(x, y + 1)
    return score

def part2():
    total_score = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                total_score += hardtrail(x, y)
    return total_score
    

print("Part 2:", part2())
submit(part2(), part="b", day=day, year=year)


