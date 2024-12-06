from aocd import get_data
from aocd import submit
day = 6
year = 2024
data = get_data(day=day, year=year).split('\n')

# data = [
#     "....#.....",
#     ".........#",
#     "..........",
#     "..#.......",
#     ".......#..",
#     "..........",
#     ".#..^.....",
#     "........#.",
#     "#.........",
#     "......#..."
# ]

# Part 1
directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
map_data = []
guard_pos = None
guard_dir = None

for x, row in enumerate(data):
    map_row = []
    for y, cell in enumerate(row):
        if cell in directions:
            guard_pos = (x, y)
            guard_dir = directions[cell]
            map_row.append(".")
        else:
            map_row.append(cell)
    map_data.append(map_row)
    

def part1(map_data):
    right_turns = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
    rows, cols = len(map_data), len(map_data[0])
    visited_positions = set()
    visited_direction_positions = set()

    current_pos = guard_pos
    current_dir = guard_dir

    while 0 <= current_pos[0] < rows and 0 <= current_pos[1] < cols:
        if (current_pos, current_dir) in visited_direction_positions:
            return "Loop"
        visited_direction_positions.add((current_pos, current_dir))
        visited_positions.add(current_pos)

        next_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])
        if next_pos[0] < 0 or next_pos[0] >= rows or next_pos[1] < 0 or next_pos[1] >= cols:
            break
        if 0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols and map_data[next_pos[0]][next_pos[1]] != "#":
            current_pos = next_pos
        else:
            current_dir = right_turns[current_dir]
    return len(visited_positions)


print("Part 1:", part1(map_data))
# submit(part1(), part="a", day=day, year=year)

# Part 2

def part2():
    total = 0
    for y in range(len(map_data)):
        for x in range(len(map_data[y])):
            if (x, y) == guard_pos:
                continue
            if map_data[y][x] == ".":
                new_map = [row.copy() for row in map_data]
                new_map[y][x] = "#"
                if part1(new_map) == "Loop":
                    total += 1
    return total
            
    

print("Part 2:", part2())
# submit(part2(), part="b", day=day, year=year)


