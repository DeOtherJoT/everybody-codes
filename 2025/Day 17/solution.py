from math import sqrt

def get_input(filename: str) -> list[str]:
    with open(filename, 'r') as fd:
        return fd.read().splitlines()


def print_grid(grid: list[str]) -> None:
    for line in grid:
        print(line)


def find_volcano(grid: list[str]) -> tuple[int, int]:
    for row in grid:
        if '@' in row:
            return (grid.index(row), row.index('@'))
    raise ValueError("No volcano found in the grid")


def is_burnt(volcano: tuple[int, int], cell: tuple[int, int]) -> bool:
    v_x = volcano[0]
    v_y = volcano[1]
    c_x = cell[0]
    c_y = cell[1]

    n_x = v_x - c_x
    n_y = v_y - c_y
    distance = sqrt(n_x**2 + n_y**2)
    return distance <= 10


def part_1():
    input_grid = get_input('input.txt')
    # print_grid(input_grid)
    volcano = find_volcano(input_grid)
    # print(volcano)
    total = 0
    for r_idx, row in enumerate(input_grid):
        for c_idx, cell in enumerate(row):
            if (r_idx, c_idx) == volcano:
                continue
            if is_burnt(volcano, (r_idx, c_idx)):
                total += int(cell)
    print(total)


def get_range(volcano: tuple[int, int], cell: tuple[int, int]) -> int:
    v_x = volcano[0]
    v_y = volcano[1]
    c_x = cell[0]
    c_y = cell[1]

    n_x = v_x - c_x
    n_y = v_y - c_y
    distance = sqrt(n_x**2 + n_y**2)
    return int(distance)


def part_2():
    input_grid = get_input('input.txt')
    volcano = find_volcano(input_grid)
    print(volcano)
    sums = [0 for _ in range(volcano[0])]
    for r_idx, row in enumerate(input_grid):
        for c_idx, cell in enumerate(row):
            if (r_idx, c_idx) == volcano:
                continue
            dist = get_range(volcano, (r_idx, c_idx))
            print(f"Cell: {(r_idx, c_idx)} ")
            print(dist)
            if dist < len(sums):
                sums[dist] += int(cell)
    max_sum = max(sums)
    max_range = sums.index(max_sum)
    print(f"Max range: {max_range} with sum: {max_sum}")

if __name__ == "__main__":
    # part_1()
    part_2()