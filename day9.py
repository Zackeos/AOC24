from aocd import get_data
from aocd import submit
day = 9
year = 2024
data = get_data(day=day, year=year)
# print(data)
# data = "2333133121414131402"

# Part 1

goal_len = sum([int(data[x]) for x in range(len(data)) if x % 2 == 0])

def spaced_file():
    spaced = []
    current_num = 0
    for x in range(len(data)):
        if x % 2 == 0:
            spaced.extend([current_num]*int(data[x]))
            current_num += 1
        else: 
            spaced.extend(["."] * int(data[x]))
    return spaced



def part1():
    total = 0
    free_spaces = []
    spaced = spaced_file()
    for index, item in enumerate(spaced[:goal_len]):
        if item == ".":
            free_spaces.append(index)
        elif index < goal_len:
            total += int(item)*index
    for item in spaced[goal_len:][::-1]:
        if item == ".":
            free_spaces.append(index)
        else:
            total += free_spaces.pop(0)*int(item)
    return total



print("Part 1:", part1())
# submit(part1(), part="a", day=day, year=year)

# Part 2
def pointers_files():
    files = []
    count = 0
    for i in range(len(data)):
        if i % 2 == 0:
            files.append((count, count + int(data[i]), i // 2))  # Add file ID as third element
            count += int(data[i])
        else:
            count += int(data[i])
    return files

def part2():
    spaced = spaced_file()
    files = pointers_files()
    files.sort(key=lambda x: x[2], reverse=True)

    for start, end, file_id in files:
        file_size = end - start
        free_span_start = None
        free_span_length = 0

        for i in range(len(spaced)):
            if spaced[i] == ".":
                if free_span_start is None:
                    free_span_start = i
                free_span_length += 1

                if free_span_length >= file_size:
                    break
            else:
                free_span_start = None
                free_span_length = 0

        if free_span_length >= file_size and free_span_start is not None and free_span_start < start:
            for i in range(start, end):
                spaced[i] = "."
            for i in range(free_span_start, free_span_start + file_size):
                spaced[i] = file_id

    total = 0
    for i, block in enumerate(spaced):
        if block != ".":
            total += i * int(block)

    return total

    

print("Part 2:", part2())
submit(part2(), part="b", day=day, year=year)


