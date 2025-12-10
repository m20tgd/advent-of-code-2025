def count_paper_in_surrounding_coords(target_x, target_y, grid):
    max_y = len(grid)
    max_x = len(grid[0]) if max_y > 0 else 0
    paper_count = 0
    surrounding_coords = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            new_x, new_y = target_x + dx, target_y + dy
            if 0 <= new_x < max_x and 0 <= new_y < max_y:
                surrounding_coords.append((new_x, new_y))
    for [x, y] in surrounding_coords:
        if grid[y][x] == '@':
            paper_count += 1
    return paper_count


with open("input.txt", 'r') as file:
    accessible_paper_count = 0
    rows = [line.strip() for line in file.readlines()]
    number_of_rows = len(rows)
    number_of_columns = len(rows[0]) if rows else 0
    for y in range(number_of_rows):
        for x in range(number_of_columns):
            if rows[y][x] == '@' and count_paper_in_surrounding_coords(x, y, rows) < 4:
                accessible_paper_count += 1

print(accessible_paper_count)
