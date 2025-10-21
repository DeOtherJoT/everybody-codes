def get_input() -> list[list[str]]:
    with open('input.txt', 'r') as fd:
        return [list(line) for line in fd.read().splitlines()]


def print_map(input_map: list[list[str]]) -> None:
    for line in input_map:
        print(line)


def check_pos(input_map: list[list[str]], row: int, col: int, level: int) -> bool:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if input_map[r][c] not in [str(level), str(level - 1)]:
            return False
    return True


def process_map(input_map: list[list[str]], level: int) -> list[list[str]]:
    changes = False
    
    if level == 1:
        for row in range(len(input_map)):
            for col in range(len(input_map[row])):
                if input_map[row][col] == '#':
                    input_map[row][col] = '1'
        return process_map(input_map, level + 1)
    else:
        for row in range(len(input_map)):
            for col in range(len(input_map[row])):
                if input_map[row][col] == str(level - 1):
                    if check_pos(input_map, row, col, level):
                        input_map[row][col] = str(level)
                        changes = True
        if changes:
            return process_map(input_map, level + 1)
        return input_map

def main():
    input_map = get_input()
    # print_map(input_map)

    processed_map = process_map(input_map, 1)

    print_map(processed_map)

    total = 0
    for line in processed_map:
        for char in line:
            try:
                total += int(char)
            except ValueError:
                pass
    print(total)


if __name__ == "__main__":
    main()