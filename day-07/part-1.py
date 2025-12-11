# filename = 'example.txt'
filename = 'input.txt'

with open(filename) as file:
    manifold = file.readlines()

start_index = manifold[0].find('S')

split_count = 0
tachyon_indexes = set({start_index})
for line_index, line in enumerate(manifold):
    if line_index == 0:
        continue
    new_indexes = set()
    for i in tachyon_indexes:
        if line[i] == '.':
            new_indexes.add(i)
        else:
            split_count += 1
            new_indexes.add(i-1)
            new_indexes.add(i+1)
    tachyon_indexes = new_indexes

print(split_count)
