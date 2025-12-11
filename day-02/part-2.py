import re

invalid_id_sum = 0

# Open file and read line by line
with open('input-2.txt', 'r') as file:
    data = file.readline()
    product_ids = data.split(',')
    for id in product_ids:
        [startId, endId] = id.split('-')
        for i in range(int(startId), int(endId) + 1):
            id = str(i)
            match = re.search(r'^(\d+)\1+$', id)
            if match:
                invalid_id_sum += i

print(invalid_id_sum)
