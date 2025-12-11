# filename = 'example.txt'
filename = 'input.txt'

with open(filename) as file:
    manifold = file.readlines()

start_index = manifold[0].find('S')

timeline_count = 1
tachyon_indexes = {start_index: 1}
for line_index, line in enumerate(manifold):
    if line_index == 0:
        continue
    new_indexes = dict()
    for [i, count] in tachyon_indexes.items():
        if line[i] == '.':
            existing = new_indexes.get(i)
            new_indexes[i] = existing + count if existing else count
        else:
            timeline_count += (1 * count)
            existing = new_indexes.get(i-1)
            new_indexes[i-1] = existing + count if existing else count
            existing = new_indexes.get(i+1)
            new_indexes[i+1] = existing + count if existing else count
    tachyon_indexes = new_indexes

print(timeline_count)
