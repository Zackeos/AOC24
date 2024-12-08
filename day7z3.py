from aocd import get_data
day = 7
year = 2024
data = get_data(day=day, year=year).split('\n')
import z3
from time import perf_counter

result = 156
operands = [15, 6]
s = z3.Solver()

def is_valid(result, operands):
    s.reset()
    operators = [[z3.Bool(f"op_{i},{j}") for i in range(3)] for j in range(len(operands) - 1)]

    # Only one operator type per operator
    for i in range(len(operands) - 1):
        s.add(z3.PbEq([(operators[i][0], 1), (operators[i][1], 1), (operators[i][2], 1)], 1))

    concatenation = operands[0] * 10**len(str(operands[1])) + operands[1]
    cur = z3.If(operators[0][0], operands[0] + operands[1], z3.If(operators[0][1], operands[0] * operands[1], concatenation))
    for i in range(1, len(operators)):
        concatenation = cur * 10**len(str(operands[i+1])) + operands[i+1]
        cur = z3.If(operators[i][0], cur + operands[i+1], z3.If(operators[i][1], cur * operands[i+1], concatenation))

    s.add(cur == result)

    return s.check() == z3.sat
    # if s.check() == z3.sat:
    #     m = s.model()
    #     for i in range(len(operators)):
    #         if m[operators[i][0]]:
    #             print('+', end='')
    #         elif m[operators[i][1]]:
    #             print('*', end='')
    #         else:
    #             print('||', end='')
    # else:
    #     print('no solution found')


start = perf_counter()
total = 0
for line in data:
    value, numbers = line.split(':')
    value = int(value.strip())
    numbers = [int(i) for i in numbers.split()]
    if is_valid(value, numbers):
        total += value
end = perf_counter()

print(end - start)
print(total)
