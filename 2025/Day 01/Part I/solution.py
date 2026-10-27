def get_input() -> tuple[list[str], list[str]]:
    with open('input.txt', 'r') as fd:
        lines = fd.read().splitlines()

    names = lines[0].split(',')
    moves = lines[2].split(',')

    return names, moves


def main():
    names, moves = get_input()

    index = 0
    for move in moves:
        if move[0] == 'L':
            index = max(0, index - int(move[1]))
        if move[0] == 'R':
            index = min(len(names) - 1, index + int(move[1]))

    print(names[index])


if __name__ == "__main__":
    main()