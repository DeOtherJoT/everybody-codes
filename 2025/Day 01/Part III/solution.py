def get_input() -> tuple[list[str], list[str]]:
    with open('input.txt', 'r') as fd:
        lines = fd.read().splitlines()
    
    names = lines[0].split(',')
    moves = lines[2].split(',')

    return names, moves


def swap(names: list[str], index: int) -> list[str]:
    print("Before swap:", names)
    print(f"Index: {index}, Swapping {names[0]} with {names[index]}")
    
    names[0], names[index] = names[index], names[0]
    return names


def main():
    names, moves = get_input()

    for move in moves:
        if move[0] == 'L':
            names = swap(names, -int(move[1:]) % len(names))
        elif move[0] == 'R':
            names = swap(names, (int(move[1:]) % len(names)))

    print(names[0])


if __name__ == "__main__":
    main()