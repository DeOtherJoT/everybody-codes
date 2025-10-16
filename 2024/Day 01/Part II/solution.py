def get_input() -> str:
    with open("input.txt", "r") as file:
        return file.read().strip()


def group_up(input: str) -> list[str]:
    return [input[i : i + 2] for i in range(0, len(input), 2)]


def main():
    input = get_input()

    # split into groups of two
    groups = group_up(input)

    keys = {
        'x': 0,
        'A': 0,
        'B': 1,
        'C': 3,
        'D': 5
    }

    total = 0
    for group in groups:
        first, second = group
        if 'x' in group:
            total += keys[first] + keys[second]
        else:
            total += keys[first] + keys[second] + 2
    
    print(total)


if __name__ == "__main__":
    main()