# filename = 'example.txt'
filename = 'input.txt'

fresh_ranges = []

with open(filename) as f:
    for line in f:
        line = line.strip('\n')
        if line == '':
            break
        start, end = line.split('-')
        fresh_ranges.append(range(int(start), int(end) + 1))

sorted_fresh_ranges = sorted(fresh_ranges, key=lambda r: r.start)

merged_ranges = []
current_range = sorted_fresh_ranges[0]

for fresh_range in sorted_fresh_ranges:
    print(f"Fresh Start: {fresh_range.start}, Fresh End: {fresh_range.stop}, Current Start: {current_range.start}, Current End: {current_range.stop}")
    if fresh_range.start <= current_range.stop:
        current_range = range(current_range.start, max(
            current_range.stop, fresh_range.stop))
    else:
        merged_ranges.append(current_range)
        current_range = fresh_range
merged_ranges.append(current_range)

fresh_id_count = 0
for merged_range in merged_ranges:
    print(len(merged_range))
    fresh_id_count += len(merged_range)

print(fresh_id_count)
