joltage = 0

# Open file and read line by line
with open('input.txt', 'r') as file:
    for line in file:
        digit_1 = None
        digit_2 = None
        line_length = len(line)
        for i in range(line_length - 1):
            is_last_digit = (i == line_length - 2)
            if not is_last_digit and (digit_1 is None or int(line[i]) > digit_1):
                digit_1 = int(line[i])
                digit_2 = int(line[i+1])
            elif int(line[i]) > digit_2:
                digit_2 = int(line[i])
        joltage += (digit_1 * 10) + digit_2

print(joltage)
