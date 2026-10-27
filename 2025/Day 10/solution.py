def get_grid(filename):
    with open(filename, 'r') as fd:
        return fd.read().splitlines()


def get_dragon_start(grid):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 'D':
                return r, c


def get_positions(grid, target):
    positions = set()
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == target:
                positions.add((r, c))
    return positions


def move_dragon(dragon_pos: set[list[int]], max_rows: int, max_cols: int) -> set[list[int]]:
    offsets = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
    new_positions = set()

    for pos in dragon_pos:
        for offset in offsets:
            new_r = pos[0] + offset[0]
            new_c = pos[1] + offset[1]
            if 0 <= new_r < max_rows and 0 <= new_c < max_cols:
                new_positions.add((new_r, new_c))
    return new_positions


def part_1():
    grid = get_grid('input.txt')
    # print(grid)
    # init_pos = get_dragon_start(grid)
    dragon_pos = get_positions(grid, 'D')
    print(dragon_pos)
    for _ in range(4):
        dragon_pos.update(move_dragon(dragon_pos, len(grid), len(grid[0])))
    eaten_sheep = 0
    for x in dragon_pos:
        if 0 <= x[0] < len(grid) and 0 <= x[1] < len(grid[0]):
            if grid[x[0]][x[1]] == 'S':
                eaten_sheep += 1
    print(eaten_sheep)


def eliminate_sheep(dragon_pos: set[list[int]], sheep_pos: set[list[int]], safe_zones: set[list[int]], eaten_sheep: int) -> tuple[set[list[int]], int]:
    remaining_sheep = set()
    for sheep in sheep_pos:
        if sheep in dragon_pos and sheep not in safe_zones:
            continue
        remaining_sheep.add(sheep)
    # print(f'Sheep remaining: {len(remaining_sheep)}')
    return remaining_sheep, eaten_sheep + (len(sheep_pos) - len(remaining_sheep))


def move_sheep(sheep_pos: set[list[int]], max_rows: int) -> set[list[int]]:
    new_positions = set()
    for pos in sheep_pos:
        new_r = pos[0] + 1
        new_c = pos[1]
        # Sheep move down one row; if at bottom, leave grid
        if 0 <= new_r < max_rows:
            new_positions.add((new_r, new_c))
    return new_positions


def part_2():
    grid = get_grid('input.txt')

    safe_zones = get_positions(grid, '#')
    # print(safe_zones)
    dragon_pos = get_positions(grid, 'D')
    sheep_pos = get_positions(grid, 'S')
    total_eaten_sheep = 0
    for _ in range(20):
        eaten_sheep = 0
        dragon_pos = move_dragon(dragon_pos, len(grid), len(grid[0]))
        sheep_pos, eaten_sheep = eliminate_sheep(dragon_pos, sheep_pos, safe_zones, eaten_sheep)
        sheep_pos = move_sheep(sheep_pos, len(grid))
        sheep_pos, eaten_sheep = eliminate_sheep(dragon_pos, sheep_pos, safe_zones, eaten_sheep)
        total_eaten_sheep += eaten_sheep
        print(f'Eaten this round: {eaten_sheep}')
    print(f'Total eaten sheep: {total_eaten_sheep}')


if __name__ == "__main__":
    # part_1()
    part_2()