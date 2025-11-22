def get_input(filename):
    with open(filename, 'r') as fd:
        lines = fd.read().splitlines()
    grid = [list(map(int, line)) for line in lines]
    return grid


def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))


def dfs(input_grid, ref_grid, x, y, ref_val):
    if ref_grid[x][y] != 0 or input_grid[x][y] > ref_val:
        return ref_grid
    ref_grid[x][y] = 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(input_grid) and 0 <= ny < len(input_grid[0]):
            ref_grid = dfs(input_grid, ref_grid, nx, ny, input_grid[x][y])
    return ref_grid
            


def part_1():
    input_grid = get_input('input.txt')
    # print_grid(input_grid)
    ref_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    # print_grid(ref_grid)
    ref_grid = dfs(input_grid, ref_grid, 0, 0, input_grid[0][0])
    ref_grid = dfs(input_grid, ref_grid, len(input_grid) - 1, len(input_grid[0]) - 1, input_grid[-1][-1])
    print_grid(ref_grid)
    print(sum(sum(row) for row in ref_grid))


if __name__ == "__main__":
    part_1()