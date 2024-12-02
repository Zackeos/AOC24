from aocd import get_data
from aocd import submit
day = 1
year = 2024
data = get_data(day=day, year=year).split('\n')
print(data[:10])

lista = []
listb = []

for i in data:
    lista.append(int(i.split()[0]))
    listb.append(int(i.split()[1]))

# Part 1

def part1():
    tot = 0
    a = sorted(lista)
    b = sorted(listb)
    for x in range(len(a)):
        tot += abs(a[x]-b[x])
    return tot
        

print("Part 1:", part1())
# submit(part1(), part="a", day=day, year=2024)

# Part 2

def part2():
    bdict = {}
    for item in listb:
        if item in bdict:
            bdict[item] += 1
        else:
            bdict[item] = 1
    tot = 0
    for i in lista:
        if i in bdict:
            tot += i*bdict[i]
    return tot
    
    
print("Part 2:", part2())
# submit(part2(), part="b", day=day, year=2024)
