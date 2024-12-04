from aocd import get_data
from aocd import submit
day = 4
year = 2024
data = get_data(day=day, year=year).split('\n')
# print(data[:10])

# Part 1

word = "XMAS"
rows = len(data)
cols = len(data[0])

def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

def check_direction(x, y, dx, dy):
        for k in range(len(word)):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid(nx, ny) or data[nx][ny] != word[k]:
                return False
        return True

def part1():
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1),(-1, -1), (1, -1), (-1, 1)]
    total = 0
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_direction(i, j, dx, dy):
                    total += 1
    return total


print("Part 1:", part1())
# submit(part1(), part="a", day=day, year=year)

# Part 2

rows = len(data)
cols = len(data[0])

def check_x_mas(center_x, center_y):
    top_left = (center_x - 1, center_y - 1)
    top_right = (center_x - 1, center_y + 1)
    bottom_left = (center_x + 1, center_y - 1)
    bottom_right = (center_x + 1, center_y + 1)

    if not (is_valid(*top_left) and is_valid(*top_right) and is_valid(*bottom_left) and is_valid(*bottom_right)):
        return False
    diag1 = data[top_left[0]][top_left[1]] + data[center_x][center_y] + data[bottom_right[0]][bottom_right[1]]
    diag2 = data[top_right[0]][top_right[1]] + data[center_x][center_y] + data[bottom_left[0]][bottom_left[1]]
    words = ["MAS", "SAM"]
    return (diag1 in words) and (diag2 in words)

def part2():
    total = 0
    for i in range(1, rows - 1): 
        for j in range(1, cols - 1):
            if check_x_mas(i, j):
                total += 1

    return total


print("Part 2:", part2())
# submit(part2(), part="b", day=day, year=year)


