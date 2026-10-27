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
    print_grid(ref_grid)
    print(sum(sum(row) for row in ref_grid))


def part_2():
    input_grid = get_input('input.txt')
    ref_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    ref_grid = dfs(input_grid, ref_grid, 0, 0, input_grid[0][0])
    ref_grid = dfs(input_grid, ref_grid, len(input_grid) - 1, len(input_grid[0]) - 1, input_grid[-1][-1])
    print_grid(ref_grid)
    print(sum(sum(row) for row in ref_grid))

def dfs_3(input_grid, ref_grid, x, y, ref_val):
    if ref_grid[x][y] != 0 or input_grid[x][y] > ref_val:
        return ref_grid
    ref_grid[x][y] = 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(input_grid) and 0 <= ny < len(input_grid[0]):
            ref_grid = dfs_3(input_grid, ref_grid, nx, ny, input_grid[x][y])
    return ref_grid


def modify_grid(input_grid, targeted_barrel):
    for x in range(len(input_grid)):
        for y in range(len(input_grid[0])):
            if targeted_barrel[x][y] == 1:
                input_grid[x][y] = -1
    return input_grid

def part_3():
    input_grid = get_input('input.txt')
    n, m = len(input_grid), len(input_grid[0])
    ret_val = 0
    for _ in range(3):
        max_val = max(max(row) for row in input_grid)
        max_barrels_exploded = 0
        targeted_barrel = list()
        for i in range(n):
            for j in range(m):
                if input_grid[i][j] == max_val:
                    ref_grid = [[0 for _ in range(m)] for _ in range(n)]
                    ref_grid = dfs_3(input_grid, ref_grid, i, j, input_grid[i][j])
                    barrels_exploded = sum(sum(row) for row in ref_grid)
                    if barrels_exploded > max_barrels_exploded:
                        max_barrels_exploded = barrels_exploded
                        targeted_barrel = ref_grid.copy()
                    elif barrels_exploded == max_barrels_exploded:
                        print("Equal barrels exploded!")
                        exit()
        ret_val += max_barrels_exploded
        input_grid = modify_grid(input_grid, targeted_barrel)
    print(ret_val)


if __name__ == "__main__":
    # part_1()
    # part_2()
    part_3()