# filename = 'example.txt'
filename = 'input.txt'


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


sums = []

with open(filename) as f:
    for index, line in enumerate(f):
        values = line.split()
        for i, value in enumerate(values):
            if index == 0:
                sums.append([value])
            else:
                sums[i].append(value)

sum_total = 0
for sum in sums:
    [*values, operator] = sum
    values = map(int, values)
    op_func = add if operator == '+' else multiply
    sum_answer = 0 if operator == '+' else 1
    for value in values:
        sum_answer = op_func(sum_answer, value)
    sum_total += sum_answer

print(sum_total)
