from aocd import get_data
from aocd import submit
day = 11
year = 2024
data = get_data(day=day, year=year).split()
data = list(map(int, data))

# Part 1
stored = {}

def total(stone, blinks):
    if blinks == 0:
        return 1
    elif (stone, blinks) in stored:
        return stored[(stone, blinks)]
    elif stone == 0:
        val = total(1, blinks - 1)
    elif len(str_stone := str(stone)) % 2 == 0:
        mid = len(str_stone) // 2
        val = total(int(str_stone[:mid]), blinks - 1) + total(int(str_stone[mid:]), blinks - 1)
    else:
        val = total(stone * 2024, blinks - 1)
    stored[(stone, blinks)] = val
    return val

def part1():
    return sum(total(stone, 25) for stone in data)
    
        

# print("Part 1:", part1())
submit(part1(), part="a", day=day, year=year)

# Part 2

def part2():
    return sum(total(stone, 75) for stone in data)
    

# print("Part 2:", part2())
submit(part2(), part="b", day=day, year=year)


