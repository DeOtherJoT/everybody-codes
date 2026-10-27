def get_input(filename) -> list[str]:
    with open(filename, 'r') as fd:
        return fd.read().splitlines()


def part_1():
    input_map = get_input('input.txt')
    total = 0
    offset = 0
    for idx_row in range(len(input_map) - 1):
        for idx_col in range(offset, len(input_map[0]) - offset - 1):
            if input_map[idx_row][idx_col] == 'T':
                if input_map[idx_row][idx_col + 1] == 'T':
                    total += 1
                if (offset + idx_col) % 2 == 1:
                    if input_map[idx_row + 1][idx_col] == 'T':
                        total += 1
        offset += 1
    print(total)


if __name__ == "__main__":
    part_1()