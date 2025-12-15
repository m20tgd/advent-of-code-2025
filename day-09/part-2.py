# filename = 'example.txt'
filename = 'input.txt'
# filename = 'test.txt'

### ------------------------------------------------------ ###
### ------------------------------------------------------ ###
### This is the worst and messiest code I've ever written. ###
### It only works for the full input. Needs to be -------- ###
### configured based on which way round the shape goes and ###
### where it starts ---------------------------------------###
### ------------------------------------------------------ ###
### ------------------------------------------------------ ###


def get_rect_vertices_for_points(a, b):
    [ax, ay] = a
    [bx, by] = b
    c = (bx, ay)
    d = (ax, by)
    return [
        (a, c),
        (c, b),
        (b, d),
        (d, a)
    ]


def get_rect_area_for_points(a, b):
    [ax, ay] = a
    [bx, by] = b
    x = abs(ax - bx) + 1
    y = abs(ay - by) + 1
    return x * y


def do_vertices_intersect(horizontal, vertical):
    [h1, h2] = horizontal
    [v1, v2] = vertical
    return (h1[0] >= v1[0] >= h2[0] or h1[0] <= v1[0] <= h2[0]) and (v1[1] >= h1[1] >= v2[1] or v1[1] <= h1[1] <= v2[1])


def does_horizontal_side_intersect_boundary(side, boundary):
    return do_vertices_intersect(side, boundary)


def does_vertical_side_intersect_boundary(side, boundary):
    return do_vertices_intersect(boundary, side)


def is_point_on_vertix(point, vertix):
    return (
        (vertix[0][0] <= point[0] <= vertix[1][0] or vertix[0][0] >= point[0] >= vertix[1][0]) and
        (vertix[0][1] <= point[1] <= vertix[1][1]
         or vertix[0][1] >= point[1] >= vertix[1][1])
    )


def is_point_on_vertices(point, vertices):
    for vertix in vertices:
        if is_point_on_vertix(point, vertix):
            return True
    return False


# Get Tiles
red_tiles = []
with open(filename) as file:
    for line in file:
        [x, y] = line.split(',')
        red_tiles.append((int(x), int(y)))
number_of_red_tiles = len(red_tiles)

# Get Vertices
horizontal_vertices = []
vertical_vertices = []
vertices = []
for i in range(number_of_red_tiles):
    ax, ay = red_tiles[i]
    bx, by = red_tiles[(i+1) % number_of_red_tiles]
    vertices.append(((ax, ay), (bx, by)))
    if ax == bx:
        vertical_vertices.append(((ax, ay), (bx, by)))
    else:
        horizontal_vertices.append(((ax, ay), (bx, by)))

