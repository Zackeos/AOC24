from aocd import get_data
from aocd import submit
day = 8
year = 2024
data = get_data(day=day, year=year).split('\n')
# print(data[:10])

# data = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............""".split('\n')

# data = """T.........
# ...T......
# .T........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........""".split('\n')

frequencyAntennas = {}
for x in range(len(data)):
    for y in range(len(data[x])):
        if data[x][y] != '.':
            if data[x][y] not in frequencyAntennas:
                frequencyAntennas[data[x][y]] = [(x, y)]
            else:
                frequencyAntennas[data[x][y]].append((x, y))
# Part 1

def valid_coord(coord):
    return 0 <= coord[0] < len(data) and 0 <= coord[1] < len(data[0])

def findantinodes(node1, node2):
    dist = ((node2[0] - node1[0]), node2[1] - node1[1])
    antinode1 = (node2[0] + dist[0], node2[1] + dist[1])
    antinode2 = (node1[0] - dist[0], node1[1] - dist[1])
    return [node for node in [antinode1, antinode2] if valid_coord(node)]


def part1():
    antinodes = set()
    for frequency in frequencyAntennas:
        for antenna in frequencyAntennas[frequency]:
            for otherAntenna in frequencyAntennas[frequency]:
                if antenna != otherAntenna:
                    antinodes.update(findantinodes(antenna, otherAntenna))
    return len(antinodes)


print("Part 1:", part1())
# submit(part1(), part="a", day=day, year=year)

# Part 2

def findantinodescontinued(node1, node2):
    nodes = []
    dist = ((node2[0] - node1[0]), node2[1] - node1[1])
    antinode1 = node2
    if valid_coord(antinode1):
        nodes.append(antinode1)
    while valid_coord(antinode1):
        antinode1 = (antinode1[0] + dist[0], antinode1[1] + dist[1])
        if valid_coord(antinode1):
            nodes.append(antinode1)
    antinode2 = node1
    if valid_coord(antinode2):
        nodes.append(antinode2)
    while valid_coord(antinode2):
        antinode2 = (antinode2[0] - dist[0], antinode2[1] - dist[1])
        if valid_coord(antinode2):
            nodes.append(antinode2)
    return nodes

def part2():
    antinodes = set()
    for frequency in frequencyAntennas:
        for antenna in frequencyAntennas[frequency]:
            for otherAntenna in frequencyAntennas[frequency]:
                if antenna != otherAntenna:
                    antinodes.update(findantinodescontinued(antenna, otherAntenna))
    return len(antinodes)

print("Part 2:", part2())

submit(part2(), part="b", day=day, year=year)


