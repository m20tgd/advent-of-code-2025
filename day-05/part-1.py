# filename = 'example.txt'
filename = 'input.txt'

fresh_ranges = []
ids = []
fresh_ids_count = 0

with open(filename) as f:
    # Get fresh ranges
    for line in f:
        line = line.strip('\n')
        if line == '':
            break
        start, end = line.split('-')
        fresh_ranges.append(range(int(start), int(end) + 1))
    # Get ids
    for line in f:
        line = line.strip('\n')
        ids.append(int(line))

for id in ids:
    if any(id in fresh_range for fresh_range in fresh_ranges):
        fresh_ids_count += 1

print(fresh_ids_count)