# Get boundaries
vertical_boundaries = []
horizontal_boundaries = []
points = []
horizontal = False
add = True
number_of_vertices = len(vertices)
for i in range(number_of_vertices):
    pa, pb = vertices[i]
    next_pa, next_pb = vertices[(i + 1) % number_of_vertices]
    ############## HORIZONTAL ##################
    if horizontal:
        is_a_left = pa[0] < pb[0]
        if add:
            if is_a_left:
                # Horizontal, add, a is left
                new_a = (pa[0], pa[1] + 1)
                new_b = (pb[0], pb[1] + 1)
                if is_point_on_vertices(new_a, vertices):
                    new_a = (new_a[0] + 1, new_a[1])
                else:
                    new_a = (new_a[0] - 1, new_a[1])
                if is_point_on_vertices(new_b, vertices):
                    new_b = (new_b[0] - 1, new_b[1])
                else:
                    new_b = (new_b[0] + 1, new_b[1])
            else:
                # Horizontal, add, a is right
                new_a = (pa[0], pa[1] + 1)
                new_b = (pb[0], pb[1] + 1)
                if is_point_on_vertices(new_a, vertices):
                    new_a = (new_a[0] - 1, new_a[1])
                else:
                    new_a = (new_a[0] + 1, new_a[1])
                if is_point_on_vertices(new_b, vertices):
                    new_b = (new_b[0] + 1, new_b[1])
                else:
                    new_b = (new_b[0] - 1, new_b[1])
            horizontal_boundaries.append((new_a, new_b))
            points.append(new_a)
            points.append(new_b)
        else:
            if is_a_left:
                # Horizontal, minus, a is left
                new_a = (pa[0], pa[1] - 1)
                new_b = (pb[0], pb[1] - 1)
                if is_point_on_vertices(new_a, vertices):
                    new_a = (new_a[0] + 1, new_a[1])
                else:
                    new_a = (new_a[0] - 1, new_a[1])
                if is_point_on_vertices(new_b, vertices):
                    new_b = (new_b[0] - 1, new_b[1])
                else:
                    new_b = (new_b[0] + 1, new_b[1])
            else:
                # Horizontal, minus, a is right
                new_a = (pa[0] + 1, pa[1] - 1)
                new_b = (pb[0] - 1, pb[1] - 1)
                if is_point_on_vertices(new_a, vertices):
                    new_a = (new_a[0] - 1, new_a[1])
                else:
                    new_a = (new_a[0] + 1, new_a[1])
                if is_point_on_vertices(new_b, vertices):
                    new_b = (new_b[0] + 1, new_b[1])
                else:
                    new_b = (new_b[0] - 1, new_b[1])
            horizontal_boundaries.append((new_a, new_b))

            points.append(new_a)
            points.append(new_b)
        add = True if next_pa[1] < pa[1] or next_pb[1] > pa[1] else False
    ############## VERTICAL ##################
    else:
        is_a_low = pa[1] < pb[1]
        if add:
            if is_a_low:
                # Vertical, add, a is low
                new_a = (pa[0] + 1, pa[1])
                new_b = (pb[0] + 1, pb[1])
                if is_point_on_vertices(new_a, vertices):
                    new_a = (new_a[0], new_a[1] - 1)
                else:
                    new_a = (new_a[0], new_a[1] - 1)
                if is_point_on_vertices(new_b, vertices):
                    new_b = (new_b[0], new_b[1] + 1)
                else:
                    new_b = (new_b[0], new_b[1] + 1)
            else:
                # Vertical, add, a is high
                new_a = (pa[0] + 1, pa[1])
                new_b = (pb[0] + 1, pb[1])
                if is_point_on_vertices(new_a, vertices):
                    new_a = (new_a[0], new_a[1] - 1)
                else:
                    new_a = (new_a[0], new_a[1] + 1)
                if is_point_on_vertices(new_b, vertices):
                    new_b = (new_b[0], new_b[1] + 1)
                else:
                    new_b = (new_b[0], new_b[1] - 1)
            vertical_boundaries.append((new_a, new_b))

            points.append(new_a)
            points.append(new_b)
        else:
            if is_a_low:
                # Vertical, minus, a is low
                new_a = (pa[0] - 1, pa[1])
                new_b = (pb[0] - 1, pb[1])
                if is_point_on_vertices(new_a, vertices):
                    new_a = (new_a[0], new_a[1] + 1)
                else:
                    new_a = (new_a[0], new_a[1] - 1)
                if is_point_on_vertices(new_b, vertices):
                    new_b = (new_b[0], new_b[1] - 1)
                else:
                    new_b = (new_b[0], new_b[1] + 1)
            else:
                # Vertical, minus, a is high
                new_a = (pa[0] - 1, pa[1])
                new_b = (pb[0] - 1, pb[1])
                if is_point_on_vertices(new_a, vertices):
                    new_a = (new_a[0], new_a[1] - 1)
                else:
                    new_a = (new_a[0], new_a[1] + 1)
                if is_point_on_vertices(new_b, vertices):
                    new_b = (new_b[0], new_b[1] + 1)
                else:
                    new_b = (new_b[0], new_b[1] - 1)
            vertical_boundaries.append((new_a, new_b))

            points.append(new_a)
            points.append(new_b)
        add = True if next_pa[0] > pa[0] or next_pb[0] < pa[0] else False
    horizontal = not horizontal


# Get rectanges
rectangles = []
for i in range(len(red_tiles)):
    if i == len(red_tiles) - 1:
        break
    for j in range(i+1, len(red_tiles)):
        rect_area = get_rect_area_for_points(red_tiles[i], red_tiles[j])
        rect_vertices = get_rect_vertices_for_points(
            red_tiles[i], red_tiles[j])
        rectangles.append(
            (red_tiles[i], red_tiles[j], rect_area, rect_vertices))
rectangles = sorted(rectangles, key=lambda r: r[2], reverse=True)

largest_size = 0
for rect in rectangles:
    a, b, c, d = rect[3]
    if any(does_horizontal_side_intersect_boundary(a, boundary) for boundary in vertical_boundaries):
        continue
    if any(does_vertical_side_intersect_boundary(b, boundary) for boundary in horizontal_boundaries):
        continue
    if any(does_horizontal_side_intersect_boundary(c, boundary) for boundary in vertical_boundaries):
        continue
    if any(does_vertical_side_intersect_boundary(d, boundary) for boundary in horizontal_boundaries):
        continue
    largest_size = rect[2]
    print(rect[3])
    break

print(largest_size)
