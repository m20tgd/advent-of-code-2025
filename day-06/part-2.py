# filename = 'example.txt'
filename = 'input.txt'


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


rows = []
with open(filename) as f:
    for line_index, line in enumerate(f):
        line = line.strip('\n')
        line_length = len(line)
        for col_index in range(line_length-1, -1, -1):
            char = line[col_index]
            if line_index == 0:
                rows.append([char])
            else:
                rows[line_length - col_index - 1].append(char)

all_sums = []
current_sum = []
for row in rows:
    value = "".join(row[:-1]).strip()
    if value:
        current_sum.append(value)
    operator = row[-1].strip()
    if operator:
        current_sum.append(operator)
        all_sums.append(current_sum)
        current_sum = []

sum_total = 0
for sum in all_sums:
    [*values, operator] = sum
    values = map(int, values)
    op_func = add if operator == '+' else multiply
    sum_answer = 0 if operator == '+' else 1
    for value in values:
        sum_answer = op_func(sum_answer, value)
    sum_total += sum_answer

print(sum_total)
