from aocd import get_data
from aocd import submit
day = 5
year = 2024
data = get_data(day=day, year=year).split('\n\n')
with open("day5example.txt") as f:
    data = f.read().split('\n\n')
order_rules = data[0].split("\n")
updates = data[1].split("\n")
rules = {}
for rule in order_rules:
    rule = rule.split("|")
    if rule[1] not in rules:
        rules[rule[1]] = [rule[0]]
    else:
        rules[rule[1]].append(rule[0])

def part1():
    sum = 0
    for update in updates:
        update = update.split(",")
        sorted_update = sorted(update, key=lambda page: len([rule for rule in rules.get(page, []) if rule in update]))
        if update != sorted_update:
            continue
        sum += int(update[len(update) // 2])

    return sum


print("Part 1:", part1())
# submit(part1(), part="a", day=day, year=year)

# Part 2

def part2():
    sum = 0
    for update in updates:
        update = update.split(",")
        sorted_update = sorted(update, key=lambda page: len([rule for rule in rules.get(page, []) if rule in update]))

        if update == sorted_update:
            continue

        middle_page = sorted_update[len(sorted_update) // 2]
        sum += int(middle_page)
        
    return sum
    

print("Part 2:", part2())
# submit(part2(), part="b", day=day, year=year)


