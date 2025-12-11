def get_highest_digit(line):
    highest_digit = None
    index = None
    for i in range(len(line)):
        if highest_digit is None or int(line[i]) > highest_digit:
            highest_digit = int(line[i])
            index = i
    return highest_digit, index


joltage = 0

# Open file and read line by line
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        digits = []
        index = 0
        line_length = len(line)
        for i in range(12, 0, -1):
            slice = line[index:line_length - i + 1]
            [highest_digit, highest_digit_index] = get_highest_digit(slice)
            digits.append(str(highest_digit))
            index += highest_digit_index + 1
        joltage += int(''.join(digits))

print(joltage)
