def get_input() -> tuple[list[str], list[str]]:
    with open ('input.txt', 'r') as fd:
        lines = fd.read().splitlines()

    runes = lines[0].split(':')[1].split(',')
    rows = lines[2:]

    return runes, rows


def print_grid(grid: list[list[str]]) -> None:
    for row in grid:
        print(' '.join(row))


def check_rows(runes: list[str], rev_runes: list[str], input_grid: list[str], seen_grid: list[list[str]]) -> list[list[str]]:
    for r_idx, row in enumerate(input_grid):
        for rune in runes:
            looped_line = row + row[:len(rune)-1]

    return seen_grid


def main():
    runes, input_grid = get_input()

    seen_grid = [['0' for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]
    # print_grid(seen_grid)
    rev_runes = [rune[::-1] for rune in runes]

    seen_grid = check_rows(runes, rev_runes, input_grid, seen_grid)


if __name__ == "__main__":
    main()