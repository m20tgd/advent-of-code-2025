# filename = 'example.txt'
filename = 'input.txt'


def get_rect_area_for_points(a, b):
    [ax, ay] = a
    [bx, by] = b
    x = abs(ax - bx) + 1
    y = abs(ay - by) + 1
    return x * y


red_tiles = []
with open(filename) as file:
    for line in file:
        [x, y] = line.split(',')
        red_tiles.append((int(x), int(y)))

biggest_area = 0
for i in range(len(red_tiles)):
    if i == len(red_tiles) - 1:
        break
    for j in range(i+1, len(red_tiles)):
        rect_area = get_rect_area_for_points(red_tiles[i], red_tiles[j])
        if rect_area > biggest_area:
            biggest_area = rect_area

print(f"Answer: {biggest_area}")
