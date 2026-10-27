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
        if move[0] =='L':
            index -= int(move[1:])
        elif move[0] == 'R':
            index += int(move[1:])
        print(f'Moved {move[0]}, steps {move[1:]}, new index is {index}')

    print(index)


if __name__ == "__main__":
    main()